from django.urls import path

from myapp.views import index, contact_us

urlpatterns = [
    path("", index, name='index'),
    path("contact_us", contact_us, name='contact_us'),
]
