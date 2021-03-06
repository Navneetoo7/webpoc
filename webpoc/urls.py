from .views import customer_detail
from django.urls import path
urlpatterns = [
    path('start/<int:pk>', customer_detail),
    
]