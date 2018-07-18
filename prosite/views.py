from django.shortcuts import render, get_object_or_404
from prosite.models import Block
from prosite.models import Album
from prosite.models import Text


def main_page(request):
    model_block = Block.objects.all().order_by('id')
    model_photo = Album.objects.all()
    model_text = Text.objects.all()
    print([m.photo.url for m in model_photo])
    print(model_photo)
    print ([m.body for m in model_text])
    print (model_text)


    return render(request, 'blog/main_page.html', {"model_block": model_block, "model_photo": model_photo, "model_text": model_text})


def rsvp(request):

    return render(request, 'blog/rsvp.html', {})


def event(request):
    return render(request, 'blog/event.html', {})


def photo(request):
    model_block = Block.objects.all ()
    model_photo = Album.objects.all ().order_by('title')
    print ([m.photo.url for m in model_photo])
    print (model_photo)
    return render(request, 'blog/photo.html', {"model_block": model_block, "model_photo": model_photo})


def party(request):
    model_block = Block.objects.all ().order_by ('id')
    model_photo = Album.objects.all ()
    model_text = Text.objects.all ()
    print ([m.photo.url for m in model_photo])
    print (model_photo)
    print ([m.body for m in model_text])
    print (model_text)
    return render(request, 'blog/party.html', {"model_block": model_block, "model_photo": model_photo, "model_text": model_text})


def travel(request):
    return render(request, 'blog/travel.html', {})


def gift(request):
    return render(request, 'blog/gift.html', {})

