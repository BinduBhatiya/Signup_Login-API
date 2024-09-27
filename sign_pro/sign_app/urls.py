from django.urls import path
from .views import signupapi,loginapi

urlpatterns = [
    path('signup/', signupapi.as_view(), name="signup"),
    path('login/', loginapi.as_view(), name="login"),
]