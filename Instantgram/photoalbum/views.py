from .models import Photo
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
#from django.urls import reverse
#from django.shortcuts import get_object_or_404, reverse

#from .forms import LoginForm, RegisterForm, AddParticipantForm
#from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
#from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.mixins import PermissionRequiredMixin

from django.views import View

class MainView(View):

    def get(self, request):
        photos = Photo.objects.all().order_by('creation_date')
        return render(request, "main.html", {'photos': photos})
