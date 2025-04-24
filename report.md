#                    BÁO CÁO THỰC HÀNH LAB 09



------

##          

##                    Exercise #1 - Downloading Files with Python.



**YÊU CẦU:**

- **Tạo thư mục** **downloads/** nếu nó chưa tồn tại bằng Python.

- **Tải về 10 file ZIP** từ các  URL được cung cấp trong main.py bằng thư viện requests.     

- **Trích xuất tên file** từ URL để lưu file đúng tên gốc.    

- **Giải nén mỗi file ZIP** để lấy ra file .csv.

- **Xoá file ZIP** sau khi giải nén

  

### CÁC CHỈNH SỬA ĐÃ THỰC HIỆN Ở EXERCISE 1:

+ ***file requirements.txt***

#### ***Trước:***

````
requests==2.27.1
````

***Sau:***

```
requests==2.27.1
pandas
```



+ **file Main.py**

**Trước:**

```
import requests
download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

def main():
    # your code here
    pass

if __name__ == "__main__":
    main()
```



***Sau:***

```
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
```



***TÁC DỤNG***

Tạo thư mục downloads tự động nếu chưa tồn tại để lưu dữ liệu tải về.

Tải từng file ZIP từ URL, sử dụng thư viện `requests`, đồng thời trích xuất tên file từ đường dẫn để lưu đúng tên gốc.

Giải nén file ZIP bằng zipfile, và tìm ra file .csv bên trong. Nếu file ZIP không hợp lệ, chương trình sẽ không bị dừng mà sẽ hiển thị lỗi thông báo.

Xoá file ZIP sau khi giải nén thành công, giúp tiết kiệm dung lượng lưu trữ.

Xoá thư mục rác `__MACOSX` nếu có (trường hợp một số file ZIP được tạo từ hệ điều hành macOS).

Tổ chức mã nguồn rõ ràng, mỗi bước được đóng gói thành hàm riêng `(download_zip, extract_zip, delete_zip, process_zip, ...)`, giúp dễ bảo trì và mở rộng sau này.



### CÁC BƯỚC KHỞI TẠO VÀ ẢNH KẾT QUẢ CỦA EXERCISE 1

**bước 1: chạy docker **

```
build –tag=exercise-1
```

[KẾT QUẢ BƯỚC 1](https://drive.google.com/file/d/15aXTVmJfBAarnGEOPcCaPfXTP2xNkx8W/view?usp=drive_link)

**bước 2:** **chạy** 

```
docker-compose up run
```

[KẾT QUẢ BƯỚC 2](https://drive.google.com/file/d/1AmXvfOrcy4RWmAGr3oiiR6K4AeKKwQNb/view?usp=drive_link)

[KẾT QUẢ BƯỚC 2.1](https://drive.google.com/file/d/1ERt2WIuB7q4o4BMTlDFi3VhrTNX_YKBm/view?usp=drive_link)



**kiểm tra các file csv đã được tạo**

[KẾT QUẢ BƯỚC KIỂM TRA FILE CSV](https://drive.google.com/file/d/1d2quYOVIK7YEZjefX7tbSvLux3MuyEeR/view?usp=drive_link)







##         Exercise #2 - WebScraping and File Downloading with Python.



**YÊU CẦU**:

**Web Scraping từ trang HTML**

 Truy cập trang web:

​     https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/

1. Đây là một trang chứa danh sách các file dữ liệu khí tượng. Nhiệm vụ là dùng Python để **quét nội dung HTML của trang này** và tìm ra **file có thời gian sửa đổi (Last Modified) là** **2024-01-19 10:27**.
    Lưu ý: Không được tra thủ công hay "đoán" tên file – bắt buộc phải phân tích HTML để lấy đúng thông tin.

2. **Tạo URL đầy đủ để tải file**     Sau khi có được tên file từ bước trên, tôi cần ghép nó với URL gốc để tạo     ra liên kết đầy đủ và hợp lệ, ví dụ:

     https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/<ten_file.csv>

3. **Tải file về máy** Sử dụng thư viện requests để tải file .csv về, lưu vào thư mục cục bộ (có thể là downloads/ giống như bài trước).

4. **Phân tích dữ liệu bằng Pandas** Dùng thư viện pandas để đọc file CSV vừa tải về. Sau đó:

   +  Tìm dòng (hoặc các dòng) có nhiệt độ cao nhất tại cột `HourlyDryBulbTemperature.`

   + In các dòng dữ liệu này ra màn hình terminal bằng lệnh `print()`. 

5. **Cấu trúc thực thi** Tất cả mã Python sẽ được viết trong file main.py. Sau khi hoàn tất, tôi có thể build và chạy chương trình bằng Docker theo hướng dẫn:



### CÁC CHỈNH SỬA ĐÃ THỰC HIỆN Ở EXERCISE 2:

- ***file requirement.txt***

**trước:**

```
requests==2.27.1
pandas==2.2.3
```

**sau:** 

```
requests==2.27.1
pandas==2.2.3
beautifulsoup4
```



+ ***FILE Main.py***

**trước:** 

```
import requests
import pandas

def main():
    # your code here
    pass

if __name__ == "__main__":
    main()
```

**sau:**

```
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
```



**TÁC DỤNG CODE TRÊN:**

```
find_file_for_target_time(base_url, target_datetime):
```

+  Mục tiêu: Tìm và trả về đường dẫn của tệp .csv có thời gian `Last Modified` trùng với thời gian mục tiêu.

+ **Cách hoạt động:**

  + Dùng `requests` để tải trang web chứa danh sách các tệp.
  + Dùng `BeautifulSoup` để phân tích HTML và tìm tất cả các liên kết tệp .csv.
  + Duyệt qua các liên kết, lấy thông tin `Last Modified` từ cột bên cạnh và so sánh với thời gian mục tiêu.
  + Nếu tìm thấy tệp có thời gian trùng khớp, trả về đường dẫn tệp.

  

  ```
  download_file(url, save_path):
  ```

  Tải tệp .csv từ URL tìm được và lưu vào thư mục cụ thể trên máy tính.

  

  ```
  analyze_data(file_path):
  ```

  Phân tích dữ liệu trong tệp .csv và tìm bản ghi có giá trị `HourlyDryBulbTemperature` cao nhất.

  

### CÁC BƯỚC KHỞI TẠO VÀ ẢNH KẾT QUẢ CỦA EXERCISE 2

bước 1: **Chạy **

```
docker build --tag=exercise-2
```

[KẾT QUẢ BƯỚC 1](https://drive.google.com/file/d/1M4dg1Rm0UVP0vXJiakliMz1QknEQeFB1/view?usp=drive_link)



bước 2: **Chạy**

```
docker-compose up run
```

[KẾT QUẢ BƯỚC 2](https://drive.google.com/file/d/1A4ncTj93yJ-QML7o9P8Ervn8kg0G0qhr/view?usp=drive_link)



**check docker** 

[KẾT QUẢ CHECK DOCKER ĐÃ CHẠY THÀNH CÔNG](https://drive.google.com/file/d/1QfVgi1bFemxNOlwvQoXk6MJbUNaYuZgw/view?usp=drive_link)







#                   Exercise #3 - Boto3 AWS + s3 + Python.



**yêu cầu**

1. **Tải tệp .gz từ S3**:
   + Dùng thư viện **boto3** để tải tệp wet.paths.gz từ **S3 bucket** **commoncrawl** với `key crawl-data/CC-MAIN-2022-05/wet.paths.gz`.

2. **Giải nén và đọc tệp .gz**:

   + Giải nén tệp .gz ngay khi tải về mà không lưu tệp này vào ổ đĩa (tải trực tiếp vào bộ nhớ).
   + Đọc nội dung tệp này và lấy URI (địa chỉ tệp) trên dòng đầu tiên của tệp

3. **Tải tệp từ URI**:

   + Sử dụng **boto3** để tải tệp từ URI lấy được ở bước trước.

4. **In từng dòng của tệp tải về**:    

   +  Duyệt qua từng dòng trong tệp tải về và in từng dòng ra màn hình (stdout).

     

**CÁCH LÀM:**

 Do không dùng được **boto3** nên Nhóm chuyển sang dùng **request**



### CÁC CHỈNH SỬA ĐÃ THỰC HIỆN Ở EXERCISE 3:

+ ***Trong file requirements.txt***

**trước:**

```
boto3==1.21.2
```

**sau:** 

```
boto3==1.21.2
pandas
requests
```



+ ***file Main.py***

**trước:**

```
import boto3

def main():
    # your code here
    pass

if __name__ == "__main__":
    main()
```

**sau:** 

```
import requests
import gzip
import io

def download_from_s3(url):
    """Tải tệp từ S3 công khai và trả về nội dung dưới dạng bytes"""
    response = requests.get(url)
    return response.content

def extract_and_get_uri_from_gz(gz_file_bytes):
    """Giải nén tệp .gz trong bộ nhớ, đọc URI từ dòng đầu tiên"""
    with gzip.GzipFile(fileobj=io.BytesIO(gz_file_bytes)) as f:
        # Đọc toàn bộ nội dung và lấy URI từ dòng đầu tiên
        first_line = f.readline().decode('utf-8').strip()  # Đọc dòng đầu tiên và loại bỏ ký tự trắng
    return first_line

def download_and_print_uri_file(uri):
    """Tải tệp từ S3 theo URI, giải nén và in từng dòng"""
    # Xây dựng URL đầy đủ từ URI
    full_url = f'https://data.commoncrawl.org/{uri}'
   
    # Tải tệp từ URI
    response = requests.get(full_url, stream=True)  # Sử dụng stream để tránh tải toàn bộ tệp vào bộ nhớ
   
    # Giải nén tệp và in từng dòng
    with gzip.GzipFile(fileobj=io.BytesIO(response.content)) as f:
        for line in f:
            print(line.decode('utf-8'))

def main():
    # URL của tệp S3 công khai
    s3_url = 'https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-05/wet.paths.gz'
   
    # Tải tệp .gz từ S3
    gz_file_bytes = download_from_s3(s3_url)
   
    # Giải nén và lấy URI từ dòng đầu tiên
    uri = extract_and_get_uri_from_gz(gz_file_bytes)
    print(f"URI của tệp cần tải: {uri}")
   
    # Tải và in từng dòng của tệp URI
    download_and_print_uri_file(uri)

if __name__ == "__main__":
    main()
```



**GIẢI THÍCH TỔNG QUAN NHỮNG CHỈNH SỬA QUAN TRỌNG:**

1. ```
   download_from_s3(url)
   ```

Tải file .gz từ S3 bằng `requests`, trả về dạng `bytes`.

2. ```
   extract_and_get_uri_from_gz(gz_bytes)
   ```

Giải nén ngay trong bộ nhớ, đọc dòng đầu tiên để lấy URI.

3. ```
   download_and_print_uri_file(uri)
   ```

Tải file từ URL, dùng `stream=True` để đọc và in từng dòng mà không cần lưu toàn bộ vào bộ nhớ.

4. ```\
   main()
   ```

Gọi các hàm theo thứ tự: tải `.gz → lấy URI → tải file chính → in nội dung`



### CÁC BƯỚC KHỞI TẠO VÀ ẢNH KẾT QUẢ CỦA EXERCISE 4

**bước 1: chạy lệnh**

```
docker build --tag=exercise-3 
```

[KẾT QUẢ BƯỚC 1](https://drive.google.com/file/d/1lINvojDqyqPC6l2i-CJ37Ko12QBojXRG/view?usp=drive_link)



**bước 2: chạy lệnh**

```
docker-compose up run
```

[KẾT QUẢ BƯỚC 2](https://drive.google.com/file/d/1qY_W7XRcAQspOci6Giyrya5uajY8EcdY/view?usp=drive_link)

[KẾT QUẢ BƯỚC 2.1](https://drive.google.com/file/d/1QSwVyR2rJG0a41mV2bSsVPhqEkeCgxDn/view?usp=drive_link)



**check docker**

[KẾT QUẢ CHECK  DOCKER ĐÃ CHẠY THÀNH CÔNG](https://drive.google.com/file/d/14KiVxbPMTnny44HxW5VkiMub4sFwVb-t/view?usp=drive_link)













##                       Exercise #4 - Convert JSON to CSV + Ragged Directories.



### Yêu cầu:

+ Duyệt toàn bộ thư mục data/ và các thư mục con bên trong để tìm tất cả các tệp có định dạng .json.

+ Đọc nội dung các tệp `JSON` bằng Python.

+ Làm phẳng cấu trúc dữ liệu JSON nếu có các đối tượng lồng nhau (ví dụ: `{"coordinates": [-99.9, 16.88333]}` phải tách thành các giá trị riêng).

+ Chuyển đổi mỗi tệp `JSON` sang một tệp `CSV` tương ứng. File `CSV` được lưu cùng vị trí với file JSON gốc `(1:1 mapping)`.

  

### CÁC CHỈNH SỬA ĐÃ THỰC HIỆN Ở EXERCISE 4:

- ***Trong DockerFile:***

**Trước:** 

```
FROM python:latest
WORKDIR app
COPY . /app

RUN python3 -m pip install -r requirements.txt
```



**Sau:**

```
FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install requests beautifulsoup4 psycopg2-binary

CMD ["python", "main.py"]
```



***NHỮNG THAY ĐỔI TRONG DOCKERFILE BAO GỒM:***

+ Sử dụng phiên bản Python cụ thể và tối ưu hơn. `(slim)` giúp giảm dung lượng image, tăng tốc build.

+ Dùng: `RUN pip install requests beautifulsoup4 psycopg2-binary` để cài trục tiếp các thư viện luôn.

+ Thêm lệnh `CMD ["python", "main.py"]` để container tự chạy chương trình khi khởi động. 



- ***Trong file Main.py:***

  **Trước:**

  ```
  import boto3
  
  def main():
      # your code here
      pass
  
  if __name__ == "__main__":
      main()
  ```

  **sau:**

  ```
  import os
  import glob
  import json
  import csv
  
  def flatten_json(nested_json, parent_key='', sep='_'):
      """Flatten nested JSON (dict and list) into a single-level dictionary."""
      items = []
      for k, v in nested_json.items():
          new_key = f"{parent_key}{sep}{k}" if parent_key else k
          if isinstance(v, dict):
              items.extend(flatten_json(v, new_key, sep=sep).items())
          elif isinstance(v, list):
              for i, item in enumerate(v):
                  items.extend(flatten_json({f"{i}": item}, new_key, sep=sep).items())
          else:
              items.append((new_key, v))
      return dict(items)
  
  def json_to_csv(json_path):
      """Convert a JSON file to CSV, saving next to original file."""
      try:
          with open(json_path, 'r', encoding='utf-8') as file:
              data = json.load(file)
      except json.JSONDecodeError as e:
          print(f"[✘] Error reading JSON file {json_path}: {e}")
          return
      except FileNotFoundError:
          print(f"[✘] File not found: {json_path}")
          return
  
      # Handle both single JSON objects and lists
      if isinstance(data, list):
          flat_data = [flatten_json(item) for item in data]
      else:
          flat_data = [flatten_json(data)]
  
      if not flat_data:
          print(f"[!] No valid data to write from: {json_path}")
          return
  
      csv_path = json_path.replace('.json', '.csv')
  
      try:
          with open(csv_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
              writer = csv.DictWriter(csvfile, fieldnames=flat_data[0].keys())
              writer.writeheader()
              for row in flat_data:
                  writer.writerow(row)
          print(f"[✔] Converted: {json_path} → {csv_path}")
      except Exception as e:
          print(f"[✘] Error writing CSV file {csv_path}: {e}")
  
  def main():
      data_dir = "data"
      os.makedirs(data_dir, exist_ok=True)
      print(f"[+] Scanning directory: {data_dir}")
      json_files = glob.glob(os.path.join(data_dir, '**/*.json'), recursive=True)
      if not json_files:
          print("[!] No JSON files found.")
          return
      for path in json_files:
          json_to_csv(path)
  
  if __name__ == "__main__":
      main()
  ```



### CÁC BƯỚC KHỞI TẠO VÀ ẢNH KẾT QUẢ CỦA EXERCISE 4



**Bước 1:** **Build Docker:**

```
docker build --tag=exercise-4 .
```

[KẾT QUẢ 1](https://drive.google.com/file/d/1xZZZFZ5yBGxV32yC_bD6QISfrxrE3HGk/view?usp=drive_link)

**bước 2:** **Chạy Docker-Compose:**

```docker-compose up run
docker-compose up run
```

[KẾT QUẢ 2](https://drive.google.com/file/d/1_yv3zWlDzfwX5Ko7HyMdeIEztDmu_npM/view?usp=drive_link)



**Kiểm tra trên Docker:**

[KẾT QUẢ TRÊN DOCKER](https://drive.google.com/file/d/1-69wzLFmOGIjomJLuhdJGPKJu9mUhq6_/view?usp=drive_link)

**Kiểm tra file CSV:**

[KẾT QUẢ TRÊN FILE CSV](https://drive.google.com/file/d/18I6GNZyl4tB9k0SY4iIOjdOj6lVR9Jdx/view?usp=drive_link)

**Xem thông tin trong file CSV “**Ví dụ File-1.CSV**”**

[XEM THÔNG TIN TRONG FILE CSV](https://drive.google.com/file/d/1JpfInezZd8A-W2csW1ZNdRid6oJFFU-E/view?usp=drive_link)





##  

##                             Exercise #5 - Data Modeling for Postgres + Python.



### Mục tiêu

+ Khởi tạo hệ thống cơ sở dữ liệu PostgreSQL với Docker Compose.

+ Load dữ liệu từ các file CSV (accounts.csv, products.csv, transactions.csv) vào database thông qua script Python.

+ Xác thực dữ liệu đã được nhập thành công vào database.

  

### CÁC CHỈNH SỬA ĐÃ THỰC HIỆN Ở EXERCISE 5 VÀ KẾT QUẢ:

- ***viết lại code dockerfile***

  ```
  FROM python:latest
  
  WORKDIR /app
  COPY . /app
  COPY data /app/data
  
  RUN python3 -m pip install -r requirements.txt
  ```



**`FROM python:latest`**
 → Dùng image Python mới nhất để đảm bảo tương thích thư viện và bảo mật.

**`WORKDIR /app`**
 → Thiết lập thư mục làm việc là `/app`, giúp tổ chức code gọn gàng và rõ ràng.

**`COPY . /app`**
 → Sao chép toàn bộ mã nguồn và file cấu hình vào container.

**`COPY data /app/data`**
 → Đảm bảo thư mục `data` chứa CSV được copy riêng biệt vào đúng vị trí `/app/data` → tránh lỗi không tìm thấy file khi đọc dữ liệu.

**`RUN python3 -m pip install -r requirements.txt`**
 → Cài đặt tất cả thư viện cần thiết từ file `requirements.txt` để code chạy được trong container.



+ ***tạo file schema.sql***

  ```
  DROP TABLE IF EXISTS transactions;
  DROP TABLE IF EXISTS products;
  DROP TABLE IF EXISTS accounts;
  
  CREATE TABLE accounts (
      customer_id     INT PRIMARY KEY,
      first_name      VARCHAR(50),
      last_name       VARCHAR(50),
      address_1       VARCHAR(100),
      address_2       VARCHAR(100),
      city            VARCHAR(50),
      state           VARCHAR(20),
      zip_code        VARCHAR(10),
      join_date       DATE
  );
  
  CREATE TABLE products (
      product_id           INT PRIMARY KEY,
      product_code         VARCHAR(10),
      product_description  TEXT
  );
  
  CREATE TABLE transactions (
      transaction_id    VARCHAR(50) PRIMARY KEY,
      transaction_date  DATE,
      product_id        INT,
      quantity          INT,
      account_id        INT,
      FOREIGN KEY (product_id) REFERENCES products(product_id),
      FOREIGN KEY (account_id) REFERENCES accounts(customer_id)
  );
  
  -- Index để tăng hiệu suất tìm kiếm
  CREATE INDEX idx_transaction_date ON transactions(transaction_date);
  CREATE INDEX idx_account_state ON accounts(state);
  
  ```

  

  **Định nghĩa cấu trúc cơ sở dữ liệu**:
   → Giúp tạo **các bảng (`tables`)** cần thiết tương ứng với dữ liệu trong các file CSV (`accounts.csv`, `products.csv`, `transactions.csv`).

  **Thiết lập mối quan hệ giữa các bảng**:
   → Dùng **khóa chính (`PRIMARY KEY`)** và **khóa ngoại (`FOREIGN KEY`)** để đảm bảo dữ liệu được liên kết đúng logic, ví dụ:

  - `transactions.account_id` phải tồn tại trong `accounts.customer_id`
  - `transactions.product_id` phải tồn tại trong `products.product_id`

  **Tăng hiệu năng truy vấn dữ liệu**:
   → Thêm **index** để tối ưu khi tìm kiếm theo ngày giao dịch (`transaction_date`) hoặc theo tiểu bang khách hàng (`state`).

  

+ ***viết lại code file main.py***

  ```
  import psycopg2
  import csv
  from datetime import datetime
  
  def create_tables(cur):
      with open('schema.sql', 'r') as f:
          cur.execute(f.read())
  
  def insert_accounts(cur):
      with open('data/accounts.csv', newline='') as csvfile:
          reader = csv.DictReader(csvfile)
          for row in reader:
              cur.execute("""
                  INSERT INTO accounts (customer_id, first_name, last_name, address_1, address_2, city, state, zip_code, join_date)
                  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
              """, (
                  int(row['customer_id']),
                  row['first_name'],
                  row['last_name'],
                  row['address_1'],
                  row['address_2'] if row['address_2'] else None,
                  row['city'],
                  row['state'],
                  row['zip_code'],
                  datetime.strptime(row['join_date'], '%Y/%m/%d').date()
              ))
  
  def insert_products(cur):
      with open('data/products.csv', newline='') as csvfile:
          reader = csv.DictReader(csvfile)
          for row in reader:
              cur.execute("""
                  INSERT INTO products (product_id, product_code, product_description)
                  VALUES (%s, %s, %s)
              """, (
                  int(row['product_id']),
                  row['product_code'],
                  row['product_description']
              ))
  
  def insert_transactions(cur):
      with open('data/transactions.csv', newline='') as csvfile:
          reader = csv.DictReader(csvfile)
          for row in reader:
              cur.execute("""
                  INSERT INTO transactions (transaction_id, transaction_date, product_id, quantity, account_id)
                  VALUES (%s, %s, %s, %s, %s)
              """, (
                  row['transaction_id'],
                  datetime.strptime(row['transaction_date'], '%Y/%m/%d').date(),
                  int(row['product_id']),
                  int(row['quantity']),
                  int(row['account_id'])
              ))
  
  def main():
      conn = psycopg2.connect(
          host="postgres",
          database="postgres",
          user="postgres",
          password="postgres"
      )
      cur = conn.cursor()
      create_tables(cur)
      insert_accounts(cur)
      insert_products(cur)
      insert_transactions(cur)
      conn.commit()
      cur.close()
      conn.close()
      print("✅ Database loaded successfully.")
  
  if __name__ == "__main__":
      main()
  ```



File `main.py` được viết để tự động kết nối đến cơ sở dữ liệu PostgreSQL, tạo bảng theo định nghĩa trong file `schema.sql`, và nạp dữ liệu từ các file CSV (`accounts.csv`, `products.csv`, `transactions.csv`) vào các bảng tương ứng. Chương trình sử dụng thư viện `psycopg2` để thực hiện các câu lệnh SQL trong Python. Dữ liệu ngày tháng được chuyển về đúng định dạng PostgreSQL, và các trường trống được xử lý phù hợp (như `None` cho địa chỉ phụ). Việc tách ra thành các hàm giúp mã rõ ràng, dễ quản lý và tái sử dụng.



***Lý do thay đổi file data***

Khi đọc file CSV bằng Python (`pandas`, `csv.reader`) hoặc chèn vào PostgreSQL, các khoảng trắng dư thừa ở đầu/cuối mỗi trường dữ liệu có thể gây:

Lỗi khi so sánh dữ liệu (`'Widget Medium'` khác `' Widget Medium'`)

Gây kết nối sai giữa các bảng khi thiết lập `FOREIGN KEY`, vì giá trị có khoảng trắng không trùng khớp

Gây khó khăn trong việc truy vấn SQL chính xác

**nên nhóm đã quyết định bỏ khoảng trắng sau dấu phẩy ở 3 file trong mục data**



- ***accounts.csv***

  ```
  customer_id,first_name,last_name,address_1,address_2,city,state,zip_code,join_date
  4321,john,doe,1532 East Main St.,PO BOX 5,Middleton,Ohio,50045,2022/01/16
  5677,jane,doe,543 Oak Rd.,,BigTown,Iowa,84432,2021/05/07
  ```

+ ***products.csv***

  ```
  product_id,product_code,product_description
  345,01,Widget Medium
  241,02,Widget Large
  ```

+ ***transactions.csv***

  ```
  transaction_id,transaction_date,product_id,product_code,product_description,quantity,account_id
  AS345-ASDF-31234-FDAAD-9345,2022/06/01,345,01,Widget Medium,5,4321
  9234A-JFDA-87654-BFAEA-0932,2022/06/02,241,02,Widget Large,1,5677
  ```



## CÁC BƯỚC KHỞI TẠO VÀ ẢNH KẾT QUẢ CỦA EXERCISE 5

-  ***bước 1***

```
docker build --tag=exercise-5 .
```

[KẾT QUẢ BƯỚC 1](https://drive.google.com/file/d/1IMdkEXbY9EXSTAf2NkJdKbz4jWg_NdiN/view?usp=drive_link)

- ***bước 2***

```
docker-compose build
docker-compose up run
```

[KẾT QUẢ BƯỚC 2](https://drive.google.com/file/d/1QSTqdkOEbxZ4ZwL3NpQUsSKqfVEQp4oM/view?usp=drive_link)



- ***bước 3***: Truy cập vào PostgreSQL Container và kiểm tra các bảng đã được tạo chưa

  ```
   docker exec -it exercise-5-postgres-1 psql -U postgres
   
   \dt
   
   SELECT * FROM accounts LIMIT 10;
   SELECT * FROM products LIMIT 10;
   SELECT * FROM transactions LIMIT 10;
  ```

[KẾT QUẢ BƯỚC 3](https://drive.google.com/file/d/1pW3lKT7wuuz6GDhqJjcMEJDNmPVGG6tm/view?usp=drive_link)











