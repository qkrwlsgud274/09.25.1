from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
# Create your views here.


@api_view(["POST"])
def sum(request):
    if request.method == "POST":
        a = request.data["email"]
        b = request.data["password"]
        c = {
            "email": str(a),
            "password": str(b),
        }
        return JsonResponse(c, status=201, safe=False)
