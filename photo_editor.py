from PIL import Image, ImageEnhance, ImageFilter
import os

output_folder = "enhanced_images"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
for file in os.listdir():
    if file.lower().endswith(('jpg', 'jpeg', 'png')):
        print("Editing image...✨")

        img = Image.open(file)

        img = img.filter(ImageFilter.SMOOTH_MORE)  # smoothening the harsh edges.

        color_enhance = ImageEnhance.Color(img)
        img = color_enhance.enhance(1.4)  # enhancing vibrancy. Pop effect.

        brightness_enhance = ImageEnhance.Brightness(img)
        img = brightness_enhance.enhance(1.1)

        contrast_enhance = ImageEnhance.Contrast(img)
        img = contrast_enhance.enhance(1.2)

        sharpness_enhance = ImageEnhance.Sharpness(img)
        img = sharpness_enhance.enhance(1.25)

        save_path = os.path.join(output_folder, f"enhanced_{file}")
        img.save(save_path) 
        print(f"Edited image {save_path} saved successfully!✅")   

print("All photos edited successfully!🥳 Check the enhaced_images folder.")

# to run--> create a folder, add images u want to edit into that folder, download this file and move it to that folder.



