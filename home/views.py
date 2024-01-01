from django.shortcuts import render
from .models import *


# Create your views here.

def index(request):
    if request.method == "GET":
        wall = wallpaper.objects.all()
        cat = category.objects.all()
        context = {"Tittle": "index", "data": wall, "data2": cat}
        return render(request, "index.html", context)


def contact(request):
    if request.method == "GET":
        cat = category.objects.all()
    context = {"Tittle": "contact", "data2": cat}
    return render(request, "contact.html", context)


def gallery(request, pk):
    if request.method == "GET":
        wall = wallpaper.objects.filter(categories_id=pk)
        cat = category.objects.all()
        cate = category.objects.get(id=pk)
        context = {"Tittle": "index", "data": wall, "data2": cat, "data3":cate}
        return render(request, "gallery.html", context)


def single(request, pk):
    if request.method == "GET":
        wall = wallpaper.objects.get(id=pk)
        cat = category.objects.all()
        context = {"Tittle": "index", "data": wall, "data2": cat}
        return render(request, "gallery-single.html", context)

# class gellery(View):
#     def get(self, request):
#         context = {"Title": "gallery"}
#         return render(request, "gallery.html", context)
#
# class contact(View):
#     def get(self, request):
#         context = {"Title": "contact"}
#         return render(request, "contact.html", context)
#
# class single(View):
#     def get(self, request):
#         context = {"Title": "single"}
#         return render(request, "gallery-single.html", context)
