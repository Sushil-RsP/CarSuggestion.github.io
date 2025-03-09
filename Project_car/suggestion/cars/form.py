from django import forms

BodyType = [
    ('', 'Select Body Type'),
    ('SUV', 'SUV'),
    ('Sedan', 'Sedan'),
    ('Hatchback', 'Hatchback'),
    ('MPV', 'MPV'),
]

Manufacturer = [
    ('', 'Select Manufacturer'),
    ('Kia', 'Kia'),
    ('Mahindra', 'Mahindra'),
    ('Honda', 'Honda'),
    ('Renault', 'Renault'),
    ('Hyundai', 'Hyundai'),
    ('Toyota', 'Toyota'),
    ('Maruti', 'Maruti'),
    ('Jeep', 'Jeep'),
    ('Nissan', 'Nissan'),
    ('Tata', 'Tata'),
]

FuelType = [
    ('', 'Select Fuel Type'),
    ('Diesel', 'Diesel'),
    ('Petrol', 'Petrol'),
    ('CNG', 'CNG'),
]

DesiredFeatures = [
    ('', 'Select Desired Features'),
    ('Infotainment', 'Infotainment'),
    ('Rear Camera', 'Rear Camera'),
    ('Sunroof', 'Sunroof'),
    ('ADAS', 'ADAS'),
    ('ABS', 'ABS'),
    ('7-Seater', '7-Seater'),
    ('Airbags','Airbags'),
    ('CNG', 'CNG'),
    ('4x4', '4x4'),
]

SafetyRating = [
    ('', 'Safety Rating'),
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
]


class suggestionForm(forms.Form):

    Body_Type = forms.ChoiceField(label='Body Type', choices=BodyType, required=True)
    #Body_Type = forms.CharField(label='Body Type')

    Manufacturer = forms.ChoiceField(label='Manufacturer', choices=Manufacturer, required=True)
    #Manufacturer = forms.CharField(label='Manufacture')

    Fuel_Type = forms.ChoiceField(label='Flue Type', choices=FuelType, required=True)
    #Fuel_Type = forms.CharField(label='Fuel Type')

    Safety_Rating = forms.ChoiceField(label='Safety Rating', choices=SafetyRating, required=True)
    #Safety_Rating = forms.FloatField(label='Safety Rating', min_value=0, max_value=5)

    Budget = forms.FloatField(label='Budget', min_value=200000, max_value=5000000)

    Desired_Features = forms.ChoiceField(label='Desired Features', choices= DesiredFeatures, required=True)
    #Desired_Features = forms.CharField(label='Desired Features')

    Age = forms.IntegerField(label='Age', min_value=0, required=True)

    Family_Size = forms.IntegerField(label='Family Size', min_value=0, required=True)
