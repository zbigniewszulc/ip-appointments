# Infinita Perfectio Booking Platform
The Infinita Perfectio Booking Platform was designed as an add-on to an existing website for a Polish dental clinic, with the aim of encouraging clients to book dental treatments online. Potential clients can review available times and dates and proceed with booking their desired treatment.
To access the booking platform, the customer will be prompted to log in or register first. Upon registration, the customer will be able to book treatments, cancel existing bookings, and amend their personal details provided during registration. The administrator will have the option to create, amend, and delete appointment listings as well as manage the offered treatments, which are also referred to as services interchangeably. The system includes several features to prevent typical errors. For example, a warning message will appear if a client selects a timeslot in the past. Timeslots that have already been booked are grayed out and not accessible. Additionally, confirmation emails are sent to notify clients of appointment changes, such as cancellations, and verification emails.


* Link to the hosted project: **[Infinita Perfectio Booking Platform](https://ip-appointments-94bebae716d1.herokuapp.com)**


## Features

1. **Navigation Bar**  
The navigation bar appears on all pages, with different links displayed depending on the page and the user. It allows users to easily navigate between pages across all devices without the need to use the browser's 'back' button to return to the previous page.
The navigation bar includes various links depending on the page and user:
To the Home Page, Login, and Register for users who do not have their account yet.
To the Home Page, My Appointments, My Details, and Logout for signed-in users.
To the Home Page, Dental Services, and Logout for the administrator, also called superuser in the context of this web app.  

* Default navigation bar:

![navbar1](static/documentation/images/navbar1.png)

* When patient logged in

![navbar2](static/documentation/images/navbar2.png)

* When administrator logged in:
  
![navbar2](static/documentation/images/navbar3.png)

* On mobile devices:

<p align="center"><img src="static/documentation/images/navbar-mobile.png" alt="navbar-mobile"></p>

1. **The Footer**  
The footer bar appears on all pages, allowing user to easily access the clinic's Facebook page, make a phone call through WhatsApp, or view the opening hours.

![footer](static/documentation/images/footer.png)

3. **Calendar Page (The Landing Page)**  
The landing page displays the navigation bar, the footer, and the calendar with available dates and times. Timeslots highlighted in grey are already booked and therefore not available. The user has the option to switch between different dates and weeks using the arrow buttons and can return to the current week by clicking the return (go to current week) button. The customer is prompted to log in or register to access the booking option.
The navigation bar includes links to the Home Page, Login, and Register.

![calendar](static/documentation/images/calendar-landing.png)

* Calendar's navigation buttons:
![cal-nav](static/documentation/images/calendar-navigation.png)

4. **Registration Page**  
The sign-up form is displayed. A reminder to sign in for clients who are already registered is shown at the top of the form. Fields highlighted with an asterisk are mandatory, and a warning will appear if they are left blank. There is additional information regarding password requirements at the bottom of the form. Once all fields are completed correctly and the "Sign Up" box is ticked, the system will send an account verification email to the address provided by the customer. To access the account, the customer must confirm the email.  
The navigation bar includes links to the Home Page, Login, and Register.

![registration](static/documentation/images/registration-page.png)

* Verification Email:

![email1](static/documentation/images/email1.png)

5. **Login Page**  
Upon opening, a sign-in form is displayed. The customer or administrator is required to provide their username and password to sign in. An error message will be displayed if an incorrect username or password is entered. Upon signing in, a small green confirmation box will appear in the bottom right corner, confirming successful sign-in. Additionally, there is an option to click the "Remember Me" box for future sign-ins , a link to open the Registration page and password recovery functionality.
The navigation bar includes links to the Home Page, Login, and Register.

![login](static/documentation/images/login.png)

* Password reset functionality:

![passwd-reset](static/documentation/images/pass-reset.png)

6. **Customer Login**  
**Landing Page** – The calendar, showing available dates and timeslots, is displayed. The customer's username is also shown in the navigation bar for confirmation. The current day is highlighted in yellow, and unavailable slots are greyed out. A warning message will appear if a time slot selected is in the past.
The customer can navigate through dates using the arrow buttons. Upon clicking on a desired timeslot, a popup window will appear confirming the date and time, along with a dropdown list of available services, also referred to as treatments. Once the customer confirms the booking, a small green box with an acknowledgment will appear in the bottom right corner of the page.  

![appointment](static/documentation/images/appointment.png)

**My Details** – Upon clicking the "My Details" link, the customer can view and edit their details saved in the system. Once an update is saved, an acknowledgment box will appear on the screen.  

![my-details](static/documentation/images/my-details.png)

**My Appointments** – This page displays all the details of appointments booked by the customer. Each appointment can be deleted by clicking the "Delete" button next to the appointment details. A warning message will appear on the screen asking the client to confirm the cancellation. Upon confirmation, an acknowledgment box will appear on the screen.   

![my-appointments1](static/documentation/images/my-aapointments1.png)

**Logout** – Upon clicking the "Logout" link, a sign-out window will appear, and the client will be prompted to confirm if they wish to log out.  

**Home Page** – Upon clicking the logo, the client will be redirected to the landing page.

![alt text](static/documentation/images/logo.png)

7. **Administrator Login**  
**Landing Page** – Upon logging in, the landing page with the calendar is displayed. The administrator’s username is also shown in the navigation bar.  
The navigation bar includes the following links:  
**Dental Services** page – This page offers CRUD functionality, allowing the administrator to view, add, amend, and delete treatments (services) available in the calendar. All changes made by the administrator are implemented immediately and reflected in the calendar.  
**Logout** – Upon clicking the "Logout" link, a sign-out window will appear, and the administrator will be prompted to confirm if they wish to log out.

![home-admin](static/documentation/images/home-page-admin.png)

8. **Email**  
Email Confirmation Functionality – The platform also features email confirmation, ensuring key actions, such as account verification, reservations, and updates to those reservations.

![email-verified](static/documentation/images/email-verified.png)

9. **Push notifications**  
The platform uses Bootstrap Toasts for push notifications, offering a modern and effective method to deliver real-time updates to users. These notifications are displayed as compact, dismissible pop-ups, in the bottom-right corner of the screen, ensuring they are noticeable while remaining unobtrusive to the user’s workflow.  

<p align="center"><img src="static/documentation/images/toast.jpeg" alt="toast"></p>