from django.shortcuts import render,redirect , get_object_or_404
from  .models import recipes,Contact
# Create your views here.
from django.views.generic import TemplateView
from django.template import loader
from django.http import HttpResponse

class home(TemplateView):
	template_name='index.html'

class about(TemplateView):
	template_name='about.html'


class recipepost(TemplateView):
	template_name='receipe-post.html'

class elements(TemplateView):
	template_name='elements.html'

class pizzarecipe(TemplateView):
	template_name='pizza.html'

class burgerrecipe(TemplateView):
	template_name='burger.html'

class chillirecipe(TemplateView):
	template_name='chilli.html'

class dumrecipe(TemplateView):
	template_name='dum.html'

class gajarhalwarecipe(TemplateView):
	template_name='gajarhalwa.html'

class gulabjamunrecipe(TemplateView):
	template_name='gulabjamun.html'

class gunjiyarecipe(TemplateView):
	template_name='gunjiya.html'

class noodelsrecipe(TemplateView):
	template_name='noodels.html'


class pakodarecipe(TemplateView):
	template_name='pakoda.html'


class pastarecipe(TemplateView):
	template_name='pasta.html'

class rotirecipe(TemplateView):
	template_name='roti.html'

class sandwichrecipe(TemplateView):
	template_name='sandwich.html'

def recipeHome(request):
	new_name= recipes.objects.all()
	return render(request,'receipe-post.html',{'new_name':new_name})   
    
def details(request,receipepost_id):
	details_page = get_object_or_404(recipes,pk=receipepost_id)
	return render(request,'details.html',{'detail':details_page})

def contact(request):
	if request.method =='POST':
		yourname=request.POST.get('fName')
		youremail=request.POST.get('fEmail')
		yoursubject=request.POST.get('fSubject')
		yourmessage=request.POST.get('fMessage')
		var_contact=Contact( name = yourname, email = youremail, subject = yoursubject, message = yourmessage)
		var_contact.save()
		return render(request, 'thank.html')
	else:
		return render(request, 'contact.html')
	