from django.http import HttpResponse, JsonResponse
from django.urls import reverse

def check_login(request):
    if (request.user and request.user.is_authenticated):
        return JsonResponse({
             'is_authenticated': True,
             'username': request.user.username,
             'logout_url': reverse('rest_framework:logout')
            })
    return JsonResponse({
         'is_authenticated': False,
         'login_url': reverse('rest_framework:login')
        })
