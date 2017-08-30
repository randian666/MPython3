#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont, ImageFilter

#创建缩略图
im=Image.open("e:/Chrysanthemum.jpg")
w, h = im.size
im.thumbnail((w//2, h//2))
im.save('thumbnail.jpg', 'jpeg')

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('thumbnail.jpg')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')

# PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片
import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(0, 177), random.randint(32, 177), random.randint(32, 177))

width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('1/OfficinaSansStd-Bold.otf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR) #模糊
image.save('code.jpg', 'jpeg')