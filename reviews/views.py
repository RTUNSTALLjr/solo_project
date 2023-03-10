from django.shortcuts import render

def index(request):
    return render(request, 'reviews/dashboard.html')

def media(request):
    return render(request, 'reviews/media.html')

def all(request):
    return render(request,'reviews/all_reviews.html')

def one(request):
    return render(request, 'reviews/one_review.html')