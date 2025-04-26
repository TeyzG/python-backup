Hướng Dẫn Chạy Chương Trình Backup Database
Đây là chương trình Python để backup file database (.sql, .sqlite3) lúc 00:00 hàng ngày và gửi email thông báo kết quả (thành công hoặc thất bại). Dưới đây là hướng dẫn chi tiết để chạy chương trình.

Cấu trúc dự án

![image](https://github.com/user-attachments/assets/234297b3-dacf-4866-a90d-3735d3706c0a)

Các Bước Cài Đặt và Chạy
1. Cài Đặt Python

Tải Python từ python.org.
Cài đặt và đảm bảo tích chọn **Add Python to PATH** (trên Windows).
Kiểm tra Python bằng lệnh:

![image](https://github.com/user-attachments/assets/5a3936e7-ea75-4e79-a76f-1067fab99f88)

Nếu thấy phiên bản (ví dụ: Python 3.13.0), Python đã cài đúng.

2. Tải Dự Án

Tải source code từ GitHub (hoặc clone repository):git clone <link-repo-cua-ban>
Vào thư mục dự án:cd <ten-thu-muc>

3. Cài Đặt Thư Viện

Trong thư mục dự án
Các thư viện bao gồm:
python-dotenv: Để đọc file .env.
schedule: Để lập lịch backup.

4. Cấu Hình File .env
   
![image](https://github.com/user-attachments/assets/bfcd9a0f-6b0a-4d9c-9c59-902a7343f532)

Tạo file .env trong thư mục dự án với nội dung:
SENDER_EMAIL=your_email@gmail.com
APP_PASSWORD=your_app_password
RECEIVER_EMAIL=receiver_email@gmail.com

![image](https://github.com/user-attachments/assets/9c9b1d51-8266-4adf-ae57-068d98529f1b)

5. Chuẩn Bị File Database

Tạo thư mục databases trong thư mục dự án:
Đặt ít nhất một file .sql hoặc .sqlite3 vào thư mục databases (ví dụ: test.sql).
Tạo file mẫu:echo. > databases\test.sql

6. Chạy Chương Trình

Chạy file backup_database.py:

![image](https://github.com/user-attachments/assets/c66622f0-ea57-46f3-8b46-c791eab8e17f)

Chương trình sẽ:
Chờ đến 00:00 hàng ngày để backup file từ databases sang backups.
Gửi email thông báo kết quả (thành công hoặc thất bại) đến RECEIVER_EMAIL.
rồi chạy lại. Sau khi test, khôi phục dòng gốc.

7. Kiểm Tra Kết Quả

![image](https://github.com/user-attachments/assets/2ed2f45d-32e2-4ff6-bb01-692be88a5409)

Kiểm tra thư mục backups để xem file backup (có dạng tenfile_backup_NamThangNgay_GioPhutGiay.sql).

![image](https://github.com/user-attachments/assets/740f0a83-1efb-4d0d-a84d-a79934f9b2e4)

Kiểm tra email nhận được (thành công hoặc lỗi).

![image](https://github.com/user-attachments/assets/f600b450-06e9-48da-ac30-94252868f592)



Liên hệ em nếu cần hỗ trợ: luong_2251220018@dau.edu.vn

**Tác Giả**
Tên: Nguyễn Hoàng Lương
MSSV: 2251220018
Lớp: 22CT1

