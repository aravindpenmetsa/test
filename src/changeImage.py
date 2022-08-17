#!/usr/bin/env python3

from PIL import Image

# Python program to multiply two numbers
def change_ext(file_path, new_ext):
    if type(file_path) != str or type(new_ext) != str:
        return TypeError
    path_and_filename, _ = os.path.splitext(os.path.basename(file_path))[0]
    return path_and_filename.join(new_ext)

def convert_image_to_JPEG(file_path):
    ''' Converts the provided image to JPEG format 600 X 400.
        Works only on absolute path.
    '''
    # TODO: check whether the file is a valid image type, may using imghdr pkg.
    assert os.path.exists(file_path), 'No file in this path'
    image = Image.open(file_path)
    image.resize((600,400)).convert("RGB").save(change_ext(file_path, ".JPEG"))

if __init__ == '__main__':
    assert len(os.argv) != 1, 'One argument with data dir path is only allowed'
    data_dir = os.argv[1]
    assert os.path.exists(data_dir), 'Not a valid path provided as data dir'
    for file in os.listdir(data_dir):
        convert_image_to_JPEG(os.path.join(data_dir,file))
    sys.exit(0)
