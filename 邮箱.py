#连接邮箱服务器
import smtplib
qqMail = smtplib.SMTP_SSL("smtp.qq.com",465)
#登录邮箱
mailUser = "@qq.com"#(邮箱账户)
mailPass = ""#SMTP授权码
qqMail.login(mailUser,mailPass)
#编辑发收件人
from email.mime.multipart import MIMEMultipart
from email.header import Header
sender = "@qq.com"#设置发件人
receiver = "@qq.com"#设置收件人
message = MIMEMultipart()
message["Subject"] = Header("主题")
message["From"] = Header(f"kazhi<{sender}>")
message["To"] = Header(f"某某<{receiver}>")
#构建正文
from email.mime.text import MIMEText
textcontent = "内容"
#1. 第二个参数文本格式plain表示纯文本,第三个编码 utf-8可防止中文乱码
mailcontent = MIMEText(textcontent,"plain","utf-8")
#2. 读取图片文件
fillpath = r"路径"
with open(fillpath,"rb") as image:
    fileContent = image.read()
#设置附件
from email.mime.image import MIMEImage
attachment = MIMEImage(fileContent)
attachment.add_header("Content-Disposition","attachment",filename = "名称")#第三个参数附件名称

message.attach(mailcontent)#添加正文
message.attach(attachment)#添加附件

#发送邮件
qqMail.sendmail(sender,receiver,message.as_string())
print("==发送成功==")
