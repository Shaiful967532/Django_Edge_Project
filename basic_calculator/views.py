from django.shortcuts import render

def basic_calculator(request):
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1'))
            num2 = float(request.POST.get('num2'))
            operator = request.POST.get('operator')
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2 if num2 != 0 else "Division by zero error"
        except ValueError:
            result = "Invalid input"
    return render(request, 'basic_calculator/index.html', {'result': result})
