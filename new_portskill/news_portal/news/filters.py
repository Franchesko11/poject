import django_filters
from .models import Post
from django import forms

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Заголовок',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    author = django_filters.ModelChoiceFilter(
        queryset=Post.objects.values('author__username').distinct(),
        label='Автор',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    created_at = django_filters.DateFilter(
        lookup_expr='gte',
        label='После даты',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = Post
        fields = ['title', 'author', 'created_at']