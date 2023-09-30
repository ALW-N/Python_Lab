from django.shortcuts import render
from django.http import HttpResponse

def hi(Request):
    return HttpResponse('<h1> my Home<h1>')
