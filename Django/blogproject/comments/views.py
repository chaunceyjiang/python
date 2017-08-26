from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from .models import Comment
from .form import CommentsForm
import markdown
# Create your views here.

def post_comment(request,post_pk):
    post=get_object_or_404(Post,pk=post_pk)
    post.body=markdown.markdown(post.body,extensions=[ 'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',])
    if request.method=="POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context={
                'post':post,
                'form':form,
                'comment_list':comment_list,
            }
        return render(request,'blog/detail.html',context=context)
    return redirect(post)