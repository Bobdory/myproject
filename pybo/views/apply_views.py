from flask import Blueprint, render_template, request
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import datetime
from os.path import basename

bp = Blueprint('apply', __name__, url_prefix='/apply')

gmail_account_id = "k2hmal2@gmail.com"  # Gmail계정ID
gmail_account_pass = "mmzuisiuvofaphqf"  # Gmail계정의앱비밀번호16자리


@bp.route('/apply/', methods=('GET', 'POST'))
def make():
    return render_template('apply/apply_make.html')

@bp.route('/sendMail/', methods=('GET', 'POST'))
def applySendMail():
    if request.method == 'POST':
        to_mail = "k2hmal@naver.com"
        from_mail = "k2hmal2@gmail.com"
        subject = "체력단련비 신청서"
        massage = """
            <html>
            <body>
                <h2>{title}</h2>
                <p>체력단련비 신청 내역 입니다.</p>
            </body>
            </html>
        """.format(
            title='체력단련비 신청서'
        )
        sendMultiMessage(to_mail, from_mail, subject, massage,
                         'C:/projects/myproject/pybo/templates/apply/apply_make.html')

        return render_template('apply/apply_make.html')


def sendMultiMessage(to_email, from_email, subject, message, filepath):
    try:
        print("【Message와File의Email송신시작】：" + str(datetime.datetime.now()))

        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["To"] = to_email
        msg["From"] = from_email
        msg.attach(MIMEText(message, 'html'))

        # 파일첨부
        with open(filepath, "rb") as f:
            part = MIMEApplication(
                f.read(),
                Name=basename(filepath)
            )

        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(filepath)
        msg.attach(part)

        # 메일송신처리
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(gmail_account_id, gmail_account_pass)
        server.send_message(msg)
        server.quit()

    except Exception as e:
        errordate = str(datetime.datetime.now())

        print("【=== 에러내용 ===】：" + errordate)
        print("type:" + str(type(e)))
        print("args:" + str(e.args))
        print("e자신:" + str(e))

    else:
        print("【정상적으로 Message와File의Email송신이 완료됬습니다.】：" + str(datetime.datetime.now()))
    finally:
        print("【Message와File의Email송신완료】：" + str(datetime.datetime.now()))


def sendMessage(to_email, from_email, subject, message):
    try:
        print("【MessageEmail송신시작】：" + str(datetime.datetime.now()))

        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["To"] = to_email
        msg["From"] = from_email

        msg.attach(MIMEText(message, 'html'))

        # 메일송신처리
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(gmail_account_id, gmail_account_pass)
        server.send_message(msg)
        server.quit()

    except Exception as e:
        errordate = str(datetime.datetime.now())

        print("【=== 에러내용 ===】：" + errordate)
        print("type:" + str(type(e)))
        print("args:" + str(e.args))
        print("e자신:" + str(e))

    else:
        print("【정상적으로 Message의Email송신이 완료됬습니다.】：" + str(datetime.datetime.now()))
    finally:
        print("【Message의Email송신완료】：" + str(datetime.datetime.now()))