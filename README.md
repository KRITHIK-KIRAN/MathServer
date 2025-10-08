# Ex.05 Design a Website for Server Side Processing
## Date:30/09/2025

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
BMI=W/H<sup>2</sup>
<br> BMI --> Body Mass Index
<br> W --> Weight
<br> H --> Height

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
<html>
    <head>
        <title>BMI Calculator</title>
        <style>
        body{
          background-color: rgba(79, 5, 108, 0.745);
          border-top: 10;
        }
        .m{
          background-color: rgb(0, 81, 255);
          border-style: inset;
          margin-top: 100px;
          margin-left: 400px;
          margin-right: 400px;
          
        }
        *{
          color: rgb(0, 0, 0);
        }
            .main{
                font-size: 250%;
                text-align: center;
                text-decoration:underline;

                background-color: rgb(200, 0, 0);
                 margin-left: 50px;
                  margin-right: 50px;
                  padding: 5px;
                  
                  
            }
            .a{
                font-size: 150%;
                text-align: center;
                background-color: rgb(5, 5, 126);
                 margin-left: 50px;
                  margin-right: 50px;
                
                 
            }
            form{
              text-align: center;
              background-color: rgb(24, 84, 54);
               margin-left: 50px;
               margin-right: 50px;
             padding: 50px;
            }
           
        </style>
    </head>
    <body>

       <div class="m">
        <div class="main" style="color: rgb(222, 222, 222);">BMI Calculator</div>
        <div class="a">
      <p> Krithik kiran.S 25011340</p></div>
        <form method="post">
          {% csrf_token %}
           
           
            <label>Weight(kg)=</label>
            <input type="text" name="weight" value="{{w}}"><br><br>
             <label>Height(cm)=</label>
            <input type="text" name="height" value="{{h}}"><br><br>
            <button type="submit">Calculate</button><br><br>
            <label>BMI=</label>
            <input type="text" name="bmi" value="{{bmi}}">
        </div>
        </form>
        
        
    </body>
</html>


views.py

from django.shortcuts import render
def calculate_bmi(request):
    context={}
    context['bmi']="0"
    context['w']="0"
    context['h']="0"
    if(request.method=='POST'):
       w= float(request.POST.get('weight','0'))
       h=float(request.POST.get('height','0'))
       print('request=',request)
       
       print('Weight=',w)
       print('Height=',h)
       bmi=w/((h/100)**2)
       context['bmi']=bmi
       context['w']=w
       context['h']=h
       print('BMI=',bmi)
    return render(request,'mathapp/index.html',context)

urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bmi/',views.calculate_bmi,name="bmi"),
    path('',views.calculate_bmi,name="bmicalculator")
]
```

## SERVER SIDE PROCESSING:
![alt text](<Screenshot (17).png>)

## HOMEPAGE:
![alt text](<Screenshot (16).png>)

## RESULT:
The program for performing server side processing is completed successfully.
