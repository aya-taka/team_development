from django.forms import ModelForm
from .models import Theme, Comment
from django import forms


class ThemeForm(ModelForm):
    """テーマのフォーム"""
    class Meta:
        model = Theme
        fields = ('theme', 'comment', 'is_enforce', )


class CommentForm(ModelForm):
    """コメントのフォーム"""
    class Meta:
        model = Comment
        fields = ('comment', )


# 検索用フォーム
class SearchForm(forms.Form):
    # 検索キーワード
    keyword = forms.CharField(max_length=100, required=False)



