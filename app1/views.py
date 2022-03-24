from django.shortcuts import render

# Create your views here.
def jinjatags(request):
    d={'cap':'Ravi jadeja'}
    return render(request,'jinja.html',context=d)

def conditions(request):
    d1={'value':16}
    return render(request,'condition.html',d1)
