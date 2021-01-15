from django.shortcuts import render
from post.models import Post
from .forms import ContactForm


def homeView(request):
    posts = Post.objects.all()

    context = {
        'posts':posts,
    }

    return render(request,'home.html',context)


def contactView(request):
    sending = False
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.save()
        sending = True
        form = ContactForm(request.POST or None)

    context = {
        'form':form,
        'title':'İletişim Formu',
        'sending':sending,
    }

    return render(request,'contact.html',context)