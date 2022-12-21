from .models import record, recharge_list
from django.shortcuts import render
from .serializers import rechargeSerializer, historySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime

def home(request):
    return render(request,'home.html')

@api_view()
def recharge(request):
    rech_list = recharge_list.objects.all()
    serializer = rechargeSerializer(rech_list,many=True)
    return Response(serializer.data)

@api_view()
def history(request,num):
    hist = record.objects.filter(phone=num)
    serializer = historySerializer(hist,many=True)
    return Response(serializer.data)

def do_recharge(request,id,num):
    try:
        
        detail = recharge_list.objects.filter(id=id)[0]
        recharge = record(recharge_id=detail.id, phone=num,title=detail.title,ammount=detail.amount,detail=detail.detail,recharge_date=datetime.now())
        recharge.save()
        context = {
            "amt":detail.amount,
            "num":num,
            "det":detail.detail,
            "result":1
        }
        return render(request,'home.html',context)
    except Exception as e:
        print(e)
        return render(request,'home.html',{"result":0})


    





