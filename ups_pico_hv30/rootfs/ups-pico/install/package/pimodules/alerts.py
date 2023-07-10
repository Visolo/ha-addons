
import smtplib
import subprocess
import datetime
import jinja2
import base64
from email.mime.text import MIMEText


def get_host_name():
    try:
        command = "uname -n"
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]
        return output
    except:
        return None


def get_ip_address():
    try:
        #command = "hostname -I"
        command = "hostname -i"
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]
        return output
    except:
        return None


def sendEmail(emailserver, username, port, security, fromAddr, toAddr, b64Password, msgSubjectTemplate, msgBodyTemplate, identifyingName):
    try:
        port = int(port)
    except ValueError:
        port = 0

    try:
        now = datetime.datetime.now()
        now_format = now.strftime("%Y-%m-%d %H:%M:%S")
        host = get_host_name().decode('utf-8')
        name = identifyingName
        ipaddress = get_ip_address()
    except:
        raise

    #password = base64.b64decode(b64Password).decode('utf-8')
    password = b64Password

    tVars = {'now': now_format, 'host': host, 'ipaddress': ipaddress, 'name': name}

    try:
        #templateLoader = jinja2.FileSystemLoader(searchpath="/")
        templateLoader = jinja2.FileSystemLoader(searchpath="/config/ups_pico_hv30/")
        templateEnv = jinja2.Environment(loader=templateLoader)

        subjectTemplate = templateEnv.get_template(msgSubjectTemplate)
        bodyTemplate = templateEnv.get_template(msgBodyTemplate)

        msgSubject = subjectTemplate.render(tVars)
        msgBody = bodyTemplate.render(tVars)

    except:
        raise

    # Writing the message
    msg = MIMEText(msgBody)
    msg['Subject'] = msgSubject
    msg['From'] = fromAddr
    msg['To'] = toAddr

    # Sending the message
    try:
        if port:
            serverstring = format("%s:%d" % (emailserver, port))
        else:
            serverstring = emailserver

        if security.lower() in ['ssl']:
            server = smtplib.SMTP_SSL(serverstring)
        else:
            server = smtplib.SMTP(serverstring)
            server.starttls()

        server.login(username, password)
        server.sendmail(fromAddr, [toAddr], msg.as_string())
        server.quit()
    except:
        raise

    return True
