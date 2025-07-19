from django.shortcuts import render
from .forms import StudentForm
import pickle
import pandas as pd
import os

# Load model once when server starts
model_path = os.path.join(os.path.dirname(__file__), 'student_model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

def predict_result(request):
    result = None
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            df = pd.DataFrame([{
                'studytime': data['studytime'],
                'failures': data['failures'],
                'absences': data['absences'],
                'G1': data['G1'],
                'G2': data['G2'],
                'Medu': data['Medu'],
                'Fedu': data['Fedu'],
                'internet': int(data['internet']),
                'goout': data['goout'],
                'freetime': data['freetime']
            }])

            pred = model.predict(df)[0]
            result = "Pass 🎉" if pred == 1 else "Fail 😢"

    else:
        form = StudentForm()

    return render(request, 'predictor/form.html', {'form': form, 'result': result})
