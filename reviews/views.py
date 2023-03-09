from django.shortcuts import render

def index(request):
    return render(request, 'dashboard.html')

def media(request):
    return render(request, 'media.html')

def all(request):
    return render(request,'all_reviews.html')

def one(request):
    return render(request, 'one_review.html')