
import subprocess
import os
try:
    import fitz
except:
    subprocess.check_call['pip','install','fitz']
    import fitz


def create_dir(directory):
    """
    Function to create directory if it doesn't exist
    """
    if not os.path.exists(directory):
        os.makedirs(directory)


def extract_images_from_pdf(pdf_path, output_dir):
    """
    Function: To loop through a document and find each image, appending each image to a output folder
    """
    create_dir(output_dir)
    doc = fitz.open(pdf_path)
    image_count = 0

    for i in range(len(doc)):
        page = doc.load_page(i)
        images = page.get_images(full=True)
        
        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_count += 1
            
            image_path = os.path.join(output_dir, f"image_{image_count}.{image_ext}")
            with open(image_path, "wb") as image_file:
                image_file.write(image_bytes)
    
    print(f"Total {image_count} images extracted and saved to {output_dir}")


if __name__ == "__main__":
    pdf_path = input("Full Path to PDF document that contains the images:\n>")
    output_dir = input("Full Path to Directory (Folder) to save images to:\n>")
    extract_images_from_pdf(pdf_path, output_dir)
    