from django.shortcuts import render
from .models import TagModel

# Create your views here.

def tag_list(request):
	tags = TagModel.objects.all()
	return render(request, 'extra/tag_list.html', {'tags':tags})