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