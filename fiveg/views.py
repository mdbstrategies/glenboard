from django.shortcuts import render


def home(request):
    return render(request, template_name="fiveg/home.html")


def about(request):
    return render(request, template_name="fiveg/about.html")
