"""basic pillow import"""

from PIL import Image

def load_image(file:str, img_folder='photos/'):
    """Takes a filename (with extension) and returns the image data

    Args:
        filename (str): Filename including relative path
        img_folder (str, optional): _description_. Defaults to 'photos'.

    Returns:
        imagedata
    """
    if file.startswith(img_folder):
        im = Image.open(file)
    else:
        im = Image.open(img_folder + file)
    return im
