
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from copy import deepcopy

import email_builder.clients

class Email:

  def __init__(self):
    self.__message = MIMEMultipart('mixed')
    self.__body = MIMEMultipart('alternative')
    self.__charset = "utf-8"
    self.__sender = None
    self.__recipients = []

  def __str__(self):
    temp = deepcopy(self.__message)
    temp.attach(self.__body)
    return str(temp)
    
  def get_sender(self):
    return self.__sender
    
  def get_recipients(self):
    return self.__recipients
  
  def sender(self, sender):
    self.__message["From"] = sender
    self.__sender = sender
    return self

  def to(self, *recipients):
    for recipient in recipients:
      self.__message["To"] = recipient
      self.__recipients.append(recipient)
    return self
  
  def cc(self, *recipients):
    for recipient in recipients:
      self.__message["Cc"] = recipient
    return self
  
  def bcc(self, *recipients):
    for recipient in recipients:
      self.__message["Bcc"] = recipient
    return self

  def subject(self, subject):
    self.__message["Subject"] = subject
    return self
  
  def html(self, data):
    self.__body.attach(MIMEText(data.encode(self.__charset), 'html', self.__charset))
    return self
  
  def text(self, data):
    self.__body.attach(MIMEText(data.encode(self.__charset), 'plain', self.__charset))
    return self
  
  def attachment(self, *attachments):
    for attachment in attachments:
      self.__body.attach(attachment.object)
    return self
  
  def send(self, service):
    return service.send(self)
    
    
class Attachment:

  def __init__(self, filename, contents, encoding="utf-8"):
    contents = contents if isinstance(contents, bytes) else contents.encode(encoding)
    self.object = MIMEApplication(contents)
    self.object.add_header('Content-Disposition','attachment',filename=filename)
