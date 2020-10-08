from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name='sell-home'),
    path('about/', views.about_us , name='sell-about'),

]
