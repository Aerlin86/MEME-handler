import os
import shutil
from samenameerrorhandler import same_name

files = os.listdir("D:\\Meme")

for file in files:
    if file.endswith(".gif"):
        try:
            shutil.move("D:\\Meme\\" + file, "D:\\Meme\\GIF")

        except:
            same_name(file)
