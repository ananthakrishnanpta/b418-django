"""
URL configuration for yshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# importing the following to allow media folder to be available in the development server.
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('authentication/',include('authentication.urls')), # including our authentication app's urls
    # to include the paths from django's inbuilt authentication, from django.contrib.auth
    path('authentication/',include('django.contrib.auth.urls'))
]

if settings.DEBUG == True:
    urlpatterns +=  static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# In debug mode, during development, django will help to host the media folder and act as a media server
# But, during deployment, this debug mode will be turned off for security purposes.
# Debug mode throws exceptions into the front end to help debug the backend during development.
# This must be turned off by changing the value of `DEBUG ` variable in django's settings.py.
# The above line of code enables django server to include the media folder in hosting during debug mode.