from django import forms
from django.utils.text import slugify

<<<<<<< HEAD
from .models import Article, Comment
from pagedown.widgets import PagedownWidget

=======
from .models import Article

from pagedown.widgets import PagedownWidget
>>>>>>> 3ec144f17a8518fac5452626e5ad3279f4829cb5

class CommentForm(forms.Form):

    comment = forms.CharField(widget=forms.Textarea)


<<<<<<< HEAD
class ArticleEdit(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'image'
        ]


class CommentEditForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content'
        ]


class RepostForm(forms.Form):
=======
class RepostForm(forms.Form):

>>>>>>> 3ec144f17a8518fac5452626e5ad3279f4829cb5
    repost_comment = forms.CharField(widget=forms.Textarea)


class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(
                            attrs={
                                                    'class': 'form-control',
                                                    'placeholder': 'Write about it...'
                            }
        ))

    class Meta:
        model = Article
        fields = ('title', 'content', 'image',)

    def save(self, user, category):
        article = super(ArticleForm, self).save(commit=False)
        article.author = user
        article.slug = slugify(article.title)
        article.category = category
        article.save()

        return article
