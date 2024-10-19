# ABHILASH/forms.py
from django import forms

class TravelExperienceForm(forms.Form):
    DESTINATION_CHOICES = [
        ('paris', 'Paris'),
        ('new_york', 'New York'),
        ('tokyo', 'Tokyo'),
        # Add more destination options as needed
    ]

    destination = forms.ChoiceField(choices=DESTINATION_CHOICES, label="Destination")
    average_temperature = forms.FloatField(label="Average Temperature (°C)")
    tourist_attractions = forms.IntegerField(label="Number of Tourist Attractions")
    accommodation_cost = forms.FloatField(label="Accommodation Cost (per night in $)")
    transportation_cost = forms.FloatField(label="Transportation Cost ($)")
    cuisine_diversity = forms.ChoiceField(choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], label="Cuisine Diversity")
    safety_rating = forms.IntegerField(label="Safety Rating (1-10)")
    nightlife_rating = forms.IntegerField(label="Nightlife Rating (1-10)")
    outdoor_activities = forms.ChoiceField(choices=[
        ('yes', 'Yes'),
        ('no', 'No'),
    ], label="Outdoor Activities Available")
    cultural_heritage = forms.ChoiceField(choices=[
        ('yes', 'Yes'),
        ('no', 'No'),
    ], label="Cultural Heritage Sites Available")
