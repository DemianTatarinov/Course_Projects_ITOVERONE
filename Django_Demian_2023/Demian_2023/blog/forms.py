from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length = 60,
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': 'Ваше имя'

        })

    )
    body = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': ' Ваш коментарий'print(1+4*3)
        })
    )