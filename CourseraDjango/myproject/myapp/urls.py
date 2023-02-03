from django.urls import path
from . import views

#urls mapping
urlpatterns = [
    
    path('home/',views.home,name="home"),

    path('menu/',views.menu,name="menu"),
    #path ('drinks/<str:name>',views.drinks),str:name-> that name is passed as argument in the view func in views.py
    # <str path converter to capture the URL parameter for the string "Pasta",
    # from view function menuitems (dic) 
    path('dishes/<str:dish>', views.dishesitems),
    #in link add /drinks/tea
    path('drinks/<str:drink>',views.drinksitems),

    path('about',views.about,name="about"),

]
