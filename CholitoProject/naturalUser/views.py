from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from CholitoProject.userManager import get_user_index
from complaint.models import AnimalType
from naturalUser.forms import SignUpForm, AvatarForm
from naturalUser.models import NaturalUser, FavoriteONGs
from ong.models import ONG
from animals.models import *
from municipality.models import MunicipalityUser

class IndexView(TemplateView):
    context = {}

    def get(self, request, **kwargs):
        c_user = get_user_index(request.user)
        self.context['c_user'] = c_user
        animals = AnimalType.objects.all()
        self.context['animal_types'] = animals
        ongs = ONG.objects.all()
        self.context['ongs'] = ongs
        if c_user is None:
            return render(request, 'index.html', context=self.context)
        elif request.user.has_perm('municipality.municipality_user_access'):
            return c_user.get_index(request, context=self.context)
        favorites_temp = FavoriteONGs.objects.filter(user=c_user)
        favorites = []
        for fav in favorites_temp:
            for ong in ongs:
                if fav.ongs.id == ong.id:
                    favorites.append(fav)
                    break
        self.context['favorites'] = favorites
        return c_user.get_index(request, context=self.context)

    def post(self, request, **kwargs):
        ongs_raw = ONG.objects.all()
        filter_by_type = request.POST.get('filter_type')
        selected_type = request.POST.get('animal_type')
        filter_by_age = request.POST.get('filter_age')
        selected_age_range = request.POST.get('age_range')
        ongs_temp = []

        if filter_by_type == "1":
            for ong in ongs_raw:
                animals = Animal.objects.filter(ong = ong)
                for animal in animals:
                    if animal.animal_type.name == selected_type:
                        ongs_temp.append(ong)
                        break
        else:
            for ong in ongs_raw:
                ongs_temp.append(ong)

        ongs = []
        max = 0
        min = 0
        if filter_by_age == "1":
            if selected_age_range == "0":
                max = 1
            elif selected_age_range == "1":
                min = 2
                max = 4
            elif selected_age_range == "2":
                min = 4
                max = 10
            elif selected_age_range == "3":
                min = 10
                max = 10000
            for ong in ongs_temp:
                animals = Animal.objects.filter(ong=ong)
                for animal in animals:
                    if animal.estimated_age >= min and animal.estimated_age <= max:
                        ongs.append(ong)
                        break
        else:
            for ong in ongs_temp:
                ongs.append(ong)

        c_user = get_user_index(request.user)
        animals = AnimalType.objects.all()
        self.context['c_user'] = c_user
        self.context['animal_types'] = animals
        self.context['ongs'] = ongs
        if c_user is None:
            return render(request, 'index.html', context=self.context)
        favorites_temp = FavoriteONGs.objects.filter(user=c_user)
        favorites = []
        for fav in favorites_temp:
            for ong in ongs:
                if fav.ongs.id == ong.id:
                    favorites.append(fav)
                    break
        self.context['favorites'] = favorites
        return c_user.get_index(request, context=self.context)

class LogInView(TemplateView):
    template_name = 'login.html'
    animals = AnimalType.objects.all()
    ongs = ONG.objects.all()
    context = {'animal_types': animals, 'ongs': ongs}

    def get(self, request, **kwargs):
        return render(request, self.template_name, context=self.context)


class SignUpView(View):
    user_form = SignUpForm(initial={'username': 'dummy'}, prefix='user')
    avatar_form = AvatarForm(prefix='avatar')
    animals = AnimalType.objects.all()
    context = {'user_form': user_form,
               'avatar_form': avatar_form, 'animal_types': animals}
    template_name = 'sign_up.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name, context=self.context)

    def post(self, request, **kwargs):
        user_form = SignUpForm(request.POST, prefix='user')
        avatar_form = AvatarForm(request.POST, request.FILES, prefix='avatar')
        if user_form.is_valid() and avatar_form.is_valid():
            user_ = user_form.save()
            user_.refresh_from_db()
            natural_user = NaturalUser.objects.create(
                user=user_, avatar=avatar_form.cleaned_data.get('avatar'))
            username = user_form.cleaned_data.get('email')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        messages.error(request,
                       "Ha ocurrido un error en el registro. Debes ingresar todos los campos para registrarse")
        return render(request, self.template_name, context=self.context)


class UserDetail(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = 'naturalUser.natural_user_access'

    def post(self, request, **kwargs):
        c_user = get_user_index(request.user)
        c_user.user.first_name = request.POST['f_name']
        c_user.user.last_name = request.POST['l_name']
        if 'avatar' in request.FILES:
            c_user.avatar = request.FILES['avatar']
        c_user.save()
        return redirect('/')


class OngInViewTemplate(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    permission_required = 'naturalUser.natural_user_access'
    template_name = 'usuario-in-ong.html'
    context = {}

    def get(self, request, pk, **kwargs):
        natural = NaturalUser.objects.get(user = request.user)
        ong = get_object_or_404(ONG, pk=pk)

        try:
            FavoriteONGs.objects.get(user=natural.id, ongs=pk)
            self.context['ong_is_fav'] = True
        except FavoriteONGs.DoesNotExist:
            self.context['ong_is_fav'] = False

        try:
            self.context['ong_count'] = FavoriteONGs.objects.filter(ongs=pk).count()
        except FavoriteONGs.DoesNotExist:
            self.context['ong_count'] = 0

        animals = AnimalType.objects.all()
        self.context['animal_types'] = animals
        user = get_user_index(request.user)
        self.context['user'] = request.user
        self.context['c_user'] = user
        self.context['ong'] = ong
        animals = Animal.objects.filter(ong=ong.id)
        animal_images = []
        for animal in animals:
            animal_images.append(AnimalImage.objects.filter(animal=animal.id)[0])
        self.context['animals'] = animal_images

        return render(request, self.template_name, context=self.context)

    def post(self, request, pk, **kwargs):
        natural = NaturalUser.objects.get(user = request.user)
        ong = get_object_or_404(ONG, pk=pk)

        try:
            FavoriteONGs.objects.get(user=natural.id, ongs=ong)
            self.context['ong_is_fav'] = False
            FavoriteONGs.objects.get(user=natural, ongs=pk).delete()
        except FavoriteONGs.DoesNotExist:
            self.context['ong_is_fav'] = True
            FavoriteONGs.objects.create(user=natural, ongs=ong).save()

        try:
            self.context['ong_count'] = FavoriteONGs.objects.filter(ongs=pk).count()
        except FavoriteONGs.DoesNotExist:
            self.context['ong_count'] = 0

        animals = AnimalType.objects.all()
        self.context['animal_types'] = animals
        user = get_user_index(request.user)
        self.context['user'] = request.user
        self.context['c_user'] = user
        self.context['ong'] = ong
        animals = Animal.objects.filter(ong=ong.id)
        animal_images = []
        for animal in animals:
            animal_images.append(AnimalImage.objects.filter(animal=animal.id)[0])
        self.context['animals'] = animal_images

        return render(request, self.template_name, context=self.context)

class OngOutViewTemplate(TemplateView):
    template_name = 'usuario-out-ong.html'
    context = {}

    def get(self, request, pk, **kwargs):
        ong = get_object_or_404(ONG, pk=pk)

        try:
            self.context['ong_count'] = FavoriteONGs.objects.filter(ongs=pk).count()
        except FavoriteONGs.DoesNotExist:
            self.context['ong_count'] = 0

        animals = AnimalType.objects.all()
        self.context['animal_types'] = animals
        self.context['ong'] = ong
        animals = Animal.objects.filter(ong=ong.id)
        animal_images = []
        for animal in animals:
            animal_images.append(AnimalImage.objects.filter(animal=animal.id)[0])
        self.context['animals'] = animal_images
        return render(request, self.template_name, context=self.context)