from django.shortcuts import render

# Create your views here.


def sayHI(req):
    return render(req, "account/index.html")

