print("Hello, Harbour.Space")

from filter import Filter, GrayScaleFilter, MyFilter
import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 400))

image_path = "test3.png"  # Update the path to your image
output_path_gray = "output_gray.jpg"
output_path_my = "output_my.jpg"

# Example usage
print("Applying Grayscale Filter...")
grayscale_filter = GrayScaleFilter()

grayscale_filter.load_image(image_path)
grayscale_filter.transform()
grayscale_filter.save_image(output_path_gray)

print("Applying My Filter...")
my_filter = MyFilter()

my_filter.load_image(image_path)
my_filter.transform()
my_filter.save_image(output_path_my)



