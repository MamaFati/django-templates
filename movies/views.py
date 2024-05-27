from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {
        'movies':['young sheldon','The last ship','Casino']
        }
    return render(request, 'movies\index.html', context )

def contact(request):
    socail = {
        'media' :['twitter','Instagram','Linkedin']
    }
    return render(request, 'movies\contact.html', socail)