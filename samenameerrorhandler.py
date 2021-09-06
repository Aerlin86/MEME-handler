import os
import shutil
import datetime
import re
from imagesize import get_image_size
from pathlib import Path


def same_name(file):
    new_image = ("D:\\Meme\\" + file)
    new_image_path = Path(new_image)
    new_dimensions = get_image_size(new_image_path)

    old_image = ("D:\\Meme\\GIF\\" + file)
    old_image_path = Path(old_image)
    old_dimensions = get_image_size(old_image_path)

    width = (new_dimensions[0] - old_dimensions[0])
    height = (new_dimensions[1] - old_dimensions[1])

    if width == 0 and height == 0:
        check_path = "D:\\Meme\\GIF\\Check"
        if not os.path.exists(check_path):
            os.mkdir(check_path)

        add = '(spr)'
        old_file_name = file
        path = str("D:\\Meme\\")
        p = '.gif'
        nf = re.search("(.*)(\.gif)", old_file_name)
        new_file = nf.group(1)
        new_file_name = new_file + add + p
        os.rename(os.path.join(path, old_file_name), os.path.join(path, new_file_name))
        shutil.move("D:\\Meme\\" + new_file_name, "D:\\Meme\\GIF\\Check")
        shutil.move("D:\\Meme\\GIF\\" + old_file_name, "D:\\Meme\\GIF\\Check")

    else:
        Current_Date = datetime.datetime.today().strftime('%d')
        old_file_name = file
        path = str("D:\\Meme\\")
        p = '.gif'
        nf = re.search("(.*)(\.gif)", old_file_name)
        new_file = nf.group(1)
        new_file_name = new_file + Current_Date + p
        os.rename(os.path.join(path, old_file_name), os.path.join(path, new_file_name))
        shutil.move("D:\\Meme\\" + new_file_name, "D:\\Meme\\GIF")
