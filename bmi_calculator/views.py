from django.shortcuts import render

def bmi_calculator(request):
    bmi = None
    if request.method == 'POST':
        try:
            weight = float(request.POST.get('weight'))
            height = float(request.POST.get('height'))
            bmi = weight / (height ** 2)
        except (ValueError, ZeroDivisionError):
            bmi = "Invalid input"
    return render(request, 'bmi_calculator/index.html', {'bmi': bmi})
