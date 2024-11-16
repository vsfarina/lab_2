from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),  # A URL do blog deve começar com 'blog/'
    path('', include('blog.urls')),
]
