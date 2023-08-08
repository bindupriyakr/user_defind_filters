from django.shortcuts import render

# Create your views here.
def User_Defined_Filters(request):
    d={'data':'Today we are learning User defined Filters'}
    return render(request, 'User_Define_Filters.html',d)