# boat-app

Flask-based web application that allows users to book charter boats and view the availability of boats. The application provides a user-friendly interface for selecting available dates, making reservations, and selling boats.

## How to Run
1. Clone the repository to your local machine:
 - git clone https://github.com/your-username/charterboat.git
3. Install the required dependencies. You can use pip to install them:
 - pip install Flask tkcalendar
5. Before running the application, set the EMAIL_PASSWORD environment variable to allow sending emails. This variable will be used as the password for the email account used to send notifications about boat selling inquiries:
 - export EMAIL_PASSWORD="your_email_password"
 - python app.py
7. The application will be accessible at http://localhost:5001.

## Features

- Home Page: The landing page of the web application displays an image and provides an introduction to CharterBoat.
- Contact Page: A simple page that allows users to get in touch with the CharterBoat team.
- Boat Availability: Users can view available dates for booking charter boats.
- Book Boat: Users can select start and end dates to book a charter boat. The application checks for payment and marks the selected dates as unavailable if payment goes through.
- Sell Boat: Users can sell their boats by filling out a form with boat details. The inquiry is sent to the email provided.
## Data Storage

- Database: The application uses a database to store information about boats and boat reservations. 
## Technologies Used

- Python
- Flask
- HTML
- CSS
- JQUERY
- tkcalendar
- MongoDB(?)

## Possible Improvements

The following are possible improvements that could be added in the future:

- Add Square for charter payment handling.
- Setup company email to receive inquiries.
- Set up and connect to Database.
- Set up galleries and connect pictures to respective galleries.

This is a private project and is not open-source. All rights reserved.
