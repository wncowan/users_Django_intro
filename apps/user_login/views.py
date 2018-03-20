# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "user_login/index.html")