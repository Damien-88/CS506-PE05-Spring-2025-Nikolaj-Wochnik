from PIL import Image, ImageOps, ImageFilter, ImageEnhance
import matplotlib.pyplot as plt
import numpy as np

# Open image, assign to variable
img = Image.open("PE05-input.jpg")

# Use numpy to create exposure adjustment
np_img = np.array(img).astype(np.float32) # Convert for np adjustment
np_img = np.clip(np_img * 0.65, 0, 255) # Decrease light exposure
img = Image.fromarray(np_img.astype(np.uint8)) # Convert back for pillow adjustment

img = ImageOps.equalize(img) # Histogram Equalization
img = ImageOps.grayscale(img) # Histogram Equalization
img = ImageOps.autocontrast(img) # Histogram Equalization
img = img.filter(ImageFilter.GaussianBlur(0.85))
img = ImageEnhance.Brightness(img).enhance(0.8) # Decrease brightness
img = ImageEnhance.Sharpness(img).enhance(5) # Slightly increase sharpness

img.save("PE05-output.png", format = "PNG") # Save new image

plt.axis("off")
plt.imshow(img, cmap = "gray")
plt.show()

"""
1. How many people do you see in the output image?
    
    4: 2 Obvious, 2 Probable
    There are 2 people in the foreground. 
    There also appears to be 2 people in the distance standing on opposite sides of the street from eachother.

2. How many trees can you identify?
    
    There appears to be just two trees on the left side of the foreground.

3. How many windows can you identify on the 2nd floor of the first building (labelled as “1”) on the
right-hand side of the road?

    There appears to be 3 windows on the second floor. Two in the front and one on the side.

4. How many windows can you identify in the second building (labeled as “2”) on the right-hand
side of the road facing you?

    My observation is 6 windows.
    It looks to be 4 windows on the side and 2 on the second floor on the front. 
    
"""