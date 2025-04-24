import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def download_file(url, save_path):
    """Tải tệp từ URL và lưu vào thư mục"""
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print(f"Tệp đã được tải xuống và lưu tại {save_path}")

def find_file_for_target_time(base_url, target_datetime):
    """Truy cập vào trang web, kiểm tra 'Last modified' và tìm tệp có mốc thời gian 'Last modified' chính xác"""
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Tìm tất cả các liên kết tệp CSV
    links = soup.find_all('a', href=True)

    # Duyệt qua tất cả các liên kết tệp CSV và tìm tệp có mốc thời gian 'Last modified' chính xác
    for link in links:
        href = link['href']
        if href.endswith('.csv'):  # Chỉ lấy các tệp .csv
            file_name = href.split("/")[-1]
            print(f"Tên tệp tìm thấy: {file_name}")
            
            # Lấy mốc thời gian 'Last modified' từ phần trong HTML (dựa trên cấu trúc trang)
            last_modified_text = link.find_next('td').text.strip()  # Lấy thời gian từ cột "Last modified"
            try:
                last_modified_time = datetime.strptime(last_modified_text, "%Y-%m-%d %H:%M")
            except ValueError:
                continue  # Nếu không thể chuyển đổi thời gian, bỏ qua tệp này

            # So sánh thời gian 'Last modified' với thời gian mục tiêu
            if last_modified_time == target_datetime:
                # Trả về URL tệp nếu mốc thời gian trùng khớp
                return base_url + href

    print(f"Không tìm thấy tệp với thời gian {target_datetime}.")
    return None

def analyze_data(file_path):
    """Phân tích dữ liệu và tìm bản ghi có HourlyDryBulbTemperature cao nhất"""
    df = pd.read_csv(file_path)

    # Kiểm tra các cột có trong dữ liệu để biết cột nào chứa thông tin cần tìm
    print("Cột trong dữ liệu:", df.columns)

    # Giả sử cột "HourlyDryBulbTemperature" tồn tại trong dữ liệu
    if 'HourlyDryBulbTemperature' in df.columns:
        highest_temperature = df.loc[df['HourlyDryBulbTemperature'].idxmax()]
        print("Bản ghi với HourlyDryBulbTemperature cao nhất:")
        print(highest_temperature)
    else:
        print("Cột 'HourlyDryBulbTemperature' không có trong dữ liệu.")

def main():
    # URL cơ sở của trang web chứa các tệp
    base_url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
    
    # Thời gian mục tiêu cần tìm
    target_datetime = datetime.strptime("2024-01-19 10:27", "%Y-%m-%d %H:%M")

    # Tìm tệp CSV với thời gian sửa đổi chính xác
    file_url = find_file_for_target_time(base_url, target_datetime)

    if file_url:
        file_name = file_url.split("/")[-1]
        download_path = os.path.join(os.getcwd(), file_name)

        # Tải tệp xuống
        download_file(file_url, download_path)

        # Phân tích dữ liệu
        analyze_data(download_path)

if __name__ == "__main__":
    main()
