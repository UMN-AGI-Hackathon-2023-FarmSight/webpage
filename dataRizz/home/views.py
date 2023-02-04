from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .forms import NewGraph
from planning_items_scanner import main

def home(response):
  form = NewGraph()
  
  
  
  template = loader.get_template('home.html')
  return render(response, 'home.html', {'form': form})