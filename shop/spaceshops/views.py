from django.shortcuts import render

# Create your views here.
def space_shop(request):
    return render(request, 'spaceshops/index.html')