from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import Text

# Create your views here.

def main(request, location: str):
    if Text.objects.filter(location = location).exists():
        text = Text.objects.get(location = location)
        content = text.content
        MMIE = text.MMIE
        return HttpResponse(content, content_type=MMIE)
    else:
        return HttpResponse("Not found", content_type="text/plain", status=404)

def change(request, location: str):
    return redirect("/admin/main/text/{}/change/".format(location))



