from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import Thread
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
@method_decorator(login_required, name="dispatch")
class ThreadList(TemplateView):
    template_name = "messenger/thread_list.html"


@method_decorator(login_required, name="dispatch")
class ThreadDetail(DetailView):
    model = Thread

    def get_object(self):
        obj = super(ThreadDetail, self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404()
        return obj

#Recuperamos el contenido apartir del request.GET y con otro get que tienen los diccinarios
#If content si hay algun contenido y probaremos de recuperar el hilo
#FirstTrue es si hay 1 mensaje en la conversacion
def add_message(request, pk):
    json_response = {'created':False}
    if request.user.is_autheticated:
        content = request.GET.get('content', None)
        if content:
            thread = get_object_or_404(Thread, pk=pk)
            message= message.object.created(user=request.user, content=content)
            thread.message.add(message)
            json_response['created'] = True
            if len(thread.message.all()) is 1:
                json_response['first'] = True

    else:
        raise Http404("User is not authenticated") 
    return JsonResponse(json_response)
@login_required
def start_thread(request, username):
    user = get_object_or_404(user, username=username)
    thread = thread.object.fin.or_create(user, request.user)
    return redirect(reverse_lazy('messenger:detail', args=[thread.pk]))

