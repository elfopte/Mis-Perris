from django.urls import path
from .views import home, galeria, registroPostulante




urlpatterns = [

    path('', home, name= "home"),
    path('galeria/', galeria , name ="galeria"),
    path('home/', home, name="home"),
    path('registroPostulante/', registroPostulante, name="registroPostulante"),
    
]