# -*- coding: utf-8 -*-

# @Author  : Skye
# @Time    : 2018/1/9 00:40
# @desc    : adb 获取截屏，截取图片


from PIL import Image
import os
import matplotlib.pyplot as plt

def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/screenshot.png')
    os.system('adb pull /sdcard/screenshot.png .')

#pull_screenshot()
img = Image.open("./screenshot.png")

# 用 matplot 查看测试分辨率，切割问题和选项区域
#region = img.crop((75, 315, 1167, 789)) # iPhone 7P
question_im  = img.crop((75, 560, 990, 1200)) # Z11 miniS xigua
choices_im = img.crop((75, 560, 990, 1200))
#question_im  = img.crop((50, 580, 1000, 840)) # Z11 wangzhe
#choices_im = img.crop((192, 887, 890, 1730))

plt.subplot(221)
im = plt.imshow(img, animated=True)
plt.subplot(222)
im2 = plt.imshow(question_im, animated=True)
plt.subplot(212)
im3 = plt.imshow(choices_im, animated=True)
plt.show()