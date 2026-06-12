import os
import shutil

folder_path = input("Enter folder path: ")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "PDFs": [".pdf"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Documents": [".docx", ".txt"]
}

for filename in os.listdir(folder_path):

    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):

        extension = os.path.splitext(filename)[1].lower()

        for folder, extensions in file_types.items():

            if extension in extensions:

                target_folder = os.path.join(folder_path, folder)

                os.makedirs(target_folder, exist_ok=True)

                shutil.move(
                    file_path,
                    os.path.join(target_folder, filename)
                )

                print(f"Moved: {filename} → {folder}")
                break

print("\nFiles Organized Successfully! 🎉")