from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from base import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include("base.urls")),

]


