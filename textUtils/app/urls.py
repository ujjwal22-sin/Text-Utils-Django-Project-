from django.contrib import admin
from django.urls import path,include
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index2,name="index2"),
    path('analyze',views.analyze,name="analyze"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
]

