from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello, this is my first django app!' +str(data))
    

data = {

   "Name" : "Cece Collado",

    "Track" : "Backend(Python)",

    "Message" : "Thank you mentors for always helping and answering all my simple questions! You guys are great"

}

