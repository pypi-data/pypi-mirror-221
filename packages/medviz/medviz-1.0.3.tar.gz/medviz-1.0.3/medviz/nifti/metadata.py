import nibabel as nib
import numpy as np
import nibabel as nib

def metadata(image_path: str):
    """
    Get metadata of a NIfTI image
    :param image_path: path to NIfTI image
    :return: metadata
    """
    image_info = {}

    # Load the NIfTI file and extract necessary information
    image = nib.load(image_path)
    image_data = image.get_fdata()
    image_header = image.header
    affine = image.affine

    slope_obj = image.dataobj.slope
    intercept_obj = image.dataobj.inter

    print("slope_obj", slope_obj)
    print("intercept_obj", intercept_obj)
    

    # Get image dimensions and voxel size
    dimensions = image_data.shape
    voxel_size = image_header.get_zooms()[:3]

    # Get spatial and temporal units
    spatial_units, temporal_units = image_header.get_xyzt_units()

    # Get slope and intercept for Hounsfield Unit (HU) conversion
    slope, intercept = image_header.get_slope_inter()[:2]

    # Determine if the image is in HU format
    is_hu_format = slope == 1 and intercept <= 0

    # Check if the image is isotropic
    is_isotropic = all(size == voxel_size[0] for size in voxel_size)

    # Store the information in the dictionary
    image_info["dimensions"] = dimensions
    image_info["voxel_size"] = voxel_size
    image_info["spatial_units"] = spatial_units
    image_info["temporal_units"] = temporal_units
    image_info["slope"] = slope
    image_info["intercept"] = intercept
    image_info["is_hu"] = is_hu_format
    image_info["is_isotropic"] = is_isotropic

    return image_info


# if __name__ == "__main__":
#     image_path = "data/CT.nii.gz"
#     ct_meta = metadata(image_path)
#     print(ct_meta)