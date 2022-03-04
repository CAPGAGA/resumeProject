from django.shortcuts import render
from django.http import HttpResponse

def main(request, lang='EN'):
    return render(request, 'main/main.html', {'lang':lang})
