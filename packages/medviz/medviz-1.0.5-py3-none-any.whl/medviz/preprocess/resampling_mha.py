import SimpleITK as sitk
import numpy as np
from ..utils import path_in, save_path_file

def resample_mha(input_path, output_path, new_voxel_size, method="trilinear"):
    input_path = path_in(input_path)

    # Load the input image using SimpleITK
    img = sitk.ReadImage(input_path)
    data = sitk.GetArrayFromImage(img)
    spacing = img.GetSpacing()

    print("Current voxel size", spacing)
    current_voxel_size = np.array(spacing)

    scaling_factors = current_voxel_size / new_voxel_size
    print("Scaling factors", scaling_factors)

    # Compute the new shape after resampling
    print("Input shape", data.shape)
    new_shape = np.ceil(data.shape * scaling_factors).astype(int)
    print("Output shape", new_shape)

    # Use Trilinear interpolation to resample the data
    resampled_data = sitk.Resample(img, new_shape.tolist(), sitk.Transform(), sitk.sitkLinear)

    # Create a new SimpleITK image with resampled data and updated spacing
    resampled_img = sitk.GetArrayFromImage(resampled_data)
    resampled_spacing = new_voxel_size
    resampled_img = sitk.GetImageFromArray(resampled_img)
    resampled_img.SetSpacing(resampled_spacing)

    # Save the resampled image to the output path
    save_path = save_path_file(output_path, suffix=".mha")

    sitk.WriteImage(resampled_img, save_path)
