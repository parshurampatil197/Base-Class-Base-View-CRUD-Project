from django.shortcuts import render
from .forms import StudentRegForm
from .models import User
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView, RedirectView
from django.views import View


# this class will add new items and show all items
class UserAddShowView(TemplateView):
    template_name = 'enroll/addandshow.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentRegForm()
        stud = User.objects.all()
        context = {'form': fm, 'stu': stud}
        return context

    def post(self, request):
        fm = StudentRegForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('')


# this class will delete items
class UserDeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)


# this class will update items
class UserUpdateView(View):
    def get(self, request, id):
        pi = User.objects.get(pk=id)
        fm = StudentRegForm(instance=pi)
        return render(request, 'enroll/updatestu.html', {'form': fm})

    def post(self, request, id):
        pi = User.objects.get(pk=id)
        fm = StudentRegForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')

    