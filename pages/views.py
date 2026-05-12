from django.shortcuts import render

def index(request):
    return render(request,"pages/index.html")
# Create your views here.
def about(request):
    return render(request,"pages/about.html")