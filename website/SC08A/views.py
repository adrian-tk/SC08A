from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Motor
from django.views import generic
from .scripts import send_socket

class MotorsView(generic.ListView):
    model=Motor
    template_name = 'SC08A/motoindex.html'

class MotorDetail(generic.DetailView):
    model=Motor
    template_name = 'SC08A/moto.html'

class SetVal(generic.TemplateView):
    template_name='SC08A/setview.html'
    def get(self, request, *args, **kwargs):
        #val=request.GET.items()
        keys = list(request.GET)
        send_socket.send_to_socket("kanał" + keys[0])
        send_socket.send_to_socket(request.GET[keys[0]])
        val=request.GET.keys()
        return HttpResponse(val)

class UpdateName(generic.DetailView):
    model=Motor

def update_name(request, moto_id):
    motor=get_object_or_404(Motor, pk=moto_id)
    motor.motor_name=request.POST['new_name']
    motor.save()
    return HttpResponseRedirect(reverse('SC08A:motors'))

def update_channel(request, moto_id):
    motor=get_object_or_404(Motor, pk=moto_id)
    motor.channel_no=request.POST['new_channel']
    motor.save()
    return HttpResponseRedirect(reverse('SC08A:motors'))

def delete_motor(request, moto_id):
    motor=get_object_or_404(Motor, pk=moto_id)
    motor.delete()
    return HttpResponseRedirect(reverse('SC08A:motors'))

def add_motor(request):
    motor=Motor()
    motor.save()
    motors_list=Motor.objects.all()
    context = {'motors_list': motors_list}
    return HttpResponseRedirect(reverse('SC08A:motors'))
