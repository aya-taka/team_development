from django.shortcuts import render
from accounts.forms import UserChangeForm, UserForm
from accounts.models import UserManager, User
from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView

# Create your views here.


def register(request):
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            # screenname = request.POST['screenname']
            password = request.POST['password']
            new_user = User.objects._create_user(username=username, password=password, is_superuser=False)
            new_user.is_active = True
            new_user.save()
            return render(request, 'accounts/login.html')
    else:
        form = UserForm()

    return render(request, 'accounts/register.html', {'form': form})


# 詳細表示
class daily_detail(DetailView):
    # 表示対象となるモデルの指定
    model = User
    # 表示に使用するテンプレートを指定
    template_name = 'cms/user_detail.html'


# ユーザー情報の編集
def user_edit(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('chat:user_detail', theme_id=user.id)
    else:
        form = UserForm(instance=user)


# ユーザー情報の削除
def user_del(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if user != request.user:
        return redirect('login')
    user.delete()
    return redirect('login')
