from django.http import JsonResponse
from django.core import serializers
from .models import Choice

def get_available_choices(request):
    data = serializers.serialize('json', Choice.objects.all(),
      fields=('id', 'title'))
#    return JsonResponse(data)
    return JsonResponse({'choices': data})
