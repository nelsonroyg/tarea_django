from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls', namespace="account")),
    path('tasks/', include('tasks.urls')),
    path('', include('account.urls', namespace="account")),
]
