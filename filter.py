# filter.py
import pygame


class Filter:
    def load_image(self, image_path):
        # Implement image loading logic
        img = pygame.image.load(image_path).convert_alpha()
        self.arr = pygame.surfarray.array3d(img)

    def save_image(self, output_path):
        # Implement image saving logic
        surface = pygame.surfarray.make_surface(self.arr)  # convert array back to pygame surface
        pygame.image.save(surface, output_path)  # save the surface as png
# filter.py


class MyFilter(Filter):
    def transform(self):
        for i in range(0, 1020):  # column number from 0 to 15
            for j in range(0, 574):  # row number from 0 to 15
                r, g, b = self.arr[i][j]  # get rgb values for the pixel
                self.arr[i][j] = [g, b, r]  # swap r, g, and b values

        print(self.arr)

class GrayScaleFilter(Filter):
    def transform(self):
        for i in range(0, 1020):
            for j in range(0, 574):
                # Get RGB values for the pixel
                r, g, b = self.arr[i][j]

                # Transform RGB to grayscale
                grayscale_value = r // 3 + g // 3 + b // 3

                # Update the pixel in self.arr with the grayscale value
                self.arr[i][j] = (grayscale_value, grayscale_value, grayscale_value)

        print(self.arr)