import sys
import skimage
from pathlib import Path
import numpy as np

def process_image_file(in_path, out_path):
    """ Adds some random noise to an image to augment it. """
    # read image file, 
    image = skimage.io.imread(in_path)
    # augment the image
    augmented_image = skimage.util.random_noise(image, mode='gaussian', clip=True)
    # convert pixel representation from [0..1] to [0..255]
    augmented_image = (augmented_image * 255).astype(np.uint8)
    # save image to given location
    skimage.io.imsave(out_path, augmented_image, check_contrast=False)

def process_text_file(in_path, out_path):
    """ Replaces every occurrence of a white space with double white space to augment a text. """
    # open and read a text file
    text = in_path.read_text()
    # augment the text file
    augmented_text = text.replace(" ", "  ")
    # save text as file to given location
    out_path.write_text(augmented_text)

if __name__ == '__main__':
    # check if an input and an output file path was given
    assert len(sys.argv) == 3 

    # get the given input and output file paths and save them in a variable
    input_filepath = Path(sys.argv[1])
    output_filepath = Path(sys.argv[2])

    # check if the input and output filetypes match, otherwise we might need to process the data differently
    assert input_filepath.suffix == output_filepath.suffix

    # create needed directories first, if not already created
    output_filepath.parent.mkdir(parents=True, exist_ok=True)

    # Process files accordingly to suffix
    if input_filepath.suffix in ('.txt'):
        process_text_file(input_filepath, output_filepath)
    elif input_filepath.suffix in ('.png', '.jpg'):
        process_image_file(input_filepath, output_filepath)
    