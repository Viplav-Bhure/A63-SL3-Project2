from django.shortcuts import render

def page(request):
    return render(request, 'app2/page.html')
