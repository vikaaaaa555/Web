import random
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .forms import FeedbackForm
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


def luck(request):
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    image_url = response.json()['message']

    # response = requests.get('https://cat-fact.herokuapp.com/facts')
    # facts = response.json()
    # random_fact = random.choice(facts)

    context = {
        'image_url': image_url,
        #'random_fact': random_fact
    }
    return render(request, 'fitness_club/luck.html', context)


# class ShoppingCardView(DetailView):
#     model = Membership
#     template_name = 'fitness_club/shopping_cart.html'
#     pk_url_kwarg = 'membership_id'
#     context_object_name = 'pushcase'
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
        'memberships': memberships,
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


class Inform(ListView):
    model = News
    template_name = 'fitness_club/inform.html'
    context_object_name = 'inform'

    def get_queryset(self):
        return News.objects.all()


def about_us(request):
    return render(request, 'fitness_club/about_us.html')


def news(request):
    return render(request, 'fitness_club/news.html')


def privacy_politic(request):
    return render(request, 'fitness_club/privacy_politic.html')


class CouponsView(ListView):
    model = Coupon
    template_name = 'fitness_club/coupon.html'
    context_object_name = 'coupon'

    def get_queryset(self):
        return Coupon.objects.all()


class NewsView(ListView):
    model = News
    template_name = 'fitness_club/news.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.all()


class VocationView(ListView):
    model = Vocation
    template_name = 'fitness_club/vocation.html'
    context_object_name = 'vocation'

    def get_queryset(self):
        return Vocation.objects.all()


class FeedbackForm(CreateView):
    form_class = FeedbackForm
    template_name = 'fitness_club/feedback_form.html'
    success_url = reverse_lazy('feedback_view')
    login_url = reverse_lazy('signup')
    raise_exception = True

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


class FeedbackView(ListView):
    model = Feedback
    template_name = 'fitness_club/feedback_view.html'

    def get_queryset(self):
        return Feedback.objects.all()


class FAQView(ListView):
    model = Coupon
    template_name = 'fitness_club/faq.html'
    context_object_name = 'faq'

    def get_queryset(self):
        return FAQ.objects.all()


def news_view(request, news_id):
    news = News.objects.all()
    pushcase = News.objects.get(pk=news_id)

    context = {
        'news': news,
        'pushcase': pushcase
    }
    return render(request, 'fitness_club/news_view.html', context)


def certificate(request):
    return render(request, 'fitness_club/certificate.html')


def scroll(request):
    return render(request, 'fitness_club/js/scroll.html')


def autoplay(request):
    return render(request, 'fitness_club/js/autoplay.html')


def array(request):
    return render(request, 'fitness_club/js/associative_array.html')


def interactive(request):
    return render(request, 'fitness_club/js/interactive_table.html')


def calculate(request):
    return render(request, 'fitness_club/js/calculator.html')


def text_change(request):
    return render(request, 'fitness_club/js/text_change.html')
