from django.shortcuts import render
from django.http import HttpResponse

def single_photo(request, pk):
    # return HttpResponse('<strong>nothing yet</strong>')

    # response = HttpResponse('<strong>nothing yet</strong>')
    # response.status = 404
    # return response

    response = HttpResponse(
        '<strong>nothing yet</strong>',
        content_type='text/plain',
        status=404,
    )
    return response

#from photos.models import Post

# def index(request):
#     post_list = Post.objects.all()
#     return render(request, 'photos/index.html', {
#             'post_list': post_list,
#         })

# def detail(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(request, 'photos/detail.html', {
#             'post': post,
#         })
