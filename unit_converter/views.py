from django.shortcuts import render

def unit_converter(request):
    result = None
    if request.method == 'POST':
        try:
            number = float(request.POST.get('number', 0))
            conversion_type = request.POST.get('conversion_type')
            if conversion_type == 'km_to_miles':
                result = number * 0.621371  # kilometers to miles
            elif conversion_type == 'miles_to_km':
                result = number / 0.621371  # miles to kilometers
        except ValueError:
            result = "Invalid input"
    return render(request, 'unit_converter/index.html', {'result': result})
