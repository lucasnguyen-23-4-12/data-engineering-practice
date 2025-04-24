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
