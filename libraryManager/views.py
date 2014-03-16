# Create your views here.
from django.shortcuts import render
from oauth2_provider.views.generic import ProtectedResourceView
from django.http.response import HttpResponse

def index(request):
    context = {
        'index_view': "Job Index View",
        'index_hello': "Hello World!",
        'index_user': "Wilson",
    }
    return render(request, 'libraryManager/index.html', context)

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')