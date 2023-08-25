from datetime import datetime
import json
from flask import Flask, jsonify, render_template, url_for, request
import smtplib
from email.message import EmailMessage
import smtplib
import datetime
import os
import utils



app = Flask(__name__)

# Connect to DB
boats_sale = utils.boats_sale
boats_collection = utils.sale_collection 

collection = utils.sale_collection


@app.route('/')
def index():
    image_url = url_for('static', filename='images/index.jpg')
    boats_charter =  [boats_sale[0], boats_sale[1]]
    return render_template('index.html', image_url=image_url, boats_sale = boats_sale, boats_charter = boats_charter)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        inquiry = request.form['inquiry']
        if firstname and lastname and inquiry and email:
            message = "Thank you! We will be in touch."
            color_message = "green"
            email_content = f"""
            First Name: {firstname}
            Last Name: {lastname}
            Email: {email}
            Inquiry: {inquiry}
            """
            subject = f"Contact Inquiry - {email}"
            send_email(email_content, subject)
        else:
            message = "There was an error processing your request. Please try again."
            color_message = "red"
        return render_template('contact.html', message = message, color_message = color_message)

    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

def get_booked_dates():
    return [
        {'start_date': '2023-06-05', 'end_date': '2023-06-10'},
        {'start_date': '2023-06-15', 'end_date': '2023-06-20'},
        {'start_date': '2023-06-25', 'end_date': '2023-06-28'},
        {'start_date': '2023-06-28', 'end_date': '2023-07-02'}
    ]

@app.route('/info/<string:boat_name>', methods=['GET', 'POST'])
def info(boat_name):
    #fix to handle dates when neccessary
    today = datetime.date.today()
    booked_dates = []
    filtered_dates = [date for date in booked_dates if datetime.date.fromisoformat(date['end_date']) >= today]
    
    boat_info = boats_collection.find_one({'boat_name': boat_name})
    folder_path = f'static/images/gallery/{boat_info["_id"]}'
    file_names = [file for file in os.listdir(folder_path) if not file.startswith('.')]
    images = json.dumps(file_names)

    if request.method == 'POST':
        startDate = request.form.get('startDate')
        endDate = request.form.get('endDate')
        numDays = request.form.get('numDays') 
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        if (
            firstname and lastname  and numDays and email
            ):
                message = "Thank you! We will be in touch."
                color_message = "green"
                email_content = f"""
                First Name: {firstname}
                Last Name: {lastname}
                Email: {email}
                Start Date: {startDate}
                End Date: {endDate}
                Number of Days: {numDays}
                """
                subject = f"Boat Charter Inquiry - {email}"
                send_email(email_content, subject)
        else:
            message = "There was an error proccessing your request. Please try again."
            color_message = "red"

        return render_template('charterboat.html', unavailable_dates=filtered_dates,boat_info=boat_info, image_names = images, file_names = file_names, message = message, color_message = color_message)

    if request.method == 'GET':
        return render_template('charterboat.html', unavailable_dates=filtered_dates, boat_info=boat_info, image_names = images, file_names = file_names)

@app.route('/info-sale/<string:boat_name>', methods=['GET', 'POST'])
def infoSale(boat_name):
    boat_info = boats_collection.find_one({'boat_name': boat_name})
    folder_path = f'static/images/gallery/{boat_info["_id"]}'
    file_names = [file for file in os.listdir(folder_path) if not file.startswith('.')]
    images = json.dumps(file_names)

    if request.method == 'GET':
        if boat_info:
            description_first = boat_info.get("description")
            description = description_first.replace('\n', '<br>')

            return render_template('forSale.html', boat_info=boat_info, description = description, image_names = images, file_names = file_names)
        else:
            message="Boat not found"  
            color_message = "red"
            return render_template('forSale.html', message=message, color_message=color_message)

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
            return render_template('forSale.html', boat_info=boat_info, image_names = images, file_names = file_names, message=message, color_message=color_message)
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
        year = request.form['year']
        condition = request.form['condition']

        if (
            firstname and lastname and email and phone and boatmake
            and year and condition
        ):
            message = "Thank you! We will be in touch soon."
            color_message = "green"
            email_content = f"""
            First Name: {firstname}
            Last Name: {lastname}
            Email: {email}
            Phone: {phone}
            Boat Make: {boatmake}
            Year: {year}
            Condition: {condition}
            """
            subject = f"Boat Selling Inquiry - {email}"
            send_email(email_content, subject)

        else:
            message = "Please fill in all fields."
            color_message = "red"

        return render_template('sellboat.html', message=message, color_message=color_message)

# Send emails when required
def send_email(email_content, subject):
    # Email settings
    sender_email = "tonyyachts0@gmail.com"
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
