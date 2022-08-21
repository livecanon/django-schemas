from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(
                attrs={"class": "form-control", "cols": 80, "rows": 8}
            ),
            "tags": forms.CheckboxSelectMultiple(),
        }

    # see https://docs.djangoproject.com/en/3.2/ref/forms/validation/
    def clean_title(self):
        if self.cleaned_data["title"] == "mock":
            # self.add_error('title', 'asd is incorect')
            raise forms.ValidationError("Incorrect value.")

        return self.cleaned_data["title"]
