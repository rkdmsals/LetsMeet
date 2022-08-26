# import requests


# def post_message(token, channel, text):
#     response = requests.post("https://slack.com/api/chat.postMessage",
#                              headers={"Authorization": "Bearer " + token},
#                              data={"channel": channel, "text": text}
#                              )
#     print(response)


# myToken = "xoxb-4018156897472-4018178014048-YEAKogIWmpg612S7aXxE0ksY"

# post_message(myToken, "#admin", "lucykorea님이 우지만에 가입했습니다.")

import requests


def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={"Authorization": "Bearer " + token},
                             data={"channel": channel, "text": text}
                             )
    print(response)


# myToken = "xoxb-4018156897472-4018178014048-Sa13o0yf7f6OpA6rK6zVFvCy"

# post_message(myToken, "#admin", "사용자가 새로운 모임.")



# from slacker import Slacker

# def slack_notify(text=None, channel='#admin'):
#     token = "xoxb-4018156897472-4018178014048-Sa13o0yf7f6OpA6rK6zVFvCy" #토근값은 공개저장소에 공개되지 않도록 주의
#     slack = Slacker(token)
#     slack.chat.post_message(text=text, channel=channel)