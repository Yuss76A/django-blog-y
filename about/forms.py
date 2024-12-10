from .models import CollaborateRequest
from django import forms


class CollaborateForm(forms.ModelForm):
    """
       Form for submitting a collaboration request.

    This form allows users to provide their name, email, and 
    a message to express interest in collaboration.

    Meta:
        model (CollaborateRequest): The model associated with this form.
        fields (tuple): The fields included in the form - name, email, 
        and message.
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')