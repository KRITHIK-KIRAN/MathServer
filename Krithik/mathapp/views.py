
from django.shortcuts import render

def calculate_power(request):
    if request.method == 'POST':
        try:
            intensity = float(request.POST.get('intensity'))
            resistance = float(request.POST.get('resistance'))
            power = intensity ** 2 * resistance

            # Print to terminal
            print("⚡ Received POST request")
            print(f"Intensity (I): {intensity} A")
            print(f"Resistance (R): {resistance} Ω")
            print(f"Calculated Power (P): {power:.2f} Watts")

            return render(request, 'mathapp/index.html', {
                'result': f'Power (P) = {power:.2f} Watts',
                'intensity': intensity,
                'resistance': resistance
            })
        except (TypeError, ValueError):
            print("❌ Invalid input received")
            return render(request, 'mathapp/index.html', {
                'result': 'Please enter valid numbers.'
            })
    else:
        return render(request, 'mathapp/index.html')