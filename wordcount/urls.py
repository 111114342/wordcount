from django.urls import path
from . import views

urlpatterns = (
    path("", views.homepage, name='hello'),
    # path("contact", views.contact)
    path("count/", views.count, name='count'),
    path("about/", views.about, name="about")
)
