from django import forms


class GameForm(forms.Form):
    game = forms.ChoiceField(choices=(('coin', 'монетка',), ('cube', 'кубик',), ('number', 'случайное число',), ))
    attempts =forms.IntegerField(min_value=1, max_value=100)

