from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

# open an image file
img = Image.open('PIL\image.jpg')

# display image dimensions and format
print('Image format:', img.format)
print('Image size:', img.size)

# crop image
crop_box = (100, 100, 300, 300)
cropped_img = img.crop(crop_box)
cropped_img.save('PIL\cropped_image.jpg')

# resize image
resize_img = img.resize((400, 400))
resize_img.save('PIL\\resized_image.jpg')

# rotate image
rotated_img = img.rotate(45)
rotated_img.save('PIL\\rotated_image.jpg')

# convert image to grayscale
gray_img = img.convert('L')
gray_img.save('PIL\gray_image.jpg')

# apply filter to image
filtered_img = img.filter(ImageFilter.GaussianBlur(radius=10))
filtered_img.save('PIL\\filtered_image.jpg')

# flip image
flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
flipped_img.save('PIL\\flipped_image.jpg')

# create new image
new_img = Image.new('RGB', (400, 400), color=(255, 255, 255))

# draw on image
draw = ImageDraw.Draw(new_img)
draw.text((100, 100), 'Hello, World!', fill=(0, 0, 0))
draw.line([(0, 0), (400, 400)], fill=(255, 0, 0), width=5)
draw.rectangle([(50, 50), (350, 350)], outline=(0, 255, 0), width=2)

# add border to image
bordered_img = ImageOps.expand(new_img, border=10, fill=(255, 0, 0))
bordered_img.save('PIL\\bordered_image.jpg')
