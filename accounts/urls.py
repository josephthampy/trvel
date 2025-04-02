from  django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('gallery', views.gallery, name='gallery'),
    path('destinations', views.destinations, name='destinations'),
    path('packages', views.packages, name='packages'),
    path('package1', views.package1, name='package1'),
    path('delhi', views.delhi, name='delhi'),
    path('kerala', views.kerala, name='kerala'),
    path('malaysia', views.malaysia, name='malaysia'),
    path('punjab', views.punjab, name='punjab'),
    path('rajasthan', views.rajasthan, name='rajasthan'),
    path('singapore', views.singapore, name='singapore'),
    path('thailand', views.thailand, name='thailand'),
    path('varanasi', views.varanasi, name='varanasi')
]