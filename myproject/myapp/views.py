from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome Little Lemon")

def menu(request):
    return HttpResponse("Menu for little lemon")

# Create your views here ,pass the dish param u added in urls.py path.
def dishesitems(request,dish):
    
     #dictionary called items
    items={
        #keys values pair
        'Pasta':'Pasta is a type of food typically made from an unleavened dough of wheat flour mixed with water or eggs, and formed into sheets or other shapes, then cooked by boiling or baking.',
        'Falafel':"Falafel is a deep-fried ball or patty-shaped fritter in Middle Eastern cuisine made from ground chickpeas, broad beans, or both.",
        'cheesecake':"Cheesecake is a sweet dessert consisting of one or more layers."
    }
#pass the dic items to dish save the values to var name description
    description =items[dish]

    return HttpResponse(f"<h1> {dish} </h1>"+ description)

#new view func to add drinks items    
def drinksitems(request,drink):
    ditem={
        'mocha':"A caffè mocha, also called mocaccino, is a chocolate-flavoured warm beverage that is a variant of a caffè latte,",
        'tea': "Tea is an aromatic beverage prepared by pouring hot or boiling water over cured or fresh leaves of Camellia sinensis",
        'lemonade':"Lemonade is a sweetened lemon-flavored beverage. There are varieties of lemonade found throughout the world."
    }
    drinkdesc=ditem[drink]
    return HttpResponse(f"<h1>{drink}</h1>"+drinkdesc)

def about(request):
    return HttpResponse("About us")    