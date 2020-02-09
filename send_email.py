import smtplib, requests
from flask import Flask
from email.mime.text import MIMEText

# Initialize the Flask service
app = Flask(__name__)

@app.route('/email', methods=['GET'])
def send_email():
    # Make the GET request from app.py
    request = requests.get('https://wedding-survey-service.herokuapp.com/guests')

    # Parse the data into a JSON file
    temp = request.json()
    data = temp[len(temp)-1] # Get the latest element added to the JSON file

    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '7728418512a6c8'
    password = '8f360fdf9cb5db'
    message = f"<p>Dear {data['guest']}, </br>Thank you for your feedback! We are happy you enjoyed our wedding! And we are a lot more excited by the fact that your favorite thing was " + str(data['favorite']).lower() + "<p>With love,</br>Alexu &Lavi"

    sender_email = "alexu_lavi@weddings.com"
    reciever_email = data['email']
    msg = MIMEText(message, 'html')
    msg['Subject'] = "Wedding survey"
    msg['From'] = sender_email
    msg['To'] = reciever_email

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, reciever_email, msg.as_string())

if __name__ == "__main__":
    app.debug = True
    app.run()