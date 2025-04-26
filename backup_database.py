#Nguyen Hoang Luong 22CT1 - Bai tap Backup database
import os
import shutil
import schedule
import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from dotenv import load_dotenv

# doc file env
load_dotenv()

# email gui va nhan
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

# thu muc chua db
DB_FOLDER = "databases"
BACKUP_FOLDER = "backups"

# gui email
def gui_mail(chude, noidung):
    try:
        mail_server = smtplib.SMTP("smtp.gmail.com", 587) # ket noi gmail
        mail_server.starttls()
        mail_server.login(SENDER_EMAIL, APP_PASSWORD)
        message = MIMEText(noidung)
        message["Subject"] = chude
        message["From"] = SENDER_EMAIL
        message["To"] = RECEIVER_EMAIL
        mail_server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())
        mail_server.quit()
        print("Gui mail ok")
    except:
        print("Loi gui mail")

# backup db
def sao_luu_db():
    count = 0  # dem file nhung k dung
    print("Bat dau backup...")
    try:
        if not os.path.exists(BACKUP_FOLDER):
            os.makedirs(BACKUP_FOLDER) # tao folder backup
        now = datetime.now()
        time_string = now.strftime("%Y%m%d_%H%M%S") # lay thoi gian
        for file in os.listdir(DB_FOLDER):
            if file.endswith((".sql", ".sqlite3")):
                count += 1
                src = os.path.join(DB_FOLDER, file)
                new_file = f"{file.split('.')[0]}_backup_{time_string}.{file.split('.')[-1]}"
                dst = os.path.join(BACKUP_FOLDER, new_file)
                shutil.copy2(src, dst)
                print(f"Backup ok: {file}")
        gui_mail(
            "Backup Thanh Cong",
            f"Backup xong luc {now.strftime('%Y-%m-%d %H:%M:%S')}."
        )
    except:
        gui_mail("Backup Loi", "Co loi khi backup")
        print("Loi backup")

#backup db, chay luc 00h hang ngay
schedule.every().day.at("20:00").do(sao_luu_db)

# chay mai mai
while True:
    schedule.run_pending()
    time.sleep(60) # cho 1 phut