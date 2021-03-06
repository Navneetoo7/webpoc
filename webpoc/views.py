from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Customer
from .serializers import customerSerializer 
from django.views.decorators.csrf import csrf_exempt




# Create your views here.
@csrf_exempt
def customer_detail(request, pk):
    try:
        detail = Customer.objects.get(pk=pk)
        
    except Customer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method =='GET':
        serializer = customerSerializer(detail)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer= customerSerializer(detail, data=request.data) 

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        detail.delete()
        return JsonResponse(status=204)