from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name="base"

urlpatterns=[

	url(r'^admin/', admin.site.urls),
	url(r'^$',views.Index.as_view(), name="index"),
	url(r'^contact-us/$',views.Contact_Us.as_view(), name="contact-us"),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^registration/$', views.register,name='register'),
	url(r'^logout/$', views.user_logout, name="logout"),
	url(r'^category/(?P<slug>[\w-]+)/', views.get_category, name="category"),

]

if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


