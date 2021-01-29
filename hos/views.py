from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def graph(request):
    datas= [
            ['Patients', 65],
            ['Empty beds', 35],
        ]
    context = {
      'datas':datas
    };
    return JsonResponse(context)