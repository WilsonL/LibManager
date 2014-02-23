# Create your views here.
from django.shortcuts import render


def index(request):
    context = {
        'index_view': "Job Index View",
        'index_hello': "Hello World!",
        'index_user': "Wilson",
    }
    return render(request, 'libraryManager/index.html', context)