from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signupView.as_view(), name='signup'),
]