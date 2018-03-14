from django.core.files.uploadedfile import SimpleUploadedFile

import zipfile
import hashlib

import PIL
import magic

from io import BytesIO

import logging
logger = logging.getLogger(__name__)

def identify_picture_type(upload):
    """Check if the uploaded file is of a supported picture type.
    
    Returns a (mime type, suffix) tuple, or None if file is not recognized.

    Possible return values:
    - ("image/jpeg", "jpeg")
    - ("image/png", "png")
    - ("image/openraster", "ora")
    - None (if not recognized)
    """
    chunk = next(upload.chunks(1024))
    
    mime = magic.from_buffer(chunk, mime=True)
    
    if mime in ('image/jpeg', 'image/png'):
        return (mime, mime[mime.index('/')+1:])

    elif mime == 'application/zip' and is_openraster(upload):
        return ('image/openraster', 'ora')
        
    logger.warning("Unidentified picture: %s", mime)

    return None


def is_openraster(upload):
    """Check if the uploaded file is an OpenRaster file. In addition to the mimetype
    file, it should contain mergedimage.png
    """

    # TODO use actual file if one exists.
    with zipfile.ZipFile(upload, 'r') as zf:
        
        # First, check the mimetype file
        try:
            info = zf.getinfo('mimetype')
        except KeyError:
            return False
        
        EXPECTED_MIMETYPE = b'image/openraster'
        if info.file_size != len(EXPECTED_MIMETYPE):
            return False
        
        with zf.open('mimetype', 'r') as mt:
            if mt.read() != EXPECTED_MIMETYPE:
                return False
        
        # Check that other required files also exist
        files = zf.namelist()
        
        # TODO validate these
        if 'mergedimage.png' not in files:
            return False
        
        if 'stack.xml' not in files:
            return False
        
        if 'Thumbnails/thumbnail.png' not in files:
            return False
        
    return True


def make_thumbnail(upload):
    """Generate a standard thumbnail for an uploaded picture
    """
    if upload.content_type == 'image/openraster':
        with zipfile.ZipFile(upload, 'r') as zf:
            with zf.open('Thumbnails/thumbnail.png', 'r') as thumb:
                return _make_image_thumbnail(thumb)

    elif upload.content_type.startswith('image/'):
        return _make_image_thumbnail(upload)

    else:
        raise ValueError("Unhandled content type: " + upload.content_type)

            
def _make_image_thumbnail(imagefile):
    img = PIL.Image.open(imagefile)
    
    TARGET_HEIGHT = 256
    MAX_WIDTH = 512
    
    w, h = img.size
    
    # Scale down to thumbnail height
    if h > TARGET_HEIGHT:
        scale = h / TARGET_HEIGHT
        thumb_size = (int(w / scale), TARGET_HEIGHT)
        img = img.resize(thumb_size, PIL.Image.BICUBIC)

    # Convert to RGB format and center if the image is too short
    if img.mode != 'RGB' or img.size[1] < TARGET_HEIGHT:
        img2 = PIL.Image.new("RGB", (w, TARGET_HEIGHT), (255, 255, 255))
        img2.paste(img, (0, (TARGET_HEIGHT - img.size[1])//2))
        img = img2

    # Crop if too wide
    if img.size[0] > MAX_WIDTH:
        img = img.crop(((img.size[0] - MAX_WIDTH)/2, 0, (img.size[0] - MAX_WIDTH)/2 + MAX_WIDTH, img.size[1]))
    
    return _image_to_upload(img)

        
def downscale_if_necessary(upload):
    """Generate the downscaled version of an image file.
    If the file format is suitable and the image is small enough,
    no downscaled version is generated.
    """
    if upload.content_type == 'image/openraster':
        # A downscaled version must always be generated for ORA files,
        # since web browsers do not support this format.
        with zipfile.ZipFile(upload, 'r') as zf:
            with zf.open('mergedimage.png', 'r') as thumb:
                return _downscale_image_if_necessary(thumb, force=True)

    elif upload.content_type.startswith('image/'):
        return _downscale_image_if_necessary(upload)

    else:
        raise ValueError("Unhandled content type: " + upload.content_type)


def _downscale_image_if_necessary(imagefile, force=False):
    img = PIL.Image.open(imagefile)
    
    MAX_WIDTH = 1600
    MAX_HEIGHT = 900
    w, h = img.size
    if not force and w <= MAX_WIDTH and h <= MAX_HEIGHT:
        # small enough
        return None

        
    img.thumbnail((MAX_WIDTH, MAX_HEIGHT))
    
    if img.mode != 'RGB':
        img2 = PIL.Image.new("RGB", img.size, (255, 255, 255))
        img2.paste(img)
        img = img2
    
    return _image_to_upload(img)


def _image_to_upload(image):
    buf = BytesIO()
    image.save(buf, 'JPEG')
    buf = buf.getvalue()
    
    h = hashlib.sha1()
    h.update(buf)
    
    return SimpleUploadedFile(h.hexdigest() + '.jpeg', buf, 'image/jpeg')
