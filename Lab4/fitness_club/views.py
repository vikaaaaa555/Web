import random
import requests
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import *

MEM1 = 0
MEM2 = 0
MEM3 = 0

class FitnessClubHome(ListView):
    model = Group
    template_name = 'fitness_club/index.html'
    context_object_name = 'groups'
    ordering = ('name',)

class MembershipView(ListView):
    model = Membership
    template_name = 'fitness_club/gym_membership.html'
    context_object_name = 'memberships'

class InstructorsView(ListView):
    model = Instructor
    template_name = 'fitness_club/instructors.html'
    context_object_name = 'instructor'
    ordering = ('name',)

def services(request):
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    image_url = response.json()['message']

    response = requests.get('https://cat-fact.herokuapp.com/facts')
    facts = response.json()
    random_fact = random.choice(facts)

    context = {
        'image_url': image_url,
        'random_fact': random_fact
    }
    return render(request, 'fitness_club/services.html',  context)

# class ShoppingCardView(DetailView):
#     model = Membership
#     template_name = 'fitness_club/shopping_cart.html'
#     pk_url_kwarg = 'membership_id'
#     context_object_name = 'pushcase'
#
#
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['memberships'] = Membership.objects.order_by('name')
#         return context

def shopping_cart(request, membership_id):
    memberships = Membership.objects.all()
    pushcase = Membership.objects.get(pk=membership_id)
    # for el in memberships:
    #     if el.name == pushcase.name:
    #         el.count += 1
    #         el.save()
    #         pushcase.save()

    context = {
        'memberships':memberships,
        'pushcase': pushcase
    }
    return render(request, 'fitness_club/shopping_cart.html', context)

def home(request):
    return render(request, 'fitness_club/home.html')

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def admin_view(request):
    return render(request, 'admin.html')

