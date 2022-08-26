import requests


def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={"Authorization": "Bearer " + token},
                             data={"channel": channel, "text": text}
                             )
    print(response)


myToken = "xoxb-4018156897472-4018178014048-YEAKogIWmpg612S7aXxE0ksY"

post_message(myToken, "#admin", "lucykorea님이 우지만에 가입했습니다.")