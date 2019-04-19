from django import forms
from .models import Movie, Score

class MovieModelForm(forms.ModelForm):
    class Meta:
        model = Movie  # 사용하고 있는 모델만 알려주면 된다.
        fields = ['title', 'audience', 'poster_url', 'description', 'genre']  # 어떤 필드를 만들지 구체적으로 알려줌
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '영화제목을 입력해주세요',
                }),
            'audience': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }),
            'poster_url': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '영화이미지 url을 입력해주세요',
                }),
            'genre': forms.select(
                attrs={
                    'class': 'form-control',
                }),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': '영화소개를 작성해 주세요',
                }),
        }

class ScoreModelForm(forms.ModelForm):
    class Meta:
        model = Score  # 사용하고 있는 모델만 알려주면 된다.
        fields = ['title', 'content']  # 어떤 필드를 만들지 구체적으로 알려줌
        widgets = {
            'title': forms.TextInput(
                # attrs 안에는 attribute(속성)가 들어간다.
                attrs={
                    'class': 'form-control',
                    'placeholder': '제목을 입력해주세요',
                }),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': '관람평을 작성해 주세요',
                }),
        }