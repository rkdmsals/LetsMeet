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
    text = "new test"
    myToken = "xoxb-4018156897472-4018178014048-AqC17N7a1Zf8deS77MZs5tEl"

    post_message(myToken, "#admin", text)
    return redirect('sociallogin:register_finish')

