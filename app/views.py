from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def index(request):
    if request.method == 'POST':

        return JsonResponse({
            'status': 'success',
            'message': 'We will send the result as CSV file to your email.'
        })

    return render(request, 'home/index.html')