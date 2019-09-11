from instapy_cli import client
import os
from os import listdir
from os.path import isfile, join

username = '_xcel_ior'
password = 'Cooligna77'
path = 'queue/'
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
#onlyfiles is an array containing the filenames of all queued photos

def publish(image, caption):
    #publishes image using photo path(image) and a caption, it also deletes the image from the queue folder
    with client(username, password) as cli:
        cli.upload('queue/' + image, caption)
    os.remove('queue/' + image)

text = 'This is just a test'

publish(onlyfiles[0], text)
