from django import forms

class StudentForm(forms.Form):
    studytime = forms.IntegerField(min_value=1, max_value=4)
    failures = forms.IntegerField(min_value=0, max_value=3)
    absences = forms.IntegerField(min_value=0)
    G1 = forms.IntegerField(min_value=0, max_value=20)
    G2 = forms.IntegerField(min_value=0, max_value=20)
    Medu = forms.IntegerField(min_value=0, max_value=4)
    Fedu = forms.IntegerField(min_value=0, max_value=4)
    internet = forms.ChoiceField(choices=[('1', 'Yes'), ('0', 'No')])
    goout = forms.IntegerField(min_value=1, max_value=5)
    freetime = forms.IntegerField(min_value=1, max_value=5)
