# boat-app

Flask-based web application that allows users to book charter boats and view the availability of boats. The application provides a user-friendly interface for selecting available dates, making reservations, and selling boats. Website pulls information from MongoDB Database, and displays the available boats in homepage(Some for sale and some for charter).  


## Features

- **Charter Boats:** Browse and book charter boats with ease. Check real-time availability in a calendar, select preferred dates, and make reservations effortlessly.

- **Boats For Sale:** Browse boats for sale, boat listing page has a gallery and description for each listing.

- **MongoDB Integration:** Platform pulls data from a MongoDB Database, ensuring up-to-date and automatically updating webpage when there are new boats or one was sold.

- **Automated Emails with smtplib:** Seamlessly communicate with boat owners or potential buyers through automated emails, powered by the `smtplib` library.


