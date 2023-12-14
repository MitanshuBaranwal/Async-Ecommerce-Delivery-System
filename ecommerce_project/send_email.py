import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_order_status_email(receiver, orderid, order,quantity, username, status, companyname):
    print(receiver, orderid, order, quantity, username, status, companyname)

    # Set up the email message
    msg = MIMEMultipart()
    msg['From'] = 'emailer_example@gmail.com'
    msg['To'] = receiver
    msg['Subject'] = f"{order} Order Status - {companyname}"

    # Customize the email body with HTML formatting
    body = f"""
        <html>
            <body>
                <p>Hi {username},</p>
                <p>We hope this email finds you well. Your recent order <strong><span style="color: green;">{order}</span></strong> with the order number <strong><span style="color: green;">{orderid}</span></strong> and order quantity <strong><span style="color: green;">{quantity}</span></strong> is now <strong><span style="color: green;">{status}</span></strong>.</p>
                <p>If you have any questions or need further assistance, please don't hesitate to reach out.</p>
                <p>Thank you for choosing us.</p>
                <p>Happy Shopping!</p>
                <p>Best regards,<br>The {companyname} Team</p>
            </body>
        </html>
    """

    msg.attach(MIMEText(body, 'html'))

    # Set up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login to your Gmail account with App Password
    # Go to https://myaccount.google.com/security and generate an app password
    server.login('emailer_example@gmail.com', 'app_password')

    # Send the email
    text = msg.as_string()
    server.sendmail('emailer_example@gmail.com', receiver, text)

    # Close the connection to the SMTP server
    server.quit()

    return 'done'

if __name__ == "__main__":
    # Example usage
    email = "user_example@gmail.com"
    username = "user_name"
    orderid = 82892
    quantity = 7
    order = "Laptop Bag"
    status = "Delivered"
    companyname = "ShopVista"
    send_order_status_email(email, orderid, order, quantity, username, status, companyname)
