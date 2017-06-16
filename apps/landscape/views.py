# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    return render(request, 'landscape/index.html')

def results(request, num):
    print "in result"
    print num
    if int(num) <= 10:
        print "10"
        img = "snow"
    elif int(num) <= 20:
        img = "desert"
    elif int(num) <= 30:
        img = "forest"
    elif int(num) <= 40:
        img = "vineyard"
    elif int(num) <= 50:
        img = "tropical"
    elif int(num) > 50:
        return redirect(request, '/fail')
    print img
    imgurl = "landscape/images/"+img+".jpg"
    context = {'imgurl': str(imgurl)}
    print imgurl
    return render(request, 'landscape/results.html', context)
    # Create your views here.
