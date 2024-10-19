from django import forms

class TravelExperienceForm(forms.Form):
    destination = forms.CharField(label='Destination', max_length=100)
    average_temperature = forms.FloatField(label='Average Temperature')
    tourist_attractions = forms.IntegerField(label='Tourist Attractions')
    accommodation_cost = forms.FloatField(label='Accommodation Cost')
    transportation_cost = forms.FloatField(label='Transportation Cost')
    cuisine_diversity = forms.CharField(label='Cuisine Diversity', max_length=100)
    safety_rating = forms.FloatField(label='Safety Rating')
    nightlife_rating = forms.FloatField(label='Nightlife Rating')
    outdoor_activities = forms.CharField(label='Outdoor Activities', max_length=100)
    cultural_heritage = forms.ChoiceField(label='Cultural Heritage', choices=[('Yes', 'Yes'), ('No', 'No')])
