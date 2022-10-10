from django.shortcuts import render


def index(request):
    return render(request, 'collections.html')

def detailed_collection(request):
    return render(request, 'detailed_collection.html')
