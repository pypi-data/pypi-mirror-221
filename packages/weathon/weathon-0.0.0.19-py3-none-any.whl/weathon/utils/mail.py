


# -*- coding: utf-8 -*-
# @Time    : 2022/12/22 22:11
# @Author  : LiZhen
# @FileName: email_utils.py
# @github  : https://github.com/Lizhen0628
# @Description:

import os
from typing import List
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from weathon.utils.constants import SMPT_HOST, SMPT_PASSWORD, SMPT_NAME,SMPT_PORT, SMPT_USER


# def send_email(to_users: str, subject: str = "", content: str = "", filenames: List[str] = None):
#     """
#     发送邮件
#     Args:
#         to_users: 收件人， 多个收件人用英文分号进行分割
#         subject: 邮件主题
#         content: 邮件正文内容
#         filenames: 附件，要发送的文件路径
#     Returns:
#     """
#     email = MIMEMultipart()
#     email['From'] = SMPT_NAME
#     email['To'] = to_users
#     email['Subject'] = subject

#     message = MIMEText(content)
#     email.attach(message)

#     for filename in filenames or []:
#         display_filename = os.path.basename(filename)
#         fp = open(filename, 'rb')
#         attachment = MIMEApplication(fp.read())
#         attachment.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', display_filename))
#         email.attach(attachment)
#         fp.close()

#     email_host = SMPT_HOST # 邮件服务器域名(自行修改)
#     email_port = SMPT_PORT  # 邮件服务端口(通常是465)

#     smtp = smtplib.SMTP_SSL(email_host, email_port)  # 创建SMTP_SSL对象(连接邮件服务器)
#     smtp.login(SMPT_NAME, SMPT_PASSWORD)  # 通过用户名和授权码进行登录  
#     smtp.sendmail(SMPT_NAME, to_users.split(';'), email.as_string())  # 发送邮件(发件人，收件人，邮件内容)


def send_email(receivers:List[str]=['16621660628@163.com'], subject:str="Python SMTP 邮件测试 subject", content:str="Python 邮件发送测试...",filenames: List[str] = None ):
    """
    发送邮件
    Args:
        receivers: 收件人
        subject: 邮件主题
        content: 邮件正文内容
        filenames: 附件，要发送的文件路径
    """
    # 第三方 SMTP 服务
    smpt_host = SMPT_HOST #设置服务器
    smpt_port = SMPT_PORT
    smpt_name = SMPT_NAME
    smpt_pass = SMPT_PASSWORD #口令 
    smpt_user = SMPT_USER   #用户名
    
    sender = smpt_user
     
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header("from_header", 'utf-8')
    message['To'] =  Header("to_header", 'utf-8')
    
    subject = subject
    message['Subject'] = Header(subject, 'utf-8')

    # multi_parts = MIMEMultipart()
    # multi_parts.attach(message)
    # for filename in filenames or []:
    #     display_filename = os.path.basename(filename)
    #     fp = open(filename, 'rb')
    #     attachment = MIMEApplication(fp.read())
    #     attachment.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', display_filename))
    #     multi_parts.attach(attachment)
    #     fp.close()
    
    smtp = smtplib.SMTP() 
    try:
        smtp.connect(smpt_host, smpt_port)    # 25 为 SMTP 端口号
        smtp.login(smpt_user,smpt_pass)  
        smtp.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
    smtp.quit()






if __name__ == '__main__':
    content_str = """在前面的课程中，我们已经"""
    # filenames = ['logger.py']
    send_email(receivers="16621660628@163.com", subject="邮件测试", content=content_str)
