#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
# SMTP发送邮件
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_addr = "364206176@qq.com"
password = "nmmktwnhhbzsbhah"
to_addr = "364206176@qq.com"
smtp_server = "smtp.qq.com"


def send_email(from_addr, password, to_addr, smtp_server, msg):
    # smtp协议的默认端口为25
    # ssl加密协议
    server = smtplib.SMTP_SSL(host=smtp_server)
    # 可以不用指定端口号
    # server.connect(smtp_server, smtp_port)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()


def test_send_msg_email():
    msg = MIMEText("Hello, send by Python....", "plain", "utf-8")
    # 主题
    msg["Subject"] = "文本邮件发送测试"
    # 发件人
    msg["from"] = "Mason"
    # 收件人
    msg["To"] = "Mason"

    # # 输入Email地址和口令
    # from_addr = input("From:")
    # password = input("Password:")
    #
    # # 输入收件地址
    # to_addr = input("To:")
    # # 输入SMTP服务器地址
    # smtp_server = input("SMTP server:")
    # smtp_port = 465

    # 发送邮件
    send_email(from_addr, password, [to_addr], smtp_server, msg)


# if __name__ == "__main__":
#     test_send_msg_email()


def test_send_html_email():
    msg = MIMEText("<html><body><h1>Hello</h1>" +
                   "<p>send by <a href='http://www.python.org'>Python</a>...</p>" +
                   "</body></html>", "html", "utf-8")
    # 主题
    msg["Subject"] = "HTML邮件发送测试"
    # 发件人
    msg["from"] = "Mason"
    # 收件人
    msg["To"] = "Mason"
    send_email(from_addr, password, [to_addr], smtp_server, msg)


# if __name__ == "__main__":
#     test_send_html_email()


def test_send_attachment_email():
    msg = MIMEMultipart()
    # 内容
    msg.attach(MIMEText("send with file...", "plain", "utf-8"))
    # 主题
    msg["Subject"] = "附件邮件发送测试"
    # 发件人
    msg["from"] = "Mason"
    # 收件人
    msg["To"] = "Mason"

    # 添加附件
    with open(r"D:\PyCode\PythonStarter\src\main\resources\test_pillow.jpeg", "rb") as image_file:
        # 设置附件的MIME和文件名及类型
        mime = MIMEBase("image", "jpeg", filename="娘口三三.jpeg")
        # 加上必要的头信息
        mime.add_header("Content-Disposition", "attachment", filename="娘口三三.jpeg")
        mime.add_header("Content-ID", "<0>")
        mime.add_header("X-Attachment-Id", "0")
        # 把附件内容读进来
        mime.set_payload(image_file.read())
        # 用base64编码
        encoders.encode_base64(mime)
        # 添加到msg中
        msg.attach(mime)

        send_email(from_addr, password, [to_addr], smtp_server, msg)


if __name__ == '__main__':
    test_send_attachment_email()

# cid:0-->把附件中的图片，添加到html正文中
# msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
#     '<p><img src="cid:0"></p>' +
#     '</body></html>', 'html', 'utf-8'))


# 同时发文本和html
# msg = MIMEMultipart('alternative')
# msg['From'] = ...
# msg['To'] = ...
# msg['Subject'] = ...
#
# msg.attach(MIMEText('hello', 'plain', 'utf-8'))
# msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))

# 加密SMTP
# server.starttls()
# tls加密协议


# 继承关系
# Message
# +- MIMEBase
#    +- MIMEMultipart
#    +- MIMENonMultipart
#       +- MIMEMessage
#       +- MIMEText
#       +- MIMEImage
