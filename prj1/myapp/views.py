from django.shortcuts import render
from myapp.models import *
# Create your views here.
def index(request):
	queryset = profile.objects.all()
	context = {
	"object_list": queryset
	}	
	return render(request,'index.html',context)
