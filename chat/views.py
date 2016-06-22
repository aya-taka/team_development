from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from chat.models import Theme, Comment
from chat.forms import ThemeForm, CommentForm


# 一覧表示
def theme_list(request):
    # 更新の新しい順にソートして取得
    themes = Theme.objects.all().order_by('updatedate')
    return render(request,
                  'chat/theme_list.html',
                  {'theme':themes})


# 作成・編集
def theme_edit(request, theme_id=None):
    # idが指定されている場合=編集
    if theme_id:
        theme = get_object_or_404(Theme, pk=theme_id)
        if theme.user != request.user:
            return redirect('login')
    # idが指定されていない場合=新規作成
    else:
        theme = Theme(authid=request.user)

    # POSTされているとき
    if request.method == 'POST':
        form = ThemeForm(request.POST, instance=theme)
        if form.is_valid():
            theme = form.save(commit=False)
            theme.save()
            return redirect('chat:theme_detail', theme_id=theme.id)
    else:
        form = ThemeForm(instance=theme)

    return render(request, 'chat/theme_detail.html', dict(form=form, theme_id=theme_id))


# 削除
def theme_del(request, theme_id):
    theme = get_object_or_404(Theme, pk=theme_id)
    if theme.user != request.user:
        return redirect('chat:theme_list')
    theme.delete()
    return redirect('chat:theme_list')

