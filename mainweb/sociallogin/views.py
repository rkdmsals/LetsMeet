from django.shortcuts import render, redirect
from django.contrib.auth import logout

def sociallogin(request):
    return render(request, 'sociallogin/sociallogin.html')


def logout_view(request):
    logout(request)
    return render(request, 'sociallogin/logout.html')

def register_view(request):
    return render(request, 'sociallogin/register1.html')

def register_finish_view(request):
    return render(request, 'sociallogin/register_complete.html')


# from slack import slack_notify
from django.views.decorators.http import require_GET, require_POST

# @require_POST
# def register_save(request):
#     # isbn = request.POST['isbn']
#     # message, book = register_book(isbn)
#     # messages.info(request, message)
#     # if book:
#     #     # slack_message = "*[신규회원]* {}".format(book.title)
#     #     slack_message = "*[신규회원]*"
#     #     slack_notify(slack_message)
    
#     slack_message = "*[신규회원]*"
#     slack_notify(slack_message)
#     return redirect('sociallogin:register_finish')




from .slack import post_message

@require_GET
def send_slack(request):
    text = "현장 미션 완료!! ^^"
    myToken = "xoxb-4018156897472-4018178014048-AqC17N7a1Zf8deS77MZs5tEl"

    post_message(myToken, "#admin", text)
    return redirect('sociallogin:register_finish')



from .screenshot import get_service,create_message_with_attachment, send_message

@require_GET
def pic_email(request):
    service = get_service()
    user_id = 'me'
    msg = create_message_with_attachment('lucykorea@gmail.com', 'lucykorea@gmail.com', '현장미션 완료!!','This is the message body', saveas)
    send_message(service, user_id, msg)

    return redirect('sociallogin:email_finish')


def email_finish_view(request):
    return render(request, 'sociallogin/email_complete.html')