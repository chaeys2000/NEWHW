from django.shortcuts import render

# Create your views here.
def page(request):
    return render(request, 'page.html')
def project(request):
    return render(request, 'project.html')
