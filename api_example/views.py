from django.http import JsonResponse

def names(request):
    return JsonResponse({'names': ['William', 'Rod', 'Grant']})

def remoteip(request):
    return JsonResponse({'remote_addr': request.META.get('REMOTE_ADDR')})
