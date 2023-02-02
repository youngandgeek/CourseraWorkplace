from django.http import HttpResponse,HttpResponseBadRequest

def handler404(request,exception):
    return HttpResponse ("404 Page Not Found !")
    