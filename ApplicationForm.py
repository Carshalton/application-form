import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Function to send email
def send_email(name, application, reason, timestamp):
    try:
        # Email configuration
        sender_email = "ethangeng2001@gmail.com"
        receiver_email = "Geng-E-27@kcs.org.uk"
        app_password = "vqhn agoo xgfc nupj"  # Your app password

        # Create the email content
        subject = f"Application from {name}"
        body = f"""
        Full Name: {name}
        Application: {application}
        Reason: {reason}
        Submitted on: {timestamp}
        """

        # Set up the MIME
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to Gmail's SMTP server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())

        st.success("Your application has been submitted successfully!")

    except Exception as e:
        st.error(f"An error occurred while sending the email: {e}")

# Streamlit UI
st.title("Application Form")

with st.form(key='application_form'):
    full_name = st.text_input("Full Name:")
    application = st.text_input("What would you like to apply for?")
    reason = st.text_area("Why?", height=200)
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        if full_name and application and reason:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            send_email(full_name, application, reason, timestamp)
        else:
            st.warning("Please fill in all fields.")
