from django.shortcuts import render,get_object_or_404,redirect

from .models import Post,Comments,Likes
from .forms import CreatePost,CommentForm

def postDetailView(request,id):

    like = True
    post = get_object_or_404(Post,id=id)
    form  = CommentForm(request.POST or None)
    comm = Comments.objects.filter(post=post)

    if request.user.is_authenticated:

        if Likes.objects.filter(post=post,user=request.user):
            like = False

        if form.is_valid():

            com = form.save(commit=False)
            com.user = request.user
            com.post = post
            com.save()
            post.comment = len(comm)
            post.save()

            return redirect('post-detail', id=id)

        for x in comm:
            name = 'btn'+str(x.id)

            if name in request.POST:
                item = Comments.objects.get(user=request.user,id=x.id)
                item.delete()
                comm = Comments.objects.filter(post=post)
                post.comment = len(comm)
                post.save()
                return redirect('post-detail', id=id)

        if 'like' in request.POST:
            if Likes.objects.filter(post=post,user=request.user):

                like = get_object_or_404(Likes,post=post,user=request.user)
                like.delete()
                lv = Likes.objects.filter(post=postDetailView)

                post.like = len(lv)
                post.save()
            else:


                Likes.objects.create(post=post,user=request.user)
                lv = Likes.objects.filter(post=post)                
                post.like = len(lv)
                post.save()

            
            return redirect('post-detail', id=id)

    context = {
        'post':post,
        'title':post.title,
        'form':form,
        'comm':comm,
        'like':like,
    }

    return render(request,'post/detail.html',context)




def postCreateView(request):
    
    form = CreatePost(request.POST or None,request.FILES or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()

        return redirect('post-detail',id=post.id)


    context = {
        'form':form,
        'title':'Yazı Oluştur',
    }

    return render(request,'post/create.html',context)



def postUpdateView(request,id):
    post = get_object_or_404(Post,id=id)
    form = CreatePost(request.POST or None,request.FILES or None,instance=post)

    if form.is_valid():
        post.save()

        return redirect('post-detail',id=post.id)


    context = {
        'form':form,
        'title':'Yazı Güncelle',
    }

    return render(request,'post/update.html',context)