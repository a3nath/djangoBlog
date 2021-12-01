from django.shortcuts import render

# Create your views here.

def starting_page(request):
    return render(request, "blogApp/index.html")

# for our post url
def posts(req):
    pass

#for an individual post
def post_det(req):
    pass
