from django.urls import path
from insta import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.home,name="homepage"),
    path('post',views.create,name="createpage"),
    path('login',views.loginV,name="loginpage"),
    path('logout',views.logoutV,name="logoutpage"),
    path('register',views.register,name="registerpage"),
    path('profile',views.profile,name="profilepage")
     
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)