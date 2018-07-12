from django import forms
from django.utils.text import slugify

from .models import Article

from pagedown.widgets import PagedownWidget

class CommentForm(forms.Form):

    comment = forms.CharField(widget=forms.Textarea)


class RepostForm(forms.Form):

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
