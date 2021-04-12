from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import View
from rest_framework.response import Response

from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login
from django.shortcuts import reverse, redirect
from .models import UserProfile
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import UserProfileSerializer
from rest_framework.decorators import api_view

class UsersListView(View):
    def get(self, request):
        users = UserProfile.objects.all()
        return render(request, 'users_app/users_list.html', context={
            'users': users
        })


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {'form': login_form}
        return render(request, 'auth/login.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('users_list')


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {'form': register_form}
        return render(request, 'auth/registration.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            new_user = register_form.save(commit=False)
            new_user.username = register_form.cleaned_data['username']
            new_user.email = register_form.cleaned_data['email']
            new_user.save()
            new_user.set_password(register_form.cleaned_data['password'])
            new_user.save()
            UserProfile.objects.create(user = new_user, status = 'Unbanned')
            user = authenticate(username = register_form.cleaned_data['username'],
                                password = register_form.cleaned_data['password'])
            login(request, user)
            return redirect('users_list')

        context = {'register_form': register_form}
        return render(request, 'auth/registration.html', context)


class DeleteUserView(View):
    def post(self, request):
        print(request.POST.getlist('checks'))
        return redirect('users_list')


@api_view(['DELETE'])
def user_delete(request, pk):
    user_profile = UserProfile.objects.get(id = pk)
    user = User.objects.get(id = user_profile.user.id)
    print(user)
    # user.delete()
    return Response('Успешно удалено!')



# class UserProfileApiView(ModelViewSet):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer