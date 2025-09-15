import smtplib
from email.message import EmailMessage


def send_email(subject, body, to_email, cc_emails):
    from_email = "stagtestemail@gmail.com"
    from_name = "QA Reporting-Automation"
    password = "fnmp nrxj olat leyu"

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_name
    msg['To'] = to_email
    msg.set_content(body)
    if cc_emails:
        msg['Cc'] = ", ".join(cc_emails)

    recipients = [to_email] + (cc_emails if cc_emails else [])


    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(from_email, password)
            smtp.send_message(msg, from_addr=from_email, to_addrs=recipients)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")


# Usage example:
# send_email(
#     subject="Automation Script Status",
#     body="Hi Developer,\n\nThe automation script has completed execution.\n\nRegards,\nAutomation Bot",
#     to_email="mubashar4603@gmail.com",
#     cc_emails=["test@gmail.com"]
# )


