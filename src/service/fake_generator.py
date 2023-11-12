import skimage
import os
import random

from model.generator import Generator


class FakeGenerator(Generator):
    dir_path = "../../example/ai_gen_images/"
    images = []

    def generate(self, output_file_path):
        """
           Method that takes one random image of the ai_gen_image directory and puts it in another directory.
        """
        self.list_images()
        random_image_index = random.randint(0, len(self.images) - 1)
        random_image_path = self.images[random_image_index]
        random_image_name = random_image_path.split("/")[-1]
        random_image = skimage.io.imread(random_image_path)
        os.mkdir(output_file_path)
        skimage.io.imsave(output_file_path+random_image_name, random_image, check_contrast=False)

    def list_images(self):
        """
            Helper method, that lists all images that are in the ai_gen_image directory.
        """
        for image in os.listdir(self.dir_path):
            if os.path.isfile(os.path.join(self.dir_path, image)):
                self.images.append(self.dir_path + image)


# following is to test, TODO: can be deleted
fakeGenerator = FakeGenerator()
fakeGenerator.generate("../../fake_generator_images/")
