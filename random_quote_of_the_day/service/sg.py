import sendgrid
import os
import json
from sendgrid.helpers.mail import Mail, Email, To, Content


def send_email(from_email, to_email, subject, text_content):
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_SECRET_TOKEN"))
    from_email = Email(from_email)
    to_email = To(to_email)
    content = Content("text/html", text_content)
    mail = Mail(from_email, to_email, subject, content)

    mail_json = mail.get()

    # Send an HTTP POST request to /mail/send
    print("Sending mail:")
    print(json.dumps(mail_json, indent=2))
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)
