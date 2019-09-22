from django import forms


class CommentForm(forms.ModelForm):
    author = forms.CharField(max_length=60,
                             widget=forms.TextInput(attrs={
                                 "class": "form-control",
                                 "placeholder": "Your Name",
                                 "required": "True",
                             })
                             )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!",
            "required": "True",
        })
    )
