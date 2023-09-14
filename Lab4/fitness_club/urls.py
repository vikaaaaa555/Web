from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path


from . import views

urlpatterns = [
    path('fitness_club_home', views.FitnessClubHome.as_view(), name='fitness_club_home'),
    path('', views.home, name="home"),
    path('instructors', views.InstructorsView.as_view(), name='instructors'),
    path('luck', views.luck, name='luck'),
    path('gym_memberships', views.MembershipView.as_view(), name='gym_memberships'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('shopping_cart/<int:membership_id>/', views.shopping_cart, name='shopping_cart'),
    path('admin/', views.admin_view, name='admin'),
    path('inform', views.inform, name='inform'),
    path('about_us', views.about_us, name='about_us'),
    path('news', views.news, name='news'),
    path('privacy_politic', views.privacy_politic, name='privacy_politic'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)