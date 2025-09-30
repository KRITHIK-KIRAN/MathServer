# Ex.05 Design a Website for Server Side Processing
## Date:30/09/2025

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
index.html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Lamp Filament Power Calculator</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 40px;
      background-color: darkblue;
    }
    .container {
      max-width: 400px;
      margin: auto;
      background: white;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    h2 {
      text-align: center;
    }
    label {
      display: block;
      margin-top: 15px;
    }
    input[type="number"] {
      width: 100%;
      padding: 8px;
      margin-top: 5px;
      box-sizing: border-box;
    }
    button {
      margin-top: 20px;
      width: 100%;
      padding: 10px;
      background-color: #007BFF;
      color: white;
      border: none;
      border-radius: 5px;
      font-size: 16px;
    }
    #result {
      margin-top: 20px;
      font-weight: bold;
      text-align: center;
    }
  </style>
</head>
<body>
  <div class="container">
    <h2>Filament Power Calculator</h2>
    <label for="intensity">Intensity (I in Amperes):</label>
    <input type="number" id="intensity" step="any" required>

    <label for="resistance">Resistance (R in Ohms):</label>
    <input type="number" id="resistance" step="any" required>

    <button onclick="calculatePower()">Calculate Power</button>

    <div id="result"></div>
  </div>

  <script>
    function calculatePower() {
      const I = parseFloat(document.getElementById('intensity').value);
      const R = parseFloat(document.getElementById('resistance').value);

      if (isNaN(I) || isNaN(R)) {
        document.getElementById('result').textContent = "Please enter valid numbers for both fields.";
        return;
      }

      const P = I * I * R;
      document.getElementById('result').textContent = `Power (P) = ${P.toFixed(2)} Watts`;
    }
  </script>
</body>
</html>

views.py

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

urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.calculate_power, name='calculate-power'),
]

```

## SERVER SIDE PROCESSING:
![alt text](<Screenshot (5).png>)

## HOMEPAGE:
![alt text](<Screenshot (4).png>)

## RESULT:
The program for performing server side processing is completed successfully.
