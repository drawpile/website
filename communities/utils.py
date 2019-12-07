from django.utils.deconstruct import deconstructible
from django.core.files.uploadedfile import SimpleUploadedFile

from io import BytesIO

import PIL
import hashlib


@deconstructible
class UploadNameFromContent:
    """A Django FileField upload_to handler that
    generates the filename from the hash of the file content.
    The original file extension (if any) is included.
    """
    def __init__(self, basepath, filefield, alg='sha1'):
        self.basepath = basepath
        self.filefield = filefield
        self.alg = alg

        if self.basepath and self.basepath[-1] != '/':
            self.basepath = self.basepath + '/'

    def file_hash(self, file):
        h = hashlib.new(self.alg)
        for chunk in file.chunks():
            h.update(chunk)

        return h.hexdigest()

    def __call__(self, instance, original_filename):
        f = getattr(instance, self.filefield)

        try:
            ext = original_filename[original_filename.rindex('.'):]
        except ValueError:
            ext = ''

        return self.basepath + self.file_hash(f) + ext


def downscale_image_if_necessary(imagefile, max_size):
    img = PIL.Image.open(imagefile)
    
    w, h = img.size
    if w <= max_size[0] and h <= max_size[1]:
        return imagefile

    img.thumbnail(max_size)
    
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