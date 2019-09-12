from instapy_cli import client
import os
import time
from os import listdir
from os.path import isfile, join


username = '_xcel_ior'
password = 'Cooligna77'
path = 'queue/'
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))] # onlyfiles is an array containing the filenames of all queued photos
n = 0
secondsinaday = 86400
timespace = 20

text = '#streetphotography'

def publish(image, caption):
    # publishes image using photo path(image) and a caption
    with client(username, password) as cli:
        cli.upload('queue/' + image, caption)
    print('Published')

while __name__ == '__main__':
    print(onlyfiles[n])
    publish(onlyfiles[n], text)
    n += 1
    time.sleep(timespace)
