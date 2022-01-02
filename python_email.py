import smtplib as s
ob = s.SMTP("smtp.gmail.com", 587)

ob.starttls()

ob.login("mdsahil0170@gmail.com", "sahil2021")

subject = "Sending email using python"

body = "This is tutorial of sending email using python script in simple setting."

message = "Subject:{}\n\n{}".format(subject, body)

# print(message)

listofAddress = ["dotcode0170@gmail.com"]

ob.sendmail("mdsahil0170", listofAddress, message)


print("Send successfully...")
ob.quit()
