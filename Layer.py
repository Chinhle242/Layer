import smtplib

sender_email = "leducchinhle2002@gmail.com"
receiver_email = "lecoi224466@gmail.com"
password = "Leducchinhle0" # Nhập mật khẩu email của bạn vào đây

message = """\
Subject: helo

xin chào"""

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message)
print("Đã gửi email thành công đến", receiver_email)
server.quit()
