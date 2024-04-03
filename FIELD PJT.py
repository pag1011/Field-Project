import random
import smtplib
otp=''.join([str(random.randint(0,9)) for i in range(4)])

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('prachiagrawal0810@gmail.com',password)
msg='Hello, Your OTP is '+str(otp)
server.sendmail('prachiagrawal0810@gmail.com','fieldproject55@gmail.com',msg)
server.quit()
