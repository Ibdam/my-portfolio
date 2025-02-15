from flask_mail import Message,  Mail
from flask import jsonify
from smtplib import SMTPConnectError
import time

# App mail configuration
def mail_config(app):
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = 'olowomojuoredamilola@gmail.com'
    app.config['MAIL_PASSWORD'] = 'jdwb crgl lllx ddfp'

    # mail = Mail(app)
    # return mail

    # Compose the email
def send_email_with_retry(mail, data, retries= 3, delay= 5):
    try:
        msg = Message(
        subject=f"Contact Form Submission from {data['name']}",
        sender=data['email'],
        recipients=['olowomojuoredamilola@gmail.com'],
        body=f"Name: {data['name']}\nEmail: {data['email']}\nMessage: {data['message']}",
        )

        mail.send(msg)
        return 'Thank you for contacting, your message has been received, we will get back to you shortly!'
    
    except SMTPConnectError as e:
        print(f"SMTPConnectError: {e}. Retrying in {delay} seconds...")
        time.sleep(delay)
    
    except Exception as e:
            print(f"Unexpected error: {e}")
            return jsonify({"error": "Failed to send email after multiple attempts."}), 500


    
