#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# POP3接收邮件
# 收取邮件分两步：
# 第一步：用poplib把邮件的原始文本下载到本地；
# 第二部：用email解析原始文本，还原为邮件对象。
import poplib
from email.header import decode_header
from email.parser import Parser
from email.utils import parseaddr

email = "364206176@qq.com"
password = "nmmktwnhhbzsbhah"
pop3_server = "pop.qq.com"
pop3_port = 995


def get_latest_email():
    # 连接到pop3服务器
    server = poplib.POP3_SSL(pop3_server)
    # 打开调试信息
    server.set_debuglevel(1)
    # 打印服务器欢迎文字
    print(server.getwelcome().decode("utf-8"))

    # 身份认证
    server.user(email)
    server.pass_(password)

    # 返回邮箱的数量和占用空间
    print("Messages: %s. Size:%s" % server.stat())
    # 返回所有邮件编号
    resp, mails, octets = server.list()
    # 查看返回列表
    print(mails)

    # 获取最新一封邮件，索引从1开始
    index = len(mails)
    _, lines, _ = server.retr(index)

    # lines存储了邮件原始文本的每一行
    # 获取邮件的原始文本
    msg_content = b"\r\n".join(lines).decode("utf-8")
    # 解析出邮件--MIMEMultipart类型
    msg = Parser().parsestr(msg_content)

    # 可以根据邮件索引号直接从服务器删除邮件:
    # server.dele(index)
    # 关闭连接:
    server.quit()
    return msg


def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def print_info(msg, indent=0):
    if indent == 0:
        for header in ["From", "To", "Subject"]:
            value = msg.get(header, "")
            if value:
                if header == "Subject":
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u"%s <%s>" % (name, addr)
            print("%s%s:%s" % ("  " * indent, header, value))

    if msg.is_multipart():
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print("%spart %s" % ("  " * indent, n))
            print("%s---------------------------" % ("  " * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == "text/plain" or content_type == "text/html":
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print("%sText: %s" % ("  " * indent, content + "..."))
        else:
            print("%sAttachment: %s" % ("  " * indent, content_type))


if __name__ == '__main__':
    msg = get_latest_email()
    print_info(msg)
