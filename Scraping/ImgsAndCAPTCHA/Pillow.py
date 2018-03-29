
from PIL import Image, ImageFilter


image_sample = Image.open("test.jpg")
blurryImage = image_sample.filter(ImageFilter.GaussianBlur)
blurryImage.save("test_blurred.jpg")
blurryImage.show()
