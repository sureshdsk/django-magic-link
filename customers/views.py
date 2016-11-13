from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from sesame import utils
from django.core.mail import send_mail


def login_page(request):
    if request.method == "POST":
        email = request.POST.get("emailId")
        user = User.objects.get(email=email)
        login_token = utils.get_query_string(user)
        login_link = "http://127.0.0.1:8000/customers/{}".format(login_token)

        html_message = """
        <p>Hi there,</p>
        <p>Here is your <a href="{}">magic link</a> </p>
        <p>Thanks,</p>
        <p>Django Admin</p>
        """.format(login_link)

        send_mail(
            'Django Magic Link',
            html_message,
            'wishlist@kissflow.com',
            [email],
            fail_silently=False,
            html_message = html_message
        )
        return render(request, "login.html", context={"message":"Please check your email for magic link."})

    return render(request, "login.html")

@login_required
def customers_home_page(request):
    return render(request, "customers/index.html")