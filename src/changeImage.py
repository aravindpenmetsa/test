#!/usr/bin/env python3

import os
import sys
from PIL import Image

# Python program to multiply two numbers
def change_ext(file_path, new_ext):
    if len(file_path) <= 0:
        raise ValueError('file_path is empty')
    if type(file_path) != str or type(new_ext) != str:
        return TypeError
    path_and_filename = os.path.splitext(file_path)[0]
    print(type(path_and_filename), "path_and_filename: ", path_and_filename)
    return path_and_filename + new_ext

def convert_image_to_JPEG(file_path):
    ''' Converts the provided image to JPEG format 600 X 400.
        Works only on absolute path.
    '''
    # TODO: check whether the file is a valid image type, may using imghdr pkg.
    assert os.path.exists(file_path), 'No file in this path'
    image = Image.open(file_path)
    new_name = change_ext(file_path, ".jpeg")
    print("new_name", new_name)
    image.resize((600,400)).convert("RGB").save(new_name)
    return True

if __name__ == '__main__':
    assert len(sys.argv) != 1, 'One argument with data dir path is only allowed'
    data_dir = sys.argv[1]
    assert os.path.exists(data_dir), 'Not a valid path provided as data dir'
    for file in os.listdir(data_dir):
        convert_image_to_JPEG(os.path.join(data_dir,file))
    sys.exit(0)
