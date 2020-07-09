"""

"""


# Built-in
import os
from glob import glob

# Libs
import numpy as np
from skimage import color
from natsort import natsorted

# Own modules
import toolman as tm


def get_images(img_dir):
    return [a for a in natsorted(glob(os.path.join(img_dir, '*.jpg'))) if 'cust' not in a]


def main():
    data_dir = r'C:\Users\Bohao\Documents\CityEngine\Syn-v102\ESRI.lib\assets\Roofs'
    texture_folds = ['Flat', 'Sloped']
    for tex_name in texture_folds:
        img_files = get_images(os.path.join(data_dir, tex_name))
        save_dir = os.path.join(data_dir, tex_name+'_grey')
        tm.misc_utils.make_dir_if_not_exist(save_dir)

        for img_file in img_files:
            img = tm.misc_utils.load_file(img_file)
            img = (color.rgb2gray(img) * 255).astype(np.uint8)

            '''print(img.shape)
            import matplotlib.pyplot as plt
            plt.imshow(img)
            plt.show()'''

            tm.misc_utils.save_file(os.path.join(save_dir, os.path.basename(img_file)), img)


if __name__ == '__main__':
    main()
