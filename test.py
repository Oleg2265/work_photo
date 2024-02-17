from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


im2 = Image.open("img_2.png")
# Save the edited image
#img2.save("kak2.png")

filter_image3 = im2.filter(Image.EMBOSS)




# Open an Image
img = Image.open('img_2.png')

# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)

# Custom font style and font size
myFont = ImageFont.truetype('FreeMonospacedBold.otf', 65)

# Add Text to an image
I1.text((10, 10), "Nice Car", font=myFont, fill=(255, 0, 0))

# Display edited image
img.show()

# Save the edited image
img.save("kak2.png")