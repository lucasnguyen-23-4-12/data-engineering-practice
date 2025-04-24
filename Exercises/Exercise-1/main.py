import os
import requests
import zipfile
import shutil

# Danh sách các URL cần tải xuống
download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
]

def download_zip(url, folder):
    """Tải tệp ZIP xuống thư mục"""
    filename = url.split("/")[-1]
    file_path = os.path.join(folder, filename)
    
    # Tải tệp zip
    response = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print(f"{filename} đã được tải xuống.")
    
    return file_path

def extract_zip(file_path, folder):
    """Giải nén tệp ZIP"""
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(folder)
            print(f"{file_path} đã được giải nén.")
            
            # Xử lý tệp CSV sau khi giải nén
            extracted_files = zip_ref.namelist()
            for extracted_file in extracted_files:
                if extracted_file.endswith('.csv'):
                    csv_file_path = os.path.join(folder, extracted_file)
                    print(f"File CSV được giải nén: {csv_file_path}")
                    return csv_file_path
    except zipfile.BadZipFile:
        print(f"Lỗi: {file_path} không phải là tệp zip hợp lệ.")
    
    return None

def delete_zip(file_path):
    """Xóa tệp ZIP sau khi giải nén"""
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Đã xóa tệp zip: {file_path}")

def delete_macosx(folder):
    """Xóa thư mục _MACOSX nếu có"""
    macosx_folder = os.path.join(folder, '__MACOSX')
    if os.path.exists(macosx_folder):
        print(f"Đang xóa thư mục __MACOSX...")
        shutil.rmtree(macosx_folder)

def process_zip(url, folder):
    """Tải về, giải nén và xóa tệp ZIP"""
    file_path = download_zip(url, folder)
    extract_zip(file_path, folder)
    delete_zip(file_path)

def main():
    # Tạo thư mục 'downloads' nếu chưa có
    download_folder = "downloads"
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
        print(f"Thư mục '{download_folder}' đã được tạo.")
    
    # Tải và giải nén các file từ danh sách download_uris
    for uri in download_uris:
        process_zip(uri, download_folder)

    # Sau khi tất cả tệp đã được xử lý, xóa thư mục _MACOSX (nếu có)
    delete_macosx(download_folder)

if __name__ == "__main__":
    main()
