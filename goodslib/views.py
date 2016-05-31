from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.template import Template, Context
from goodslib.models import Good_brand, Goods_kind, Goods_attr, Goods_color,Goods, Goods_lib
# Create your views here.

def index(request):
    
    clist = Goods_color.objects.all()
    glist = Goods.objects.all()
    blist = Good_brand.objects.all()
    klist = Goods_kind.objects.all()
    alist = Goods_attr.objects.all()
    llist = Goods_lib.objects.all()
    a = 1
    print a 
    return render_to_response("goods_lib/goods_base.html",locals())

