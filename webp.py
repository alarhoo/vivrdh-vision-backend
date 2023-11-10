import os
from PIL import Image

def convert_images_to_webp(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', 'webp')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.webp')

            # Open the image and save it as WebP
            image = Image.open(input_path)
            image.save(output_path, 'webp', quality=25)  # Adjust quality as needed

            print(f"Converted {filename} to WebP")

if __name__ == "__main__":
    input_folder = input("Enter the input folder path: ")
    output_folder = input_folder+"\webp"  # Output folder name

    convert_images_to_webp(input_folder, output_folder)
