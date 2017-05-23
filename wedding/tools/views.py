import pdb
import os

from django.shortcuts import render
from django.http import HttpResponse
from lechi import settings

from PIL import Image
def create_thumbnail(request): 
    dirs = os.path.join(settings.MEDIA_ROOT, 'kb')
    files = [f for f in os.listdir(dirs) if os.path.isfile(os.path.join(dirs, f))] 
    thumbnailpath = os.path.join(settings.MEDIA_ROOT, 'thumbnail','kb')
    if not os.path.isdir(thumbnailpath):
        os.makedirs(thumbnailpath)
    for f in files:
        f = os.path.join(dirs, f) 
        image = Image.open(f)
        image.thumbnail(settings.THUMBNAIL_SIZE)
        
        thumbnailname = os.path.join(thumbnailpath, os.path.basename(f))
        image.save(thumbnailname)
    return HttpResponse(len(files))
