import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"

#Change these
sender_email = ""
password = ""
receiver_email = ""


def send(subject, message):
    if sender_email == "":
        print("Unable to send mail because sender_email is blank.")
        instructions()
        exit()
    if receiver_email == "":
        print("Please set receiver_email to your email address.")
        instructions()
        exit()
    else:
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            try:
                server.login(sender_email, password)
            except:
                print("A login error occured. Please check email, password, and that you set \"Allow less secure apps\" to true. You can do this at https://myaccount.google.com/lesssecureapps.")
                instructions()
                exit()
            server.sendmail(sender_email, receiver_email, "subject: "+subject+"\n\n"+message)


def instructions():
        print("\n")
        print("To use pymail:\n(1) Create a new email with google for pymail to send messages from.\n(2) Go to https://myaccount.google.com/lesssecureapps and set \"Allow less secure apps\" for the new email address to true. Make sure your at the right email address.\n(3) Open pymail.py\n(4) Set sender_email and password to the corresponding info.\n(5) Set receiver_email to your email address.\n(6) Import pymail and run pymail.send(subject, message).\nRun this program again to send a test email.")
        print("\n")


if __name__ == '__main__':
    if sender_email != "":
        print("Running test email")
        print("Sending email to {} from {}".format(receiver_email, sender_email))
        send("Running Test", "This email was sent to test that pymail was set up correctly.")
        print("Email sent")

    else:
        instructions()
   
