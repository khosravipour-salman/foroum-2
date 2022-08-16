from django.shortcuts import render
from .models import TagModel
from .forms import TagSearchForm

# Create your views here.

def tag_list(request):
    tags = TagModel.objects.all()
    return render(request, 'extra/tag_list.html', {'tags':tags})

def tag_search(request):
    form = TagSearchForm()

    if request.method == 'POST':
        form = TagSearchForm(request.POST)
        if form.is_valid():
            tag_name = form.cleaned_data.get('name')
            tag_list = TagModel.objects.filter(name__icontains=tag_name)

            context = {'tags':tag_list} 
            return render(request, "extra/tag_list.html", context)

    return render(request, "extra/tag_list.html", {'form':form})
