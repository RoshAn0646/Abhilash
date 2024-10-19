# ABHILASH/views.py
from django.shortcuts import render
from .forms import TravelExperienceForm
from .models import DestinationSuggestion  # Make sure to create a model for suggestions if needed

def travel_experience_view(request):
    if request.method == 'POST':
        form = TravelExperienceForm(request.POST)
        if form.is_valid():
            # Process the data and call your model to get suggestions
            destination = form.cleaned_data['destination']
            average_temperature = form.cleaned_data['average_temperature']
            # Add processing logic to call your model
            # For example:
            # suggestion = get_travel_suggestion(destination, average_temperature, ...)
            suggestion = "Example Destination Based on Your Choices"  # Placeholder

            return render(request, 'ABHILASH/suggestion.html', {'suggestion': suggestion})
    else:
        form = TravelExperienceForm()

    return render(request, 'ABHILASH/travel_experience.html', {'form': form})
