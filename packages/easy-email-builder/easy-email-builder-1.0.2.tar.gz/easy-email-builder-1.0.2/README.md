# email-builder
This is a module to make it simple to send emails. The code follows the builder design pattern and the 
email code is completely separated from the client used to actually send the email, making it easy to switch to
a new client if we ever need to move away from SES for whatever reason.

## Sample Usage

#### Install
```
pip install easy-email-builder
```

#### Setup

```python
import email_builder
```

#### Send an email from Gmail

```python
# builder syntax
# when using gmail, you need an "App Password". follow this link if you need help creating that:
# https://www.lifewire.com/get-a-password-to-access-gmail-by-pop-imap-2-1171882

import email_builder

client = email_builder.clients.Gmail(password="<gmail APP password>")
email = (
  email_builder.Email()
    .sender("your.email@gmail.com")
    .to("someones.email@gmail.com")
    .cc("copy.email@gmail.com")
    .bcc("another.copy.email@gmail.com")
    .subject("test email sent from my python lib")
    .text("hello world")
)
email.send(client)
```

#### Send an email Amazon SES with just some html as the body

```python
# builder syntax 
import email_builder

# this SES class accepts a boto3 session if you want to customize the setup
client = email_builder.clients.SES()
email = (
  email_builder.Email()
    .sender("my.email@company.com")
    .to("recipient.1@company.com")
    .to("recipient.2@company.com")
    .subject("test email sent from my python lib")
    .html("<h1> hello world </h1>")
)
email.send(email_builder.clients.SES())
```

#### Send an email with attachments

```python
# note that the contents of the attachments can be either string or bytestring 
import email_builder

with open("report.csv", "rb") as f:
  data = f.read()

client = email_builder.clients.SES()
email = (
  email_builder.Email()
    .sender("my.email@company.com")
    .to("recipient.1@company.com")
    .to("recipient.2@company.com")
    .subject("test email sent from my python lib")
    .html("<h1> hello world </h1>")
    .attachment(email_builder.Attachment("report.csv", data))
    .attachment(email_builder.Attachment("test2.json", """{"key": "value"}"""))
).send(email_builder.clients.SES())
```

## Email Options

```python
import email_builder

with open("report.csv", "rb") as f:
  data = f.read()

# --- client types are SES or Gmail --- #
# Amazon SES that can accept a session object as needed
client = email_builder.clients.SES()
# or
import boto3
session = boto3.Session(region="us-west-2", etc)
client = email_builder.clients.SES(session)

# Gmail that accepts a password and options to configure port/url if needed
client = email_builder.clients.SES(password="<password>")


# --- email options --- #
email = (
  email_builder.Email()

    # sender(sender:str) -> only one sender allowed, no chaining allowed on sender
    .sender("my.email@company.com")

    # to(*recipients:str) -> you can add as many as you want here, and chain to()
    #                        calls successively
    .to("recipient.1@company.com")
    .to("recipient.2@company.com")

    # cc(*recipients:str) -> you can add as many as you want here, and chain to()
    #                        calls successively
    .cc("recipient.1@company.com")
    .cc("recipient.2@company.com")

    # bcc(*recipients:str) -> you can add as many as you want here, and chain to()
    #                        calls successively
    .bcc("recipient.1@company.com")
    .bcc("recipient.2@company.com")

    # subject(subject:str) -> only one subject line allowed
    .subject("test email sent from my python lib")

    # --- EMAIL BODY --- #
    # you need to choose between either html or text, can't use both

    # html(body:str) -> renders the given html in the email body, no chaining
    .html("<h1> hello world </h1>")

    # test(body:str) -> adds the given text to the email body as plain text
    .text("hello world")

    # attachment(attachment:email_builder.Attchment) -> chain as many of these as you want
    .attachment(email_builder.Attachment("report.csv", data))
    .attachment(email_builder.Attachment("test2.json", """{"key": "value"}"""))

)

# result contains a dictionary with status in the body
result = email.send(client)
print(result)
```

Success result:
```python
{
	"status": "passed",
	"error": None
}
```

Failure result:
```python
{
	"status": "failed",
	"error": Exception(...)
}
```
