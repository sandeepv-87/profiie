from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    # return HttpResponse("this is my home page")
    return render(request, 'home.html')


def projects(request):
    # return HttpResponse("this is my website")
    return render(request, 'project.html')


def achievements(request):
    # return HttpResponse("this is my staff")
    return render(request, 'achievements.html')


def contact(request):
    # return HttpResponse("this is my about")
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST[
            'number']
        desc = request.POST['text']
        print(name,email,number,desc)
        lns = Contact(name=name,email=email,phone=number,desc=desc)
        lns.save()
        print("ok")
    return render(request, "contact.html")
