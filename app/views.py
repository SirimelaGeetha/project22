from django.shortcuts import render

# Create your views here.


def filters(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'Im the Queen of My Life','dt':'dt','c':1}
    return render(request,'filters.html',d)