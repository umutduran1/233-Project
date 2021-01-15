
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from user.views import loginView,registerView,logoutView
from home.views import homeView,contactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homeView,name='home'),
    path('login/',loginView,name='login'),
    path('logout/',logoutView,name='logout'),
    path('register/',registerView,name='register'),
    path('contact/',contactView,name='contact'),
    

    path('user/',include('user.urls')),
    path('post/',include('post.urls')),

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)