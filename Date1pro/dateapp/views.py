from django.shortcuts import render

import  datetime as dt
now= dt.datetime.now()
context={'now':now}

# Create your views here.
def date_display(request):
    return render(request,'dateapp/date.html',context)
def year_display(request):
    return render( request,"dateapp/year.html",context)
def month_display(request):
    return render( request,"dateapp/month.html",context)
def day_display(request):
    return render( request,"dateapp/day.html",context)
def hour_display(request):
    return render( request,"dateapp/hour.html",context)
def min_display(request):
    return render( request,"dateapp/min.html",context)
def sec_display(request):
    return render( request,"dateapp/sec.html",context)
def week_display(request):
    return render( request,"dateapp/week.html",context)

