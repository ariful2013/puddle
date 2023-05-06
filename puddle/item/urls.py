from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('additem/', views.addItem, name='additem'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.deleteItem, name='deleteitem'),
]
