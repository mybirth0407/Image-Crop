#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Yedarm Seong
Python Version: 3.5.2
"""

# python3 -m pip install pillow

from PIL import Image

def image_crop(left, top, width, height, open_file, save_file):
  img = Image.open(open_file)
  img2 = img.crop((left, top, width, height))
  # img2.show() # Cropped image show
  img2.save(save_file)

image_crop(0, 0, 300, 300, "image.jpg", "image2.jpg")
