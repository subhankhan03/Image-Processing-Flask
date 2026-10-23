from PIL import Image

def convert_to_grayscale(input_path, output_path):
    image = Image.open(input_path)
    grayscale_image = image.convert("L")
    grayscale_image.save(output_path)

from PIL import Image, ImageEnhance

def adjust_brightness(input_path, output_path, factor):
    image = Image.open(input_path)

    enhancer = ImageEnhance.Brightness(image)
    enhanced_image = enhancer.enhance(factor)

    enhanced_image.save(output_path)