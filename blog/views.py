from django.shortcuts import render
from blog.models import Post

def index(request):
    # 전체 포스팅을 가져올 준비. 아직 가져오지는 않음.
    post_qs = Post.objects.all().order_by("-id") # pk = id
    return render(request, "blog/index.html", {
    "post_list" : post_qs,
    })
    # {}는 () 안으로 들어가야 함 = 3번째 인자가 되어야 함!


def single_post_page(request, pk):
    post = Post.objects.get(pk=pk) # all 전부 get 한가지
    return render(request, "blog/single_post_page.html", {
    "post" : post,
    })