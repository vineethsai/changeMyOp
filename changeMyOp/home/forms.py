from django import forms
from django.utils.translation import ugettext_lazy as _

RELEVANCE_CHOICES = (
        (0, _("Agree")),
        (1, _("Disagree"))
    )


class OpinionForm(forms.Form):
    """
    Opinion form
    """
    text = forms.CharField(label='Enter here:', required=True)
    isPublished = forms.BooleanField(label='Do you want to publish it?', required=True)


class CommentForm(forms.Form):
    """
    Comment form
    """
    text = forms.CharField(label='Enter here:', required=True)
    isPublished = forms.BooleanField(label='Do you want to publish it?', required=True)


class LikeForm(forms.Form):
    """
    Comment form
    """
    forms.ChoiceField(choices=RELEVANCE_CHOICES, widget=forms.RadioSelect, required=True)


