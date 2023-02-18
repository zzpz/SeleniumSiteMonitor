## https://www.reddit.com/r/streetwear/comments/5er27n/python_tutorial_restock_release_monitor_notifier/?st=ivxbcaly&sh=f853a5a1

import random
import time
import requests
import os

# import smtplib
import json
from timeit import default_timer as timer
from dotenv import load_dotenv

load_dotenv()
JSON_FILE = "WebsiteStates.json"
url_param = os.environ["ENV_URL_2"]
start = timer()

delay = random.randint(3, 16) + random.random()


def send_email(user, pwd, recipient, subject, body):
    pass
    # """INPUT: gmail username, gmail password, a list of recipients, a subject, and a body"""
    # gmail_user 	= user
    # gmail_pwd 	= pwd
    # FROM 		= user
    # TO 			= recipient if type(recipient) is list else [recipient]
    # SUBJECT 	= subject
    # TEXT 		= body

    # # prepare actual message
    # message = "From: {}\nTo: {}\nSubject: {}\n\n{}".format(FROM, ", ".join(TO), SUBJECT, TEXT)
    # try:
    # 	server = smtplib.SMTP("smtp.gmail.com", 587) # start Simple Mail Transfer Protocol server on port 587
    # 	server.ehlo() # establish connection
    # 	server.starttls() # put communication in Transport Layer Security mode, encrypting all data
    # 	server.ehlo() # second time
    # 	server.login(gmail_user, gmail_pwd)
    # 	server.sendmail(FROM, TO, message)
    # 	server.quit()
    # 	print("Mail sent")
    # except Exception as e:
    # 	print("failed to send mail, " + str(e))


def main():

    # with statement closes the request session automatically
    with requests.Session() as s:
        url = url_param
        time_between_checks = delay  # seconds
        user = ""
        pwd = ""
        recipient = ""
        subject = "SITE UPDATED"
        body = "CHANGE AT " + str(url)

        page1 = s.get(url)  # "old page" that will be compared against

        time.sleep(time_between_checks)  # pause execution

        page2 = s.get(url)  # "new page" that will be compared against "old page"

        end = timer()

        if page1.content == page2.content:
            print("[-] No change detected @ " + str(url))
        else:
            print("[+] Change detected @ " + str(url))

            with open(JSON_FILE, "w") as savefile:
                json.dump([page1, page2], savefile, indent=4, separators=(",", ":"))

            send_email(user, pwd, recipient, subject, body)

        print("Elapsed time: " + str((end - start) / 60) + " minutes")

        page2 = None

        main()  # continues looping forever


if __name__ == "__main__":
    main()
