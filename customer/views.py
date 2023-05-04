from django.shortcuts import render

# Create your views here.
def baab (request):
    return render(request, 'customer/index.html')