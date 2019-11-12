from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'COLLEGE'
urlpatterns =[

    path('',views.index,name='home'),
    path('login/',views.my,name='login'),
    # path('admin/',views.my,name='admin'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name='register'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)