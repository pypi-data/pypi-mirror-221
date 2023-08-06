import SimpleITK as sitk

import matplotlib.pyplot as plt

def read_mha_image(file_path):
    image = sitk.ReadImage(file_path)
    return image

def get_image_properties(image):
    size = image.GetSize()
    origin = image.GetOrigin()
    spacing = image.GetSpacing()
    pixel_data = sitk.GetArrayFromImage(image)
    return size, origin, spacing, pixel_data

if __name__ == "__main__":
    # mha_file_path = "/storage/sync/git/mohsen/medviz/dataset/PROV_RectalCA_001_pre_ax_T2_raw.mha"
    # mha_file_path  = "/home/fes/dataset/test_nii/2.mha"
    mha_file_path = "/storage/sync/git/mohsen/medviz/dataset/3raw_resampled.mha"
        # mha_file_path ="/storage/sync/git/mohsen/medviz/dataset/PROV_RectalCA_001_pre_ax_T2_raw_resampled.mha"
    image = read_mha_image(mha_file_path)
    size, origin, spacing, pixel_data = get_image_properties(image)

    print("shape of pixel_data:", pixel_data.shape)
    plt.imshow(pixel_data[10,:,:], cmap='gray')
    plt.show()


    print("Image size:", size)
    print("Image origin:", origin)
    print("Image spacing:", spacing)
    print("Image pixel data shape:", pixel_data.shape)
