
import boto3
import logging
import typing
import smtplib


class EmailServer:
    def send(self, email): raise NotImplementedError("subclass needs to implement this method")


class SES(EmailServer):

    def __init__(self, session=boto3.Session(region_name="us-west-2")):
        self.client = session.client(service_name='ses')

    def send(self, email):
        try:
            response = self.client.send_raw_email(RawMessage={'Data': str(email)})
        except ClientError as e:
            return {
                "status": "failed",
                "message-id": None,
                "error": e,
            }
        else:
            return {
                "status": "passed",
                "message-id": response['ResponseMetadata']['RequestId'],
                "error" : None,
            }


class Gmail(EmailServer):

    def __init__(self, **kwargs):
        self.__address = kwargs.get("address", "smtp.gmail.com")
        self.__port = kwargs.get("port", 465)
        self.__password = kwargs.get("password")

    def send(self, email):
        try:
            with smtplib.SMTP_SSL(self.__address, self.__port) as smtp_server:
                smtp_server.login(email.get_sender(), self.__password)
                smtp_server.sendmail(email.get_sender(), ",".join(email.get_recipients()), str(email))
        except Exception as e:
            return {
                "status": "failed",
                "error": e,
            }
        else:
            return {
                "status": "passed",
                "error" : None,
            }

