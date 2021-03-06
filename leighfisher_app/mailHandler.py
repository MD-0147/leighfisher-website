from django.core.mail import send_mail
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()
    # Contact

def sendMailToContactPerson(name, send_to):
    subject = "Thanks for contacting us"
    message = "Hello "+name+"! \n\nWe have successfully received your message.\n\nWe will get back to you as soon as possible.\n\nRegards\n- Leighfisher Consultancy Pvt. Ltd."
    try:
        send_mail(
            subject,
            message,
            env("EMAIL"),
            [send_to],
            fail_silently = False,
        )
    except:
        print("EMAIL NOT SENT")


def sendMailToLeighfisherContact(name, email, subject, message):
    message = "A new message has been received on our website:\n\nName: "+name+"\nEmail Id: "+email+"\nSubject: "+subject+"\nMessage: "+message+"\n\n\nRegards"
    subject = "A message has been received on Leighfisher Consultancy Pvt. Ltd."
    send_mail(
        subject,
        message,
        env("EMAIL"),
        # ['thetravancorecharitabletrust@gmail.com','hari.vijayan89@gmail.com','thomaslijo634@gmail.com','sajangeorge6040@gmail.com'],
        ['rajabhishek9271@gmail.com'],
        fail_silently = False,

    )
