from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Newsfeed
from django.contrib.auth.decorators import permission_required, login_required
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import NewsfeedForm
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from .serializers import NewsfeedSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView

class UpdateRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm("newsfeed.change_newsfeed"):
            raise PermissionDenied
        return super(UpdateRequiredMixin, self).dispatch(request, *args, **kwargs)

class CreateRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm("newsfeed.add_newsfeed"):
            raise PermissionDenied
        return super(CreateRequiredMixin, self).dispatch(request, *args, **kwargs)

class DeleteRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm("newsfeed.delete_newsfeed"):
            raise PermissionDenied
        return super(DeleteRequiredMixin, self).dispatch(request, *args, **kwargs)

class NewsfeedDetailView(DetailView):
    model = Newsfeed
    def render_to_response(self, context, **kwargs):
        context['can_edit'] = self.request.user.has_perm('newsfeed.change_newsfeed')
        context['can_delete'] = self.request.user.has_perm('newsfeed.delete_newsfeed')
        context['can_create'] = self.request.user.has_perm('newsfeed.add_newsfeed')
        kwargs.setdefault('content_type', self.content_type)
        return self.response_class(request=self.request,template=self.get_template_names(),context = context,using=self.template_engine,**kwargs)

class NewsfeedCreateView(CreateRequiredMixin, CreateView):
    model = Newsfeed
    form_class = NewsfeedForm
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form1 = form.save(commit=False)
        form1.author = self.request.user
        form1.save()
        return super(NewsfeedCreateView, self).form_valid(form)

class NewsfeedUpdateView(UpdateRequiredMixin, UpdateView):
    model = Newsfeed
    fields = ['title', 'content', 'image']
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('newsfeed', args=[self.object.id, self.object.title.replace(" ","-")])

class NewsfeedDeleteView(DeleteRequiredMixin, DeleteView):
    model = Newsfeed
    success_url = reverse_lazy('home')

class NewsfeedApiView(ListAPIView):
    queryset = Newsfeed.objects.all()
    serializer_class = NewsfeedSerializer
class NewsfeedApiDelete(DeleteRequiredMixin , DestroyAPIView):
    queryset = Newsfeed.objects.all()
    serializer_class = NewsfeedSerializer
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj
class NewsfeedApiCreate(CreateRequiredMixin, CreateAPIView):
    serializer_class = NewsfeedSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
class NewsfeedApiUpdate(UpdateRequiredMixin ,UpdateAPIView):
    queryset = Newsfeed.objects.all()
    serializer_class = NewsfeedSerializer
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj