"""This showcase the server for my portfolio website using Flask framework"""

# Importing the needed libraries

from flask import Flask, render_template, url_for, request, redirect, send_from_directory
from flask_mail import Mail, Message
import csv
from auto_mail import *
# Creating an app
app= Flask('__name__')

# Configure the app message
mail= mail_config(app)
# Creating route for all HTML template

# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False
# app.config['MAIL_USERNAME'] = 'olowomojuoredamilola@gmail.com'
# app.config['MAIL_PASSWORD'] = 'jdwb crgl lllx ddfp'

mail = Mail(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

# Creating an end point for submit
@app.route('/submit', methods=['POST'])
def submit():
    if request.method=='POST':
        data= request.form.to_dict()
        send_email_with_retry(mail, data)
        # return response
    return render_template('thankYou.html')

# Downloading the cv
@app.route('/download-cv')
def download_cv():
    print('CV downloaded')
    return send_from_directory('static/files', 'Damilola_Ibrahim_Olowomojuore_Resume.pdf', as_attachment= True)

# Running the app
if __name__ == '__main__':
    app.run(debug= True)
