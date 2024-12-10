from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.


def about_me(request):
    """
     Renders the About page and handles collaboration requests.

    If the request method is POST, it processes the collaboration form,
    saves it if valid, and displays a success message.

    Attributes:
        request (HttpRequest): The HTTP request object containing metadata 
        about the request.

    Returns:
        HttpResponse: Renders the 'about.html' template with the latest 
        About information and the collaboration form. 
    """
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if  collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, 
"Collaboration request received! I endeavor to respond within 2 working days.")

    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
        "about": about,
        "collaborate_form": collaborate_form

        },
        
    )
