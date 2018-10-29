from django import forms
from blog.models import Comment, Post
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required':False, 'cols':30, 'rows':10}
        )
    )
    class Meta():
        model = Post
        fields = ('author', 'title', 'text','content') #'photo')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),

        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
        'author':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
    }

class FlatPageForm(forms.ModelForm):
    content = forms.CharField(widget =TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = FlatPage
        fields = "__all__"
