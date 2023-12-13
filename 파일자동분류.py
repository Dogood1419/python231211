import os
import shutil
from pathlib import Path

def classify_downloads_folder(download_path):
    # 분류할 파일 유형과 해당 폴더
    file_types = {
        "images": [".jpg", ".jpeg", ".png", ".gif"],
        "pdfs": [".pdf"],
        "data": [".csv", ".xlsx"]
    }

    # 경로 확인 및 폴더 생성
    download_path = Path(download_path)
    images_folder = download_path / "images"
    pdfs_folder = download_path / "pdfs"
    data_folder = download_path / "data"

    for folder in [images_folder, pdfs_folder, data_folder]:
        folder.mkdir(exist_ok=True)

    # 다운로드 폴더 내의 파일을 분류
    for file_name in os.listdir(download_path):
        file_path = download_path / file_name

        # 파일 형식에 따라 분류
        for folder_name, extensions in file_types.items():
            if file_path.suffix.lower() in extensions:
                destination_folder = download_path / folder_name
                shutil.move(str(file_path), str(destination_folder / file_name))
                print(f"Moved {file_name} to {destination_folder}")

if __name__ == "__main__":
    # 다운로드 폴더 경로
    downloads_path = r'C:\Users\david1.choi\Downloads'
    classify_downloads_folder(downloads_path)
