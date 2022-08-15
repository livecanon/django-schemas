from django import forms


# see https://docs.djangoproject.com/en/3.2/topics/forms/#more-on-fields
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)
