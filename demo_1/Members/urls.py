from django.urls  import path
from . import views

urlpatterns = [
    path('Members/', views.members, name='Members'),
    # path('Members/', views.helloWorld, name='Members'),
]