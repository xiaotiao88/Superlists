# from django.http import HttpResponse
from django.shortcuts import redirect,render
from lists.models import Item,List

# Create your views here.
def home_page(request):
    # 该方法可以与list/tests.py页中request.method='POST'相关代码配合使用
    # if request.method=='POST':
    #     Item.objects.create(text=request.POST['item_text'])
    #     return redirect('/lists/the-only-list-in-the-world/')
   
    return render(request,'home.html')


def view_list(request,list_id):
    list_=List.objects.get(id=list_id)
    return render(request,'list.html',{'list':list_})


def new_list(request):
    list_=List.objects.create()
    Item.objects.create(text=request.POST['item_text'],list=list_)
    return redirect('/lists/%d/' %(list_.id,))


def add_item(request,list_id):
    list_=List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'],list=list_)
    return redirect('/lists/%d/' %(list_.id,))
    
