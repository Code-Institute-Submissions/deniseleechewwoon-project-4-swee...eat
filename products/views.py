from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    fname = "Denise"
    lname = "Lee"
    return render(request, 'products/index.template.html', {
        'first_name':fname,
        'last_name':lname
    })