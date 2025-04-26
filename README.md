Hướng Dẫn Chạy Chương Trình Backup Database
Đây là chương trình Python để backup file database (.sql, .sqlite3) lúc 00:00 hàng ngày và gửi email thông báo kết quả (thành công hoặc thất bại). Dưới đây là hướng dẫn chi tiết để chạy chương trình.

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

Trong thư mục dự án, chạy lệnh để cài các thư viện cần thiết:pip install -r requirements.txt


Các thư viện bao gồm:
python-dotenv: Để đọc file .env.
schedule: Để lập lịch backup.



4. Cấu Hình File .env

Tạo file .env trong thư mục dự án với nội dung:SENDER_EMAIL=your_email@gmail.com
APP_PASSWORD=your_app_password
RECEIVER_EMAIL=receiver_email@gmail.com


Lưu ý:
SENDER_EMAIL: Email Gmail của bạn.
APP_PASSWORD: Mật khẩu ứng dụng Gmail. Cách lấy:
Vào Google Account > Security.
Bật 2-Step Verification (nếu chưa bật).
Vào App Passwords, tạo mật khẩu mới cho ứng dụng (chọn "Mail").


RECEIVER_EMAIL: Email nhận thông báo.
Không push file .env lên GitHub (đã được bỏ qua trong .gitignore).



5. Chuẩn Bị File Database

Tạo thư mục databases trong thư mục dự án:mkdir databases


Đặt ít nhất một file .sql hoặc .sqlite3 vào thư mục databases (ví dụ: test.sql).
Tạo file mẫu:echo. > databases\test.sql





6. Chạy Chương Trình

Chạy file backup_database.py:python backup_database.py


Chương trình sẽ:
Chờ đến 20:00 hàng ngày để backup file từ databases sang backups.
Gửi email thông báo kết quả (thành công hoặc thất bại) đến RECEIVER_EMAIL.


Để test ngay, sửa dòng:schedule.every().day.at("20:00").do(sao_luu_db)

thành:sao_luu_db()

rồi chạy lại. Sau khi test, khôi phục dòng gốc.

7. Kiểm Tra Kết Quả

Kiểm tra thư mục backups để xem file backup (có dạng tenfile_backup_YYYYMMDD_HHMMSS.sql).
Kiểm tra email nhận được (thành công hoặc lỗi).

Lưu Ý

Đảm bảo máy tính có kết nối internet khi chạy để gửi email.
Nếu gặp lỗi, kiểm tra:
File .env có đúng định dạng không.
Mật khẩu ứng dụng Gmail có chính xác không.
Thư mục databases có file .sql hoặc .sqlite3 không.


Liên hệ em nếu cần hỗ trợ: [email hoặc thông tin liên hệ của bạn].

Tác Giả

Tên: [Tên của bạn]
MSSV: [Mã số sinh viên của bạn]
Lớp: [Tên lớp]

