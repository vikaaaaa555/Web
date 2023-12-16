from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path


from . import views
from .views import FeedbackView, FeedbackForm

urlpatterns = [
    path('fitness_club_home', views.FitnessClubHome.as_view(), name='fitness_club_home'),
    path('', views.home, name="home"),
    path('instructors', views.InstructorsView.as_view(), name='instructors'),
    path('luck', views.luck, name='luck'),
    path('gym_memberships', views.MembershipView.as_view(), name='gym_memberships'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('shopping_cart/<int:membership_id>/', views.shopping_cart, name='shopping_cart'),
    path('admin/', views.admin_view, name='admin'),
    path('inform', views.Inform.as_view(), name='inform'),
    path('about_us', views.about_us, name='about_us'),
    path('news', views.NewsView.as_view(), name='news'),
    path('news_view/<int:news_id>/', views.news_view, name='news_view'),
    path('privacy_politic', views.privacy_politic, name='privacy_politic'),
    path('coupons', views.CouponsView.as_view(), name='coupons'),
    path('faq', views.FAQView.as_view(), name='faq'),
    path('vocation', views.VocationView.as_view(), name='vocation'),
    path('feedback_view/', FeedbackView.as_view(), name='feedback_view'),
    path('feedback_form/', FeedbackForm.as_view(), name='feedback_form'),
    path('certificate/', views.certificate, name='certificate'),
    path('js/scroll/', views.scroll, name='scroll'),
    path('js/autoplay/', views.autoplay, name='autoplay'),
    path('js/associative_array', views.array, name='associative_array'),
    path('js/interactive_table', views.interactive, name='interactive_table'),
    path('js/calculator', views.calculate, name='calculator'),
    path('js/text_change', views.text_change, name='text_change'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)