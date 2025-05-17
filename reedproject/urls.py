from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from reeds.views import home

urlpatterns = [
    # Application views
    path('', home, name='home'),
    path('blog/', include("posts.urls"), name='posts-urls'),
    path('reeds/', include("reeds.urls"), name='reeds-urls'),
    
    # Auth views
    path('accounts/', include('allauth.urls')),
    
    # Administration view
    path('admin/', admin.site.urls),
]
