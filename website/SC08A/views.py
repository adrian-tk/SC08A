from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Question
from .models import Motor
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'SC08A/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

# Create your views here.
class DetailView(generic.DetailView):
    model=Question
    template_name = 'SC08A/detail.html'

class ResultsView(generic.DetailView):
    model=Question
    template_name = 'SC08A/results.html'

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

class MotorsView(generic.ListView):
    model=Motor
    template_name = 'SC08A/motoindex.html'

def motor(request, moto_id):
    motor = get_object_or_404(Motor, pk=moto_id)
    context = {'motor': motor}
    return render(request, 'SC08A/moto.html', context)
    #return HttpResponse("Here, You will see  servodrive nr. %s" % moto_id)

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
