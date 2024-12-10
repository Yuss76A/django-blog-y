from django import forms
from .models import Comment



class CommentForm(forms.ModelForm):
    """
    A form for submitting a comment on a blog post.

    This form allows users to enter the body of their comment. 

    Attributes:
        body (TextField): The content of the comment, which will be saved 
        to the associated Comment model instance.

    Meta:
        model (Comment): The model associated with this form.
        fields (tuple): The fields included in the form - only 'body'.
    """
    class Meta:
        model = Comment
        fields = ('body',)
