from django.urls import path
from . import views
 
urlpatterns=[
path('index/',views.home.as_view(),name='index'),
path('about/',views.about.as_view(),name='aboutus'),
path('receipe-post/',views.recipeHome,name='recipepost'),

path('contact/',views.contact,name='contact'),

path('elements/',views.elements.as_view(),name='elements'),
path('receipe-post/<int:receipepost_id>/',views.details,name='details'),
path('pizzarecipe/',views.pizzarecipe.as_view(),name='pizza'),
path('burgerrecipe/',views.burgerrecipe.as_view(),name='burger'),
path('chillirecipe/',views.chillirecipe.as_view(),name='chilli'),
path('dumrecipe/',views.dumrecipe.as_view(),name='dum'),
path('gajarhalwarecipe/',views.gajarhalwarecipe.as_view(),name='gajarhalwa'),
path('gulabjamunrecipe/',views.gulabjamunrecipe.as_view(),name='gulabjamun'),
path('gunjiyarecipe/',views.gunjiyarecipe.as_view(),name='gunjiya'),
path('noodelsrecipe/',views.noodelsrecipe.as_view(),name='noodels'),
path('pakodarecipe/',views.pakodarecipe.as_view(),name='pakoda'),
path('pastarecipe/',views.pastarecipe.as_view(),name='pasta'),
path('rotirecipe/',views.rotirecipe.as_view(),name='roti'),
path('sandwichrecipe/',views.sandwichrecipe.as_view(),name='sandwich'),
]
