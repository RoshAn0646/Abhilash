from django.shortcuts import render
from .forms import TravelExperienceForm  # Assuming you have created a form in forms.py

def home(request):
    form = TravelExperienceForm()
    if request.method == 'POST':
        form = TravelExperienceForm(request.POST)
        if form.is_valid():
            # Process the data and load Streamlit here
            # Redirect to a results page or load the Streamlit app
            pass
    return render(request, 'ABHILASH/home.html', {'form': form})
