from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'),name="dummy"),
    path("accounts/",include('accounts.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
