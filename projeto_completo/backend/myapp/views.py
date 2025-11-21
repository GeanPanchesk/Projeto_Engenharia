from django.http import HttpResponse

def home(request):
    return HttpResponse("Backend Django rodando!")