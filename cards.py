import pygame

def load_image(file_name):
    """Loads an image from the given file and returns a scaled version.

    Args:
        file_name (str): The file name of the image to load.

    Returns:
        A scaled version of the image.
    """
    # Load the image and get its size
    image = pygame.image.load(file_name)
    width, height = image.get_size()

    # Calculate the scale factor
    scale_factor = 0.5

    # Scale the image
    image = pygame.transform.scale(image, (int(width * scale_factor), int(height * scale_factor)))

    return image
