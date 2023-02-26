from django.shortcuts import render



def home(request):
    context = {

    }
    return render(request, "posts/home.html", context)

def about(request):
    context = {}
    return render(request, "posts/about.html", context)

def contact(request):
    context = {}
    return render(request, "posts/contact.html", context)

