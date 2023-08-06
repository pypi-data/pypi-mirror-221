from ..utils import path_in, save_path_file

import torchio as tio


def resample_mha(input_path, output_path):
    input_path = path_in(input_path)

    image = tio.ScalarImage(input_path)
    resample = tio.Resample()  # default is 1 mm isotropic

    resampled = resample(image)

    save_path = save_path_file(output_path, suffix=".mha")

    resampled.save(save_path)

    print("Resampled image saved to", save_path)
