"""

"""


# Built-in

# Libs
import numpy as np
import skimage.transform

# Own modules
import toolman as tm


def upsample(file_name, size):
    img = tm.misc_utils.load_file(file_name)
    img = skimage.transform.resize(img, size, preserve_range=True).astype(np.uint8)

    # tm.vis_utils.compare_figures([img], (1, 1))
    tm.misc_utils.save_file(file_name, img)


if __name__ == '__main__':
    img_names = tm.misc_utils.get_files(r'../assets/general/dirtmap', '*.jpg')
    for img_name in img_names:
        upsample(
            file_name=img_name,
            size=(2048, 2048),
        )
