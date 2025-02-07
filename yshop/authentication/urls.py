from django.urls import path
from .views import UserRegisterView, Login

urlpatterns = [
    path('register', UserRegisterView.as_view(), name='signup'),
    # We have used the .as_view() method here to expose the function within the class.
    # path function expects a function to be used as a view.

    path('login', Login.as_view(), name='signin')

]