from django import forms
from blog.models import Post,Comment

class PostForm(forms.modelForm):

    class Meta():
        model = Post
        Fields = ('author', 'title', 'text')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})

        }


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        Fields = ('author', 'title')

        widgets = {
            'author':forms.TextInput(attr={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea!'})
        }