from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from CholitoProject.userManager import get_user_index
from ong.models import ONG
from animals.models import *
from naturalUser.models import NaturalUser, FavoriteONGs
# Create your views here.

class ONGforNaturalUser(View):
    template = 'ong-adopcion-ya.html'
    context = {}

    def get(self, request, pk, **kwargs):
        user = get_user_index(request.user)
        self.context['user'] = request.user
        self.context['c_user'] = user
        ong = get_object_or_404(ONG, pk=pk)
        self.context['ong'] = ong
        animals = Animal.objects.filter(ong = ong.id)
        animal_images = []
        for animal in animals:
            animal_images.append(AnimalImage.objects.filter(animal=animal.id)[0])
        self.context['animals'] = animal_images

        return render(request, self.template, context=self.context)
