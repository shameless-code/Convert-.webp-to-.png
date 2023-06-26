#!/usr/bin/env python

from PIL import Image
import os


def main():
    """Convert all WebP images in chosen directory into PNG
    and saves them to specially created directory 'png images'."""
    # Get from user location with WebP images
    webp_dir = input('Insert path for targeted directory:\n')

    # Create a directory for converted images
    png_dir = os.path.join(webp_dir, "png images")
    if not os.path.exists(png_dir):
        os.makedirs(png_dir)

    # Convert WebP images to PNG and save to "png_dir"
    for target_folder, sub_folders, target_folder_files in os.walk(webp_dir):
        for single_file in target_folder_files:
            if single_file.endswith('.webp'):
                print(f'Converting:\n {single_file}')
                new_name = single_file[:-5] + str('.png')
                new_directory = os.path.join(png_dir, new_name)

                file_path = os.path.join(target_folder, single_file)
                img_WEBP = Image.open(file_path)
                img_WEBP.save(new_directory, format="png", lossless = True)


if __name__ == "__main__":
    main()
