#sending email using python
import smtplib
s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
sender='sagakshathriyan@gmail.com'
receiver='sagarsrt105@gmail.com'
msg="hello"
s.login(sender,'7795300140')
s.sendmail(sender,receiver,msg)
print("msg sent successfully")		
s.quit()