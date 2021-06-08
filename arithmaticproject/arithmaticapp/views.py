from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def input_view(request):
    return render(request, 'input_data.html')

i = 0
j = 0

def output_view(request):
    value1 = request.POST.get('t1')
    value2 = request.POST.get('t2')
    global i
    global j
    i = int(value1)
    j = int(value2)
    z = request.POST.get('but')

    if z == 'Add':
        return redirect(add)
    elif z == 'Sub':
        pass
    elif z == 'Mul':
        pass
    elif z == 'Div':
        pass
def add(request):
    x = i+j
    return HttpResponse('The Addition of {} and {} is {}'.format(i,j,x))
