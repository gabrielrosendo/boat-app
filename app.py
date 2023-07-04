from datetime import datetime
from flask import Flask, jsonify, render_template, url_for, request
from tkcalendar import *
import smtplib
from email.message import EmailMessage
import smtplib
import datetime
import os


app = Flask(__name__)


@app.route('/')
def index():
    image_url = url_for('static', filename='images/index.jpg')
    return render_template('index.html', image_url=image_url)

@app.route('/contact')
def contact():
    return render_template('contact.html')

def get_booked_dates():
    return [
        {'start_date': '2023-06-05', 'end_date': '2023-06-10'},
        {'start_date': '2023-06-15', 'end_date': '2023-06-20'},
        {'start_date': '2023-06-25', 'end_date': '2023-06-28'},
        {'start_date': '2023-06-28', 'end_date': '2023-07-02'}
    ]

@app.route('/info', methods=['GET', 'POST'])
def info():
    today = datetime.date.today()
    booked_dates = get_booked_dates()
    filtered_dates = [date for date in booked_dates if datetime.date.fromisoformat(date['end_date']) >= today]

    if request.method == 'POST':
        startDate = request.form.get('startDate')
        endDate = request.form.get('endDate')
        numDays = request.form.get('numDays')
        # check if payment went through
        # if so, update the database with the selected dates (mark them as unavailable)
        # current handling counts start and end date as part of the rental, please verify
        # if payment didn't go through, present an error and reload the page
        # conect with square
        print(startDate)
        print(endDate)
        print(numDays)
        return render_template('charterboat.html', unavailable_dates=filtered_dates, message = "Your request is being processed. \n You will receive an email shortly with the next steps.")

    if request.method == 'GET':
        return render_template('charterboat.html', unavailable_dates=filtered_dates)

@app.route('/info-sale', methods=['GET', 'POST'])
def infoSale():
    if request.method == 'POST':
        if request.form:
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            email = request.form['email']
            phone = request.form['phone']
            if (
            firstname and lastname  and phone and email
            ):
                message = "Thank you! We will be in touch."
                color_message = "green"
                email_content = f"""
                First Name: {firstname}
                Last Name: {lastname}
                Email: {email}
                Phone: {phone}
                """
                subject = f"Boat Purchase Inquiry - {email}"
                send_email(email_content, subject)
            else:
                message = "Please fill in all fields."
                color_message = "red"
            return render_template('forSale.html', message=message, color_message=color_message)
        return render_template('forSale.html')

    if request.method == 'GET':
        return render_template('forSale.html')

@app.route('/get-dates', methods=['GET'])
def get_dates():
    today = datetime.date.today()
    booked_dates = get_booked_dates()
    filtered_dates = [date for date in booked_dates if datetime.date.fromisoformat(date['end_date']) >= today]

    response = {'unavailable_dates': filtered_dates}
    return jsonify(response)

@app.route('/sell', methods = ['GET', 'POST'])
def sell_boat():
    if request.method=='GET':
        return render_template('sellboat.html')
    if request.method == "POST":
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        phone = request.form['phone']
        boatmake = request.form['boatmake']
        boatmodel = request.form['boatmodel']
        year = request.form['year']
        condition = request.form['condition']
        price = request.form['price']
        description = request.form['description']

        if (
            firstname and lastname and email and phone and boatmake and
            boatmodel and year and condition and price and description
        ):
            message = "Thank you! We will be in touch."
            color_message = "green"
            email_content = f"""
            First Name: {firstname}
            Last Name: {lastname}
            Email: {email}
            Phone: {phone}
            Boat Make: {boatmake}
            Boat Model: {boatmodel}
            Year: {year}
            Condition: {condition}
            Price: {price}
            Description: {description}
            """
            subject = f"Boat Selling Inquiry - {email}"
            send_email(email_content, subject)

        else:
            message = "Please fill in all fields."
            color_message = "red"

        return render_template('sellboat.html', message=message, color_message=color_message)

# send emails when required
def send_email(email_content, subject):
    # Email settings
    sender_email = "gabrielrosendo72@gmail.com"
    receiver_email = "gabrielrosendo11@gmail.com"
    
    # Create the email message
    em = EmailMessage()
    em['From'] = sender_email
    em['To'] = receiver_email
    em['Subject'] = subject
    em.set_content(email_content)

    email_password = os.environ.get("EMAIL_PASSWORD")

    # Send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, email_password)
        smtp.sendmail(sender_email, receiver_email, em.as_string())
    return 

app.run(host='0.0.0.0', port=5001)
