from django.shortcuts import render

# Create your views here.
def index(request):
    template='noticias/index.html'
    return render(request,template)