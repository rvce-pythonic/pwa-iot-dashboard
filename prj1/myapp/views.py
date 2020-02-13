from django.shortcuts import render
from myapp.models import usr_profile
def index(request):
	queryset = usr_profile.objects.all()
	context = {
	"object_list": queryset,
	"user": 'username'
	}
	return render(request,'index.html',context)
# Create your views here.


