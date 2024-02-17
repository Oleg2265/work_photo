from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw
from PIL import ImageFont



im2 = Image.open("img_2.png")
im = Image.open("img.png")
im1 = im.transpose(Image.ROTATE_90)



print(im.format, im.size, im.mode)




#im.show()
im1.save("roted_photo.png")


img2 = Image.open('img_2.png')


filter_image = im.filter(ImageFilter.BoxBlur(4))
filter_image3 = im2.filter(ImageFilter.EMBOSS)
filter_image1 = im.filter(ImageFilter.EMBOSS)

I1 = ImageDraw.Draw(im2)





I1 = ImageDraw.Draw(img2)
myFont = ImageFont.truetype('FreeMonospacedBold.otf', 65)
I1.text((0, 0), "jkguiho:", font=myFont, fill =(255, 0, 0))

im2.show()





















