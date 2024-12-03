from django.conf import settings
from django.core.mail import send_mail

def send_account_activation_email(email, email_token):
    subject = "Your account need to be varified"
    email_from = settings.EMAIL_HOST_USER
    messege = f"Hii, click on the link to activate your account http://127.0.0.1:8000/accounts/activate/{email_token} "
    send_mail(subject,messege,email_from,[email])


def send_ticket_booking_email(username, movie, theater, address, date, number_of_tickets, total_price,email):
    subject = f"Ticket Confirmed for {movie}"
    email_from = settings.EMAIL_HOST_USER
    message = f"""
    Dear {username},

    We are excited to confirm your movie ticket booking! Here are the details of your reservation:

    Movie Name: {movie}
    Theater Name: {theater}
    Theater Address: {address}
    Date & Time: {date}
    Number of Tickets: {number_of_tickets}
    Total Price:  ₹ {total_price}

    Please make sure to arrive at least 15 minutes before the showtime to ensure a smooth experience.

    If you have any questions or need assistance, feel free to reach out to us.

    Enjoy the movie, and have a great time!

    (  ABEEE CHALE MAT JANA NAKLI  TICKET HAI YAAD HAI PESE NHI DIYE )
    """

    send_mail(subject=subject,message=message,from_email=email_from,recipient_list=[email])
