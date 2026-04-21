import os
from PIL import Image

# 👉 CHANGE THIS to your actual folder path
input_root = r"C:\Users\YourName\Desktop\images"   # or "./images"
output_root = r"C:\Users\YourName\Desktop\webp_output"

supported_formats = (".jpg", ".jpeg", ".png")

# Check if input folder exists
if not os.path.exists(input_root):
    print("❌ Input folder not found!")
    exit()

converted_count = 0

for root, dirs, files in os.walk(input_root):
    print(f"\n📂 Checking folder: {root}")

    for file in files:
        print(f"   🔍 Found file: {file}")

        if file.lower().endswith(supported_formats):
            input_path = os.path.join(root, file)

            # Preserve folder structure
            relative_path = os.path.relpath(root, input_root)
            output_dir = os.path.join(output_root, relative_path)
            os.makedirs(output_dir, exist_ok=True)

            output_filename = os.path.splitext(file)[0] + ".webp"
            output_path = os.path.join(output_dir, output_filename)

            try:
                img = Image.open(input_path)

                # Fix for PNG transparency
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")

                img.save(output_path, "WEBP", quality=85)
                print(f"   ✅ Converted → {output_path}")
                converted_count += 1

            except Exception as e:
                print(f"   ❌ Error: {e}")

print(f"\n🎉 Total converted: {converted_count}")