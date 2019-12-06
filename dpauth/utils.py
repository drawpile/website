from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError

import hashlib
import PIL

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


@deconstructible
class AvatarValidator:
    def __init__(self, max_dims=(128,128)):
        self.max_dims = max_dims
    
    def __call__(self, data):
        img = PIL.Image.open(data)
        w, h = img.size
        if w > self.max_dims[0] or h > self.max_dims[1]:
            raise ValidationError("Image too big! Max size is %dx%d" % self.max_dims)
