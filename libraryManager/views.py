# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
    template = loader.get_template('libraryManager/index.html')
    context = RequestContext(request, {
        'index_view': "Job Index View",
        'index_hello': "Hello World!",
    })
    return HttpResponse(template.render(context))