from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from posts.views import home

urlpatterns = [
    # Application views
    path('', home, name='home'),
    path('blog/', include("posts.urls"), name='posts-urls'),
    path('reeds/', include("reeds.urls"), name='reeds-urls'),
    path('events/', include('events.urls'), name='events-urls'),
    path('repertoire/', include('repertoire.urls'), name='repertoire-urls'),
    path('comments/', include('comments.urls'), name='comments-urls'),    
    
    # Auth views
    path('accounts/', include('allauth.urls')),
    
    # Administration view
    path('admin/', admin.site.urls),
]
