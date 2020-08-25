from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('details/',views.details,name='details'),
    path('submit/',views.submit,name='submit'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]