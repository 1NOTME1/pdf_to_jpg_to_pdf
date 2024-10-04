from PIL import Image
from pdf2image import convert_from_path
import os

def convert_pdf_to_jpg(pdf_path, output_folder, dpi=300, quality=100):
    
    images = convert_from_path(pdf_path, dpi=dpi, poppler_path=r'C:\poppler\Library\bin')
    image_paths = []

    for i, image in enumerate(images):
        temp_img_path = os.path.join(output_folder, f"image_{i}.jpg")
        image.save(temp_img_path, 'JPEG', quality=quality)
        image_paths.append(temp_img_path)

    return image_paths

def convert_jpgs_to_pdf(jpg_paths, output_pdf_path):
    images = [Image.open(jpg_path).convert('RGB') for jpg_path in jpg_paths]
    images[0].save(output_pdf_path, save_all=True, append_images=images[1:])

def main(txt_file_path, output_folder, dpi=300, quality=100):
    with open(txt_file_path, "r") as file:
        pdf_paths = file.readlines()

    for pdf_path in pdf_paths:
        pdf_path = pdf_path.strip()
        jpg_paths = convert_pdf_to_jpg(pdf_path, output_folder, dpi, quality)
        output_pdf_path = os.path.join(output_folder, os.path.basename(pdf_path))
        convert_jpgs_to_pdf(jpg_paths, output_pdf_path)

        for jpg_path in jpg_paths:
            os.remove(jpg_path)


main("txt.txt", r"C:\Users\Desktop\", 300, 100)
