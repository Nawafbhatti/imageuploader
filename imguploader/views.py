from django.shortcuts import render
from imguploader.models import uploadimg

def index(request):
    if request.method == 'POST':
        pic = request.FILES["img"]
        omg = uploadimg.objects.create(picture = pic)
        omg.save()
    return render(request, "index.html")