import qrcode
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from io import BytesIO

# --- 1. Генерация QR-кода ---
fio = "Иванов Иван Иванович"  # Твои ФИО

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(fio)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# Сохраняем в память (не на диск)
img_byte_arr = BytesIO()
img.save(img_byte_arr, format='PNG')
img_byte_arr.seek(0)

# Данные отправителя и получателя
smtp_server = "smtp.yandex.ru"
smtp_port = 465  # SSL
sender_email = "sokDA2023@yandex.ru"
receiver_email = "sokDA2018@yandex.ru"
password = "sthgqtigkcacuiux"  # пароль приложения

# --- 3. Создаём письмо ---
message = MIMEMultipart("related")
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Письмо с QR-кодом"

# HTML с встраиванием QR
html = """
<html>
  <body>
    <h2>Здравствуйте!</h2>
    <p>Ниже ваш QR-код с ФИО:</p>
    <img src="cid:qrimage" alt="QR Code"/>
  </body>
</html>
"""

msg_alternative = MIMEMultipart("alternative")
message.attach(msg_alternative)
msg_alternative.attach(MIMEText(html, "html"))

# --- 4. Прикрепляем QR как inline-изображение ---
qr_img = MIMEImage(img_byte_arr.read(), _subtype="png")
qr_img.add_header("Content-ID", "<qrimage>")
message.attach(qr_img)

# --- 5. Отправляем письмо ---
with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Письмо с QR-кодом отправлено!")
