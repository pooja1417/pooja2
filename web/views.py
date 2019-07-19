from django.shortcuts import render
from .models import Roles 

# Create your views here.

def career_view(request):
	obj=Roles.objects.all()
	ct=Roles.objects.all().count()
	return render(request,'career.html',{'obj':obj,'ct':ct})