from django.urls import path
from . import views


urlpatterns =[
    path('dani/',views.users ,name='users'),
    path('create/',views.create ,name='create'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')


]
