from django.shortcuts import render
from newsfeed.models import Newsfeed
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError
from django.views.generic import TemplateView
from newsfeed.models import Newsfeed


# Create your views here.
class IndexView(TemplateView):
    template_name = 'core/index.html'
    def render_to_response(self, context, **kwargs):
        context['can_create'] = self.request.user.has_perm('newsfeed.add_newsfeed')
        context['news'] = Newsfeed.objects.all()
        kwargs.setdefault('content_type', self.content_type)
        return self.response_class(request=self.request,template=self.get_template_names(),context = context,using=self.template_engine,**kwargs)

def home(request):
    news = Newsfeed.objects.all()
    return render(request, 'core/index.html', {'news':news})
def handler404(request, exception, template="core/error.html"):
    return render(request, template, {'error':'Creo que lo que buscas no está.'})
def handler403(request, exception, template="core/error.html"):
    return render(request, template, {'error':'Parece que necesitas poderes.'})
def handler500(request, exception, template="core/error.html"):
    return render(request, template, {'error':'Parece que el servidor explotó.'})
def about(request):
    return render(request, 'core/about.html')
def apiabout(request):
    return render(request, 'core/api.html')