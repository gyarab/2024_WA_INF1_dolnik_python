from django.urls import path
from .views import path, include
import content.views    

urlpatterns = [
    path('articles/', include('content.urls')),
]