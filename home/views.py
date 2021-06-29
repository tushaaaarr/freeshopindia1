from django.shortcuts import render,HttpResponse
from home.models import Product
from home.models import New_Product2
from home.models import Searched_item
# from django.http import HttpRespons
# Create your views here.
from home.models import Mobile
from home.models import Laptop
import math
from django.db.models import Max,Min,Count
from django.db.models import Min,Max
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic import ListView
import json
from django.http import JsonResponse
from django.core.paginator import Paginator
from bs4 import BeautifulSoup
import requests
import re
import datetime

def home(request):
    no_of_posts = 15
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    prod_all = Product.objects.all()
    length = len(prod_all)
    prod_all= prod_all[(page-1)*no_of_posts: page*no_of_posts]
    
    
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    minMaxPrice=Product.objects.aggregate(Min('price'),Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    filtered_price=request.GET.get('filter')
    # headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    # url = 'https://www.flipkart.com/search?q=microwaves&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    # response=requests.get(url,headers=headers)
    # soup=BeautifulSoup(response.content,'lxml')
    # # soup=BeautifulSoup(response.content,'lxml')
    # price_lst = []
    # for item in soup.select('[data-id]'):
    #     try:
    #         title= item.select('a img')[0]['alt']
    #         prices = item.find_all(text=re.compile('₹'))
    #         prices=prices[0][1:]
    #         images = item.select('img')[0].get('src')
    #         prices=re.sub(",","",prices)
    #         d = datetime.date(2021, 6, 24)
           
    #         New_Product2 =Product(product_name=title,img_url1=images,price=prices,category='electronics',
    #         pub_date = d ,sub_category='microwave',brand='microwave') 
    #         New_Product2.save()   
    #     except Exception as e:
    #         #raise e
    #         b=0
    filtered=Product.objects.filter(price__range=(price_min,filtered_price)).order_by('-price')[::-1]
    
    page_len=math.ceil(length/ no_of_posts)
    
    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    params = {'prod_all':prod_all,'prev':prev, 'nxt':nxt,'min_price':min_price,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'filtered':filtered,
    'page_len':range(1,page_len+1),'filtered_price':filtered_price}
    return render(request, 'index.html', params)
def fashion(request):
    no_of_posts = 15
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    prod_all = Product.objects.all()
    length = len(prod_all)
    prod_all= prod_all[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    minMaxPrice=Product.objects.aggregate(Min('price'),Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    filtered_price=request.GET.get('filter')
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    url = 'https://www.flipkart.com/search?q=cameras&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.content,'lxml')
    # soup=BeautifulSoup(response.content,'lxml')
    price_lst = []
    for item in soup.select('[data-id]'):
        try:
            title= item.select('a img')[0]['alt']
            prices = item.find_all(text=re.compile('₹'))
            prices=prices[0][1:]
            images = item.select('img')[0].get('src')
            prices=re.sub(",","",prices)
            d = datetime.date(2021, 6, 18)
            New_Product2 =Product(product_name=title,img_url1=images,price=prices,category='electronics',
            pub_date = d ,sub_categor='camera',brand='camera') 
            New_Product2.save()
        except Exception as e:
            #raise e
            b=0
    filtered=Product.objects.filter(price__range=(price_min,filtered_price)).order_by('-price')[::-1]
    page_len=math.ceil(length/ no_of_posts)    
    params = {'prod_all':prod_all,'prev':prev, 'nxt':nxt,'min_price':min_price,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'filtered':filtered,
    'page_len':range(1,page_len+1),'filtered_price':filtered_price}
    return render(request, 'fashion.html', params) 

def slide(request):
  
    value = request.GET.get('value')
    print('value is ',value)
    return render(request, 'slide.html')
    # mobile = Product.objects.filter(sub_category='mobile')
    # minMaxPrice=Product.objects.filter(sub_category='mobile').aggregate(Min('price'),Max('price'))
    # price_max=minMaxPrice.get('price__max')
    # # filtered_mobile=Product.objects.filter(price__range=(price_min,filtered_price),sub_category='mobile').order_by('-price')[::-1]
    # price_under5000 = Product.objects.filter(price__range=(0,5000),sub_category='mobile').order_by('-price')[::-1]
    # price_5000_to_10000 = Product.objects.filter(price__range=(5000,10000),sub_category='mobile').order_by('-price')[::-1]
    # price_10000_to_20000 = Product.objects.filter(price__range=(10000,20000),sub_category='mobile').order_by('-price')[::-1]
    # price_over_20000 = Product.objects.filter(price__range=(20000,price_max),sub_category='mobile').order_by('-price')[::-1]
    # params = {'price_under5000':price_under5000,'price_5000_to_10000':price_5000_to_10000,
    # 'price_10000_to_20000':price_10000_to_20000,'mobile':mobile}
    # return render(request, 'slide.html',params)

def home_prod(request):
    return render(request, 'home.html')

def appliances(request):
    sub_cat = 'kitchen_appliances'
    price_1= 2000
    price_2 = 3000
    price_3 = 4000
    img_height = 120
    img_width = 120
    no_of_posts = 20
    value = request.GET.get('kitchen_appliances_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 

    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,
  
    'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'appliances.html',params)

def pantry(request):
    prod_all = Product.objects.all()
    return render(request, 'pantry.html',{'prod_all': prod_all})

def ascending_products_home(request):
    no_of_posts = 15
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    ascending_prod=Product.objects.all().order_by('-price')[::-1]
    length = len(ascending_prod)
    ascending_prod= ascending_prod[(page-1)*no_of_posts: page*no_of_posts]

    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    minMaxPrice=Product.objects.aggregate(Min('price'),Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    filtered_price=request.GET.get('filter')
    filtered_home=Product.objects.filter(price__range=(price_min,filtered_price)).order_by('-price')[::-1]
    parmas ={'ascending_prod':ascending_prod,'prev':prev, 'nxt':nxt,'page_len':range(1,page_len+1),'min_price':min_price,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'filtered_home':filtered_home,'filtered_price':filtered_price}

    return render(request, 'ascending_products_home.html',parmas)


def descending_products_home(request):
    no_of_posts = 15
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    descending_prod=Product.objects.all().order_by('-price')
    length = len(descending_prod)
    descending_prod= descending_prod[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts)
    filtered_price=request.GET.get('filter')
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    minMaxPrice=Product.objects.aggregate(Min('price'),Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    filtered_home=Product.objects.filter(price__range=(price_min,filtered_price)).order_by('-price')

    parmas= {'descending_prod':descending_prod,'prev':prev, 'nxt':nxt,'page_len':range(1,page_len+1),
    'min_price':min_price,'filtered_home':filtered_home,
    'max_price':max_price,'minMaxPrice':minMaxPrice}
    return render(request, 'ascending_products_home.html',parmas)


def ascending_products_electronics(request):
    no_of_posts = 15
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    ascending_prod_elctro= Product.objects.filter(category= 'electronics').order_by('-price')[::-1]
    length = len(ascending_prod_elctro)
    ascending_prod_elctro= ascending_prod_elctro[(page-1)*no_of_posts: page*no_of_posts]

    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    minMaxPrice=Product.objects.filter(category='electronics').aggregate(Min('price'),Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    filtered_price=request.GET.get('filter')
    filtered_electronics=Product.objects.filter(price__range=(price_min,filtered_price),category='electronics').order_by('-price')[::-1]
    params = {'ascending_prod_elctro':ascending_prod_elctro,'prev':prev,
     'nxt':nxt,'page_len':range(1,page_len+1),'min_price':min_price,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'filtered_electronics':filtered_electronics}

    return render(request,'ascending_products_home.html', params)


def descending_products_electronics(request):
    no_of_posts = 15
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    descending_prod_electro=Product.objects.filter(category='electronics').order_by('-price')
    length = len(descending_prod_electro)
    descending_prod_electro= descending_prod_electro[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts)
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    minMaxPrice=Product.objects.filter(category='electronics').aggregate(Min('price'),Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    filtered_price=request.GET.get('filter')
    filtered_electronics=Product.objects.filter(price__range=(price_min,filtered_price),category='electronics').order_by('-price')[::-1]
    params={'descending_prod_electro':descending_prod_electro,'prev':prev, 'nxt':nxt,
                        'page_len':range(1,page_len+1),'min_price':min_price,'max_price':max_price,'minMaxPrice':minMaxPrice,
                        'filtered_electronics':filtered_electronics}
    return render(request, 'ascending_products_home.html',params)


def descending_products_wears(request):
    no_of_posts = 15
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    descending_prod_wears=Product.objects.filter(category = 'wears').order_by('-price')
    length = len(descending_prod_wears)
    descending_prod_wears= descending_prod_wears[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts)
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    minMaxPrice=Product.objects.aggregate(Min('price'),Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    filtered_price=request.GET.get('filter')
    filtered_wears=Product.objects.filter(price__range=(price_min,filtered_price),category = 'wears').order_by('-price')
    params = {'descending_prod_wears':descending_prod_wears,'prev':prev, 'nxt':nxt,'page_len':range(1,page_len+1),
    'min_price':min_price,'max_price':max_price,'minMaxPrice':minMaxPrice,
    'filtered_wears':filtered_wears}
    return render(request, 'ascending_products_home.html',params)


def ascending_products_wears(request):
    no_of_posts = 15
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    ascending_prod_wears=Product.objects.filter(category= 'wears').order_by('-price')[::-1]
    length = len(ascending_prod_wears)
    ascending_prod_wears= ascending_prod_wears[(page-1)*no_of_posts: page*no_of_posts]

    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts)
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    minMaxPrice=Product.objects.aggregate(Min('price'),Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    filtered_price=request.GET.get('filter')
    filtered_wears=Product.objects.filter(price__range=(price_min,filtered_price),category = 'wears').order_by('-price')[::-1]
    params = {'ascending_prod_wears':ascending_prod_wears,'prev':prev, 'nxt':nxt,'page_len':range(1,page_len+1),
    'min_price':min_price,'max_price':max_price,'minMaxPrice':minMaxPrice,
    'filtered_wears':filtered_wears}

    return render(request, 'ascending_products_home.html',params)

def ascending_prod_mobile(request):
    no_of_posts = 15
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    ascending_prod_mobile=Product.objects.filter(sub_category= 'mobile').order_by('-price')[::-1]
    length = len(ascending_prod_mobile)
    ascending_prod_mobile= ascending_prod_mobile[(page-1)*no_of_posts: page*no_of_posts]
    # print(ascending_prod_mobile)
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts)
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    minMaxPrice=Product.objects.filter(sub_category='mobile').aggregate(Min('price'),Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    filtered_price=request.GET.get('filter')
    filtered_prod_mobile=Product.objects.filter(price__range=(price_min,filtered_price),sub_category='mobile').order_by('-price')[::-1]
    params = {'ascending_prod_mobile':ascending_prod_mobile,'prev':prev, 'nxt':nxt,'page_len':range(1,page_len+1),
    'min_price':min_price,'max_price':max_price,'minMaxPrice':minMaxPrice,
    'filtered_prod_mobile':filtered_prod_mobile}
    
    return render(request, 'ascending_products_home.html',params)

def descending_prod_mobile(request):
    no_of_posts = 15
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    descending_prod_mobile=Product.objects.filter(sub_category= 'mobile').order_by('-price')[::-1]
    length = len(descending_prod_mobile)
    descending_prod_mobile= descending_prod_mobile[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts)
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    minMaxPrice=Product.objects.filter(sub_category='mobile').aggregate(Min('price'),Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    filtered_price=request.GET.get('filter')
    filtered_prod_mobile=Product.objects.filter(price__range=(price_min,filtered_price),sub_category='mobile').order_by('-price')
    params = {'descending_prod_mobile':descending_prod_mobile,'prev':prev, 'nxt':nxt,'page_len':range(1,page_len+1),
    'min_price':min_price,'max_price':max_price,'minMaxPrice':minMaxPrice,
    'filtered_prod_mobile':filtered_prod_mobile}
    
    return render(request, 'ascending_products_home.html',params)

def ascending_prod_laptop(request):
    no_of_posts = 15
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    ascending_prod_laptop=Product.objects.filter(sub_category= 'laptop').order_by('-price')[::-1]
    length = len(ascending_prod_laptop)
    ascending_prod_laptop= ascending_prod_laptop[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts)
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    minMaxPrice=Product.objects.filter(sub_category='laptop').aggregate(Min('price'),Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    filtered_price=request.GET.get('filter')
    filtered_prod_laptop=Product.objects.filter(price__range=(price_min,filtered_price),sub_category='laptop').order_by('-price')
    params = {'ascending_prod_laptop':ascending_prod_laptop,'prev':prev, 'nxt':nxt,'page_len':range(1,page_len+1),
    'min_price':min_price,'max_price':max_price,'minMaxPrice':minMaxPrice,
    'filtered_prod_laptop':filtered_prod_laptop}
    
    return render(request, 'ascending_products_home.html',params)

def descending_prod_laptop(request):
    no_of_posts = 4
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
        
    descending_prod_laptop=Product.objects.filter(sub_category= 'laptop').order_by('-price')
    length = len(descending_prod_laptop)
    descending_prod_laptop= descending_prod_laptop[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts)
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    minMaxPrice=Product.objects.filter(sub_category='laptop').aggregate(Min('price'),Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    filtered_price=request.GET.get('filter')
    filtered_prod_laptop=Product.objects.filter(price__range=(price_min,filtered_price),sub_category='laptop').order_by('-price')
    params = {'descending_prod_laptop':descending_prod_laptop,'prev':prev, 'nxt':nxt,'page_len':range(1,page_len+1),
    'min_price':min_price,'max_price':max_price,'minMaxPrice':minMaxPrice,
    'filtered_prod_laptop':filtered_prod_laptop}
    
    return render(request, 'ascending_products_home.html',params)

def descending_prod_tv(request):
    no_of_posts = 4
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    descending_prod_tv=Product.objects.filter(sub_category= 'tv').order_by('-price')
    length = len(descending_prod_tv)
    descending_prod_tv= descending_prod_tv[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts)
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    minMaxPrice=Product.objects.filter(sub_category='tv').aggregate(Min('price'),Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    filtered_price=request.GET.get('filter')
    filtered_prod_tv=Product.objects.filter(price__range=(price_min,filtered_price),sub_category='tv').order_by('-price')
    params = {'descending_prod_tv':descending_prod_tv,'prev':prev, 'nxt':nxt,'page_len':range(1,page_len+1),
    'min_price':min_price,'max_price':max_price,'minMaxPrice':minMaxPrice,
    'filtered_prod_tv':filtered_prod_tv}
    
    return render(request, 'ascending_products_home.html',params)

def ascending_prod_tv(request):
    no_of_posts = 4
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    ascending_prod_tv=Product.objects.filter(sub_category='tv').order_by('-price')[::-1]
    length = len(ascending_prod_tv)
    ascending_prod_tv= ascending_prod_tv[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts)
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    minMaxPrice=Product.objects.filter(sub_category='tv').aggregate(Min('price'),Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    filtered_price=request.GET.get('filter')
    filtered_prod_tv=Product.objects.filter(price__range=(price_min,filtered_price),sub_category='tv').order_by('-price')[::-1]
    params = {'ascending_prod_tv':ascending_prod_tv,'prev':prev, 'nxt':nxt,'page_len':range(1,page_len+1),
    'min_price':min_price,'max_price':max_price,'minMaxPrice':minMaxPrice,
    'filtered_prod_tv':filtered_prod_tv}
    
    return render(request, 'ascending_products_home.html',params)

def ascending_prod_tablet(request):
    no_of_posts = 4
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    ascending_prod_tablet=Product.objects.filter(sub_category= 'tablets').order_by('-price')[::-1]
    length = len(ascending_prod_tablet)
    ascending_prod_tablet= ascending_prod_tablet[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts)
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    minMaxPrice=Product.objects.filter(sub_category='tablets').aggregate(Min('price'),Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    filtered_price=request.GET.get('filter')
    filtered_prod_tablet=Product.objects.filter(price__range=(price_min,filtered_price),sub_category='tablets').order_by('-price')
    params = {'ascending_prod_tablet':ascending_prod_tablet,'prev':prev, 'nxt':nxt,'page_len':range(1,page_len+1),
    'min_price':min_price,'max_price':max_price,'minMaxPrice':minMaxPrice,
    'filtered_prod_tablet':filtered_prod_tablet}
    
    return render(request, 'ascending_products_home.html',params)

def descending_prod_tablet(request):
    no_of_posts = 4
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    descending_prod_tablet=Product.objects.filter(sub_category= 'tablets').order_by('-price')
    length = len(descending_prod_tablet)
    descending_prod_tablet= descending_prod_tablet[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts)
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    minMaxPrice=Product.objects.filter(sub_category='tablets').aggregate(Min('price'),Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    filtered_price=request.GET.get('filter')
    filtered_prod_tablet=Product.objects.filter(price__range=(price_min,filtered_price),sub_category='tablets').order_by('-price')
    params = {'descending_prod_tablet':descending_prod_tablet,'prev':prev, 'nxt':nxt,'page_len':range(1,page_len+1),
    'min_price':min_price,'max_price':max_price,'minMaxPrice':minMaxPrice,
    'filtered_prod_tablet':filtered_prod_tablet}
    
    return render(request, 'ascending_products_home.html',params)

def descending_prod_smart_watches(request):
    no_of_posts = 4
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    descending_prod_smart_watches=Product.objects.filter(sub_category= 'watches').order_by('-price')
    print(descending_prod_smart_watches)
    length = len(descending_prod_smart_watches)
    descending_prod_smart_watches = descending_prod_smart_watches[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts)
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    minMaxPrice=Product.objects.filter(sub_category='watches').aggregate(Min('price'),Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    filtered_price=request.GET.get('filter')
    filtered_prod_smart_watch=Product.objects.filter(price__range=(price_min,filtered_price),sub_category='watches').order_by('-price')
    params = {'descending_prod_smart_watches':descending_prod_smart_watches,'prev':prev, 'nxt':nxt,'page_len':range(1,page_len+1),
    'min_price':min_price,'max_price':max_price,'minMaxPrice':minMaxPrice,
    'filtered_prod_smart_watch':filtered_prod_smart_watch}
    
    return render(request, 'ascending_products_home.html',params)

def ascending_prod_smart_watches(request):
    no_of_posts = 4
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    ascending_prod_smart_watches=Product.objects.filter(sub_category= 'watches').order_by('-price')
    length = len(ascending_prod_smart_watches)
    ascending_prod_smart_watches= ascending_prod_smart_watches[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts)
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    minMaxPrice=Product.objects.filter(sub_category='watches').aggregate(Min('price'),Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    filtered_price=request.GET.get('filter')
    filtered_prod_smart_watch=Product.objects.filter(price__range=(price_min,filtered_price),sub_category='watches').order_by('-price')
    params = {'ascending_prod_smart_watches':ascending_prod_smart_watches,'prev':prev, 'nxt':nxt,'page_len':range(1,page_len+1),
    'min_price':min_price,'max_price':max_price,'minMaxPrice':minMaxPrice,
    'filtered_prod_smart_watch':filtered_prod_smart_watch}
    
    return render(request, 'ascending_products_home.html',params)

def descending_prod_camera(request):
    no_of_posts = 4
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    descending_prod_camera=Product.objects.filter(sub_category= 'camera').order_by('-price')
    print(descending_prod_camera)
    length = len(descending_prod_camera)
    descending_prod_camera = descending_prod_camera[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts)
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    
    price_min=minMaxPrice.get('price__min')
    # print(price_min)
    price_max=minMaxPrice.get('price__max')
    filtered_price=request.GET.get('filter')
    filtered_prod_camera=Product.objects.filter(price__range=(price_min,filtered_price),sub_category='camera').order_by('-price')
    params = {'descending_prod_camera':descending_prod_camera,'prev':prev, 'nxt':nxt,'page_len':range(1,page_len+1),
    'min_price':min_price,'max_price':max_price,'minMaxPrice':minMaxPrice,
    'filtered_prod_camera':filtered_prod_camera}
    
    return render(request, 'ascending_products_home.html',params)


def search(request): 
    if 'term' in request.GET:
        qs = Product.objects.filter(product_name__icontains=request.GET.get('term'))
        qs2 = Product.objects.filter(sub_category__icontains=request.GET.get('term'))
        titles = list()
        for product in qs:
            titles.append(product.product_name)
        for i in qs2:
            if i.sub_category in titles:
                continue
            else:

                titles.append(i.sub_category)
        return JsonResponse(titles, safe=False)

    query=request.GET['query']
    searched_item = New_Product2(query=query)
    searched_item.save()
    num =10
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    minMaxPrice = Product.objects.aggregate(Min('price'),Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    filtered_price=request.GET.get('search_filter')

    if query is None:
        print('search is none',query)
    elif len(query)>158:
        allPosts=Product.objects.none()
    else:
        Product_name = Product.objects.filter(product_name__icontains=query)
        Product_category= Product.objects.filter(category__icontains=query)
        # allPostsContent = Product.objects.filter(desc__icontains=query)
        Product_Sub_cat = Product.objects.filter(sub_category__icontains=query)
        Price_filter = Product.objects.filter(price__range=(price_min,filtered_price))
        product=  Product_name.union(Product_category,Price_filter,Product_Sub_cat).order_by('product_name')
        minMaxPrice= Product.objects.filter(product_name__icontains=query).aggregate(Min('price'),Max('price'))
        price_min=minMaxPrice.get('price__min')
        price_max=minMaxPrice.get('price__max')
        ascending_allposts = Product_name.union(Product_category).order_by('-price')[::-1]
        no_of_posts = 15
        page = request.GET.get('page')
        if page is None: 
            page = 1
        else:
            page = int(page)
        
        length = len(product)
        product = product[(page-1)*no_of_posts: page*no_of_posts]
        if page>1:
            prev = page - 1
        else:
            prev = None
        if page<math.ceil(length/ no_of_posts):
            nxt = page + 1
        else:
            nxt = None

        page_len=math.ceil(length/ no_of_posts)
            
    params={'product': product, 'query': query,'ascending_allposts':ascending_allposts,'min_price':min_price,
    'max_price':max_price,'minMaxPrice':minMaxPrice,
    'prev':prev, 'nxt':nxt}
    return render(request,'search.html' , params)


def searched_filter(request):
    no_of_posts = 20
    searched_item = New_Product2.objects.last()
    query = searched_item.query

    if len(query)>158:
        product =Product.objects.none()
    else:
        Product_name = Product.objects.filter(product_name__icontains=query)
        Product_brand = Product.objects.filter(brand__icontains=query)
        Product_category = Product.objects.filter(category__icontains=query)
        Product_Sub_cat = Product.objects.filter(sub_category__icontains=query)
        low_high = request.GET.get('ascending')
        if low_high is None:
            product = Product_name.union(Product_category,Product_Sub_cat,Product_brand).order_by('product_name')
            Low_High = None
        elif low_high == "ascending":
            Low_High = None
            product =  Product_name.union(Product_category,Product_Sub_cat,Product_brand).order_by('price')
        elif low_high == "descending":
            Low_High = None
            product =  Product_name.union(Product_category,Product_Sub_cat,Product_brand,).order_by('price')[::-1]
        else:            
            Low_High = None

        minMaxPrice= Product.objects.filter(product_name__icontains=query).aggregate(Min('price'),Max('price'))
        minMaxPrice2 = Product.objects.filter(sub_category__icontains=query).aggregate(Min('price'),Max('price'))
        price_min=minMaxPrice.get('price__min')
        price_max=minMaxPrice.get('price__max')

        price_1= price_max - price_min // 4
        price_2 = price_max - price_min // 3
        price_3 = price_max - price_min // 2
      
        filtered_price = request.GET.get('filter')
        if filtered_price is None:
            filtered_price = None 
            price_range_filter = None
            
        else:
            price_range_filter = Product_name.filter(price__range=(price_min,filtered_price)).union(Product_category,Product_Sub_cat).order_by('product_name').order_by('-price')[::-1]
        
        no_of_posts = 15
        page = request.GET.get('page')
        if page is None: 
            page = 1
        else:
            page = int(page)
        
        length = len(product)
        page_len=math.ceil(length/ no_of_posts)
        product= product[(page-1)*no_of_posts: page*no_of_posts]
        if page>1:
            prev = page - 1
        else:
            prev = None
        if page<math.ceil(length/ no_of_posts):
            nxt = page + 1
        else:
            nxt = None
        if price_range_filter is not None:
           
            length_filter = len(price_range_filter)
            page_len_filter=math.ceil(length_filter/ no_of_posts)
            price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    params={'product': product, 'query': query,'filtered_price':filtered_price,
    'price_range_filter':price_range_filter,"Low_High":Low_High,'low_high':low_high,
    'minMaxPrice':minMaxPrice,'price_1':price_1,'price_2':price_2,'price_3':price_3,
    'prev':prev, 'nxt':nxt,'page_len':range(1,page_len+1)}
    return render(request,'search.html' , params)

def ascending_products_search(request,num):
    # print('ascending_allposts',num)
    no_of_posts = 4
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    ascending_prod_search=Product.objects.filter(sub_category= 'wears').order_by('-price')[::-1]
    length = len(ascending_prod_search)
    ascending_prod_search= ascending_prod_search[(page-1)*no_of_posts: page*no_of_posts]

    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts)
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    minMaxPrice=Product.objects.aggregate(Min('price'),Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    
    return render(request, 'ascending_products_home.html',{'ascending_prod_search':ascending_prod_search,'prev':prev, 'nxt':nxt,'page_len':range(1,page_len+1),'min_price':min_price,
    'max_price':max_price,'minMaxPrice':minMaxPrice})


def shoes(request):
    no_of_posts = 4
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    shoes=Product.objects.filter(sub_category= 'shoes')
    length = len(shoes)
    shoes= shoes[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    return render(request, 'shoes.html',{'shoes':shoes,'prev':prev, 'nxt':nxt})
    

def wears(request):
    no_of_posts = 4
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    wears=Product.objects.filter(category= 'wears')
    length = len(wears)
    wears= wears[(page-1)*no_of_posts: page*no_of_posts]
    page_len=math.ceil(length/ no_of_posts)

    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    minMaxPrice=Product.objects.aggregate(Min('price'),Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    filtered_price=request.GET.get('filter')
    filtered=Product.objects.filter(price__range=(filtered_price,price_max))
    params={'wears':wears,'prev':prev, 'nxt':nxt,'min_price':min_price,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'filtered':filtered,'page_len':range(1,page_len+1)}

    return render(request, 'wears.html',params)


def wears_men(request):
    no_of_posts = 4
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    wears_men=Product.objects.filter(sub_category= 'male')
    length = len(wears_men)
    wears_men= wears_men[(page-1)*no_of_posts: page*no_of_posts]
    page_len=math.ceil(length/ no_of_posts)

    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    minMaxPrice=Product.objects.aggregate(Min('price'),Max('price'))
    # filtered_price =Product.objects.filter(price__range=())
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    filtered_price=request.GET.get('filter')
    filtered=Product.objects.filter(price__range=(filtered_price,price_max))
    params={'wears_men':wears_men,'prev':prev, 'nxt':nxt,'min_price':min_price,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'filtered':filtered,'page_len':range(1,page_len+1)}

    return render(request, 'wears.html',params)


def wears_women(request):
    no_of_posts = 4
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    wears_women=Product.objects.filter(sub_category= 'female')
    length = len(wears_women)
    wears_women= wears_women[(page-1)*no_of_posts: page*no_of_posts]
    page_len=math.ceil(length/ no_of_posts)

    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    minMaxPrice=Product.objects.aggregate(Min('price'),Max('price'))
    # filtered_price =Product.objects.filter(price__range=())
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    filtered_price=request.GET.get('filter')
    filtered=Product.objects.filter(price__range=(filtered_price,price_max))
    params={'wears_women':wears_women,'prev':prev, 'nxt':nxt,'min_price':min_price,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'filtered':filtered,'page_len':range(1,page_len+1)}
    return render(request, 'wears.html',params)

    
def electronics(request):
    category = 'electronics'
    price_1= 10000
    price_2 = 20000
    price_3 = 30000
    img_height = 150
    img_width = 80
    no_of_posts = 20
    value = request.GET.get('electronics_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(category=category).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(category=category)        
    elif value =='price_1':
        product=Product.objects.filter(category=category).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(category=category).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(category=category).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(category=category).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(category=category).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),category=category).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'category':category,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'electronics.html',params)


def laptop_brand_hp(request):
    sub_cat = 'laptop'
    brand_url = 'laptop_brand_hp'
    brand_type = 'hp'
    price_1= 40000
    price_2 = 50000
    price_3 = 60000
    img_height = 100
    img_width = 150
    no_of_posts = 20
    value = request.GET.get('laptop_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        brand_product = Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type)
    elif value =='price_1':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(brand_product)
    brand_product = brand_product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    brand_price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).filter(brand=brand_type).order_by('-price')[::-1]
    length_filter = len(brand_price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    brand_price_range_filter = brand_price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'brand_product':brand_product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'brand_price_range_filter':brand_price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1),
    'brand_type':brand_type,'brand_url':brand_url}
    return render(request, 'laptop.html',params)


def laptop_brand_dell(request):
    sub_cat = 'laptop'
    brand_url = 'laptop_brand_dell'
    brand_type = 'dell'
    price_1= 40000
    price_2 = 50000
    price_3 = 60000
    img_height = 100
    img_width = 150
    no_of_posts = 20
    value = request.GET.get('laptop_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        brand_product = Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type)
    elif value =='price_1':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(brand_product)
    brand_product = brand_product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    brand_price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).filter(brand=brand_type).order_by('-price')[::-1]
    length_filter = len(brand_price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    brand_price_range_filter = brand_price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'brand_product':brand_product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'brand_price_range_filter':brand_price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1),
    'brand_type':brand_type,'brand_url':brand_url}
    return render(request, 'laptop.html',params)

def laptop_brand_asus(request):
    sub_cat = 'laptop'
    brand_url = 'laptop_brand_asus'
    brand_type = 'asus'
    price_1= 40000
    price_2 = 50000
    price_3 = 60000
    img_height = 100
    img_width = 150
    no_of_posts = 20
    value = request.GET.get('laptop_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        brand_product = Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type)
    elif value =='price_1':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(brand_product)
    brand_product = brand_product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    brand_price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).filter(brand=brand_type).order_by('-price')[::-1]
    length_filter = len(brand_price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    brand_price_range_filter = brand_price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'brand_product':brand_product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'brand_price_range_filter':brand_price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1),
    'brand_type':brand_type,'brand_url':brand_url}
    return render(request, 'laptop.html',params)

def laptop_brand_lenovo(request):
    sub_cat = 'laptop'
    brand_url = 'laptop_brand_lenovo'
    brand_type = 'lenovo'
    price_1= 40000
    price_2 = 50000
    price_3 = 60000
    img_height = 100
    img_width = 150
    no_of_posts = 20
    value = request.GET.get('laptop_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        brand_product = Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type)
    elif value =='price_1':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(brand_product)
    brand_product = brand_product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    brand_price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).filter(brand=brand_type).order_by('-price')[::-1]
    length_filter = len(brand_price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    brand_price_range_filter = brand_price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'brand_product':brand_product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'brand_price_range_filter':brand_price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1),
    'brand_type':brand_type,'brand_url':brand_url}
    return render(request, 'laptop.html',params)

def laptop_brand_samsung(request):
    sub_cat = 'laptop'
    brand_url = 'laptop_brand_samsung'
    brand_type = 'samsung'
    price_1= 40000
    price_2 = 50000
    price_3 = 60000
    img_height = 100
    img_width = 150
    no_of_posts = 20
    value = request.GET.get('laptop_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        brand_product = Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type)
    elif value =='price_1':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(brand_product)
    brand_product = brand_product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    brand_price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).filter(brand=brand_type).order_by('-price')[::-1]
    length_filter = len(brand_price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    brand_price_range_filter = brand_price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'brand_product':brand_product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'brand_price_range_filter':brand_price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1),
    'brand_type':brand_type,'brand_url':brand_url}
    return render(request, 'laptop.html',params)

def laptop_brand_lg(request):
    sub_cat = 'laptop'
    brand_url = 'laptop_brand_lg'
    brand_type = 'lg'
    price_1= 40000
    price_2 = 50000
    price_3 = 60000
    img_height = 100
    img_width = 150
    no_of_posts = 20
    value = request.GET.get('laptop_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        brand_product = Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type)
    elif value =='price_1':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(brand_product)
    brand_product = brand_product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    brand_price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).filter(brand=brand_type).order_by('-price')[::-1]
    length_filter = len(brand_price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    brand_price_range_filter = brand_price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'brand_product':brand_product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'brand_price_range_filter':brand_price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1),
    'brand_type':brand_type,'brand_url':brand_url}
    return render(request, 'laptop.html',params)

def laptop_brand_acer(request):
    sub_cat = 'laptop'
    brand_url = 'laptop_brand_acer'
    brand_type = 'acer'
    price_1= 40000
    price_2 = 50000
    price_3 = 60000
    img_height = 100
    img_width = 150
    no_of_posts = 20
    value = request.GET.get('laptop_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        brand_product = Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type)
    elif value =='price_1':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(brand_product)
    brand_product = brand_product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    brand_price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).filter(brand=brand_type).order_by('-price')[::-1]
    length_filter = len(brand_price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    brand_price_range_filter = brand_price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'brand_product':brand_product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'brand_price_range_filter':brand_price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1),
    'brand_type':brand_type,'brand_url':brand_url}
    return render(request, 'laptop.html',params)

def laptop_brand_redmi(request):
    sub_cat = 'laptop'
    brand_url = 'laptop_brand_redmi'
    brand_type = 'redmi'
    price_1= 40000
    price_2 = 50000
    price_3 = 60000
    img_height = 100
    img_width = 150
    no_of_posts = 20
    value = request.GET.get('laptop_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        brand_product = Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type)
    elif value =='price_1':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(brand_product)
    brand_product = brand_product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    brand_price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).filter(brand=brand_type).order_by('-price')[::-1]
    length_filter = len(brand_price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    brand_price_range_filter = brand_price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'brand_product':brand_product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'brand_price_range_filter':brand_price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1),
    'brand_type':brand_type,'brand_url':brand_url}
    return render(request, 'laptop.html',params)

def laptop(request):
    sub_cat = 'laptop'
    price_1= 40000
    price_2 = 50000
    price_3 = 60000
    img_height = 80
    img_width = 140
    no_of_posts = 20
    value = request.GET.get('laptop_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'laptop.html',params)






def tv(request):
    no_of_posts = 4
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    tv=Product.objects.filter(sub_category= 'tv')
    length = len(tv)
    tv= tv[(page-1)*no_of_posts: page*no_of_posts]

    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts)  
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    minMaxPrice=Product.objects.filter(sub_category='tv').aggregate(Min('price'),Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    filtered_price=request.GET.get('filter')
    filtered_tv=Product.objects.filter(price__range=(price_min,filtered_price),sub_category='tv').order_by('-price')[::-1]
    params = {'tv':tv,'prev':prev, 'nxt':nxt,'page_len':range(1,page_len+1),
    'min_price':min_price,'max_price':max_price,'minMaxPrice':minMaxPrice,'filtered_price':filtered_price,
    'filtered_tv':filtered_tv}
    return render(request, 'laptop.html',params)


def tablet(request):
    no_of_posts = 4
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    tablet=Product.objects.filter(sub_category= 'tablets')
    length = len(tablet)
    tablet= tablet[(page-1)*no_of_posts: page*no_of_posts]

    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts)  
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    minMaxPrice=Product.objects.filter(sub_category='tablets').aggregate(Min('price'),Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    filtered_price=request.GET.get('filter')
    filtered_tablet=Product.objects.filter(price__range=(price_min,filtered_price),sub_category='tablets').order_by('-price')[::-1]
    params = {'tablet':tablet,'prev':prev, 'nxt':nxt,'page_len':range(1,page_len+1),
    'min_price':min_price,'max_price':max_price,'minMaxPrice':minMaxPrice,'filtered_price':filtered_price,
    'filtered_tablet':filtered_tablet}
    return render(request, 'mobile.html',params)


def mobile(request):
    sub_cat = 'mobile'
    price_1= 10000
    price_2 = 20000
    price_3 = 30000
    img_height = 150
    img_width = 80
    no_of_posts = 20
    value = request.GET.get('mobile_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'mobile.html',params)




# Mobile-Brands-

def mobile_brand_redmi(request):
    sub_cat = 'mobile'
    brand_url = 'mobile_brand_redmi'
    brand_type = 'redmi'
    price_1= 10000
    price_2 = 15000
    price_3 = 20000
    img_height = 150
    img_width = 80
    no_of_posts = 20
    value = request.GET.get('mobile_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        brand_product = Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type)
    elif value =='price_1':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(brand_product)
    brand_product = brand_product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    brand_price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).filter(brand=brand_type).order_by('-price')[::-1]
    length_filter = len(brand_price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    brand_price_range_filter = brand_price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'brand_product':brand_product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'brand_price_range_filter':brand_price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1),
    'brand_type':brand_type,'brand_url':brand_url}
    return render(request, 'mobile.html',params)

def mobile_brand_samsung(request):
    sub_cat = 'mobile'
    brand_url = 'mobile_brand_samsung'
    brand_type = 'samsung'
    price_1= 10000
    price_2 = 15000
    price_3 = 20000
    img_height = 150
    img_width = 80
    no_of_posts = 20
    value = request.GET.get('mobile_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        brand_product = Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type)   
    elif value =='price_1':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(brand_product)
    brand_product = brand_product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    brand_price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).filter(brand=brand_type).order_by('-price')[::-1]
    length_filter = len(brand_price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    brand_price_range_filter = brand_price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'brand_product':brand_product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'brand_price_range_filter':brand_price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1),
    'brand_type':brand_type,'brand_url':brand_url}
    return render(request, 'mobile.html',params)

def mobile_brand_realme(request):
    sub_cat = 'mobile'
    brand_url = 'mobile_brand_realme'
    brand_type = 'realme'
    price_1= 10000
    price_2 = 15000
    price_3 = 20000
    img_height = 150
    img_width = 80
    no_of_posts = 20
    value = request.GET.get('mobile_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        brand_product = Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type)       
    elif value =='price_1':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(brand_product)
    brand_product = brand_product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    brand_price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).filter(brand=brand_type).order_by('-price')[::-1]
    length_filter = len(brand_price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    brand_price_range_filter = brand_price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'brand_product':brand_product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'brand_price_range_filter':brand_price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1),
    'brand_type':brand_type,'brand_url':brand_url}
    return render(request, 'mobile.html',params)

def mobile_brand_vivo(request):
    sub_cat = 'mobile'
    brand_url = 'mobile_brand_vivo'
    brand_type = 'vivo'
    price_1= 10000
    price_2 = 15000
    price_3 = 20000
    img_height = 150
    img_width = 80
    no_of_posts = 20
    value = request.GET.get('mobile_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        brand_product = Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type)    
    elif value =='price_1':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(brand_product)
    brand_product = brand_product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    brand_price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).filter(brand=brand_type).order_by('-price')[::-1]
    length_filter = len(brand_price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    brand_price_range_filter = brand_price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'brand_product':brand_product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'brand_price_range_filter':brand_price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1),
    'brand_type':brand_type,'brand_url':brand_url}
    return render(request, 'mobile.html',params)

def mobile_brand_oppo(request):
    sub_cat = 'mobile'
    brand_url = 'mobile_brand_oppo'
    brand_type = 'oppo'
    price_1= 10000
    price_2 = 15000
    price_3 = 20000
    img_height = 150
    img_width = 80
    no_of_posts = 20
    value = request.GET.get('mobile_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        brand_product = Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type)      
    elif value =='price_1':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(brand_product)
    brand_product = brand_product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    brand_price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).filter(brand=brand_type).order_by('-price')[::-1]
    length_filter = len(brand_price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    brand_price_range_filter = brand_price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'brand_product':brand_product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'brand_price_range_filter':brand_price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1),
    'brand_type':brand_type,'brand_url':brand_url}
    return render(request, 'mobile.html',params)

def mobile_brand_poco(request):
    sub_cat = 'mobile'
    brand_url = 'mobile_brand_poco'
    brand_type = 'poco'
    price_1= 10000
    price_2 = 15000
    price_3 = 20000
    img_height = 150
    img_width = 80
    no_of_posts = 20
    value = request.GET.get('mobile_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        brand_product = Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type)        
    elif value =='price_1':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(brand_product)
    brand_product = brand_product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    brand_price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).filter(brand=brand_type).order_by('-price')[::-1]
    length_filter = len(brand_price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    brand_price_range_filter = brand_price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'brand_product':brand_product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'brand_price_range_filter':brand_price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1),
    'brand_type':brand_type,'brand_url':brand_url}
    return render(request, 'mobile.html',params)

def mobile_brand_apple(request):
    sub_cat = 'mobile'
    brand_url = 'mobile_brand_apple'
    brand_type = 'apple'
    price_1= 25000
    price_2 = 30000
    price_3 = 40000
    img_height = 150
    img_width = 80
    no_of_posts = 20
    value = request.GET.get('mobile_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        brand_product = Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type)      
    elif value =='price_1':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(brand_product)
    brand_product = brand_product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    brand_price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).filter(brand=brand_type).order_by('-price')[::-1]
    length_filter = len(brand_price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    brand_price_range_filter = brand_price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'brand_product':brand_product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'brand_price_range_filter':brand_price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1),
    'brand_type':brand_type,'brand_url':brand_url}
    return render(request, 'mobile.html',params)

def mobile_brand_nokia(request):
    sub_cat = 'mobile'
    brand_url = 'mobile_brand_nokia'
    brand_type = 'nokia'
    price_1= 10000
    price_2 = 15000
    price_3 = 20000
    img_height = 150
    img_width = 80
    no_of_posts = 20
    value = request.GET.get('mobile_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        brand_product = Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type)      
    elif value =='price_1':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(brand_product)
    brand_product = brand_product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    brand_price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).filter(brand=brand_type).order_by('-price')[::-1]
    length_filter = len(brand_price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    brand_price_range_filter = brand_price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'brand_product':brand_product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'brand_price_range_filter':brand_price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1),
    'brand_type':brand_type,'brand_url':brand_url}
    return render(request, 'mobile.html',params)

def mobile_brand_oneplus(request):
    sub_cat = 'mobile'
    brand_url = 'mobile_brand_oneplus'
    brand_type = 'oneplus'
    price_1= 15000
    price_2 = 25000
    price_3 = 25000
    img_height = 150
    img_width = 80
    no_of_posts = 20
    value = request.GET.get('mobile_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        brand_product = Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type)      
    elif value =='price_1':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(brand_product)
    brand_product = brand_product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    brand_price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).filter(brand=brand_type).order_by('-price')[::-1]
    length_filter = len(brand_price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    brand_price_range_filter = brand_price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'brand_product':brand_product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'brand_price_range_filter':brand_price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1),
    'brand_type':brand_type,'brand_url':brand_url}
    return render(request, 'mobile.html',params)

def mobile_brand_infinix(request):
    sub_cat = 'mobile'
    brand_url = 'mobile_brand_infinix'
    brand_type = 'infinix'
    price_1= 10000
    price_2 = 15000
    price_3 = 20000
    img_height = 150
    img_width = 80
    no_of_posts = 20
    value = request.GET.get('mobile_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        brand_product = Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type)      
    elif value =='price_1':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(brand_product)
    brand_product = brand_product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    brand_price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).filter(brand=brand_type).order_by('-price')[::-1]
    length_filter = len(brand_price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    brand_price_range_filter = brand_price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'brand_product':brand_product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'brand_price_range_filter':brand_price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1),
    'brand_type':brand_type,'brand_url':brand_url}
    return render(request, 'mobile.html',params)

    no_of_posts = 20
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category='mobile').filter(brand='infinix').aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    value = request.GET.get('mobile_price_range')
    value = request.GET.get('mobile_price_range')
    if value is None:
        brand_fil_mobile = Product.objects.filter(brand='infinix').filter(sub_category='mobile')        
    elif value =='price_under10000':
        brand_fil_mobile=Product.objects.filter(brand='infinix').filter(sub_category='mobile').filter(price__range=(1,10000)).order_by('-price')[::-1]
    elif value =='price_10000_to_15000':
        brand_fil_mobile=Product.objects.filter(brand='infinix').filter(sub_category='mobile').filter(price__range=(10000,15000)).order_by('-price')[::-1]
    elif value =='price_15000_to_25000':
        brand_fil_mobile=Product.objects.filter(brand='infinix').filter(sub_category='mobile').filter(price__range=(15000,25000)).order_by('-price')[::-1]
    elif value =='price_over_25000':
        brand_fil_mobile=Product.objects.filter(brand='infinix').filter(sub_category='mobile').filter(price__range=(25000,price_max)).order_by('-price')[::-1]
            
    length = len(brand_fil_mobile)
    brand_fil_mobile= brand_fil_mobile[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    brand_type = 'infinix'
    minMaxPrice=Product.objects.filter(brand='infinix').aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    brand_fill_filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,brand_fill_filtered_price),sub_category='mobile').filter(brand='infinix').order_by('-price')[::-1]
   
    params= {'brand_fil_mobile':brand_fil_mobile,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'value':value,'brand_type':brand_type,
    'ascending_prod_laptop':ascending_prod_laptop,'descending_prod_laptop':descending_prod_laptop,'price_range_filter':price_range_filter,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'mobile.html',params)

def mobile_brand_asus(request):
    sub_cat = 'mobile'
    brand_url = 'mobile_brand_asus'
    brand_type = 'asus'
    price_1= 10000
    price_2 = 15000
    price_3 = 20000
    img_height = 150
    img_width = 80
    no_of_posts = 20
    value = request.GET.get('mobile_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        brand_product = Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type)      
    elif value =='price_1':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(brand_product)
    brand_product = brand_product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    brand_price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).filter(brand=brand_type).order_by('-price')[::-1]
    length_filter = len(brand_price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    brand_price_range_filter = brand_price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'brand_product':brand_product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'brand_price_range_filter':brand_price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1),
    'brand_type':brand_type,'brand_url':brand_url}
    return render(request, 'mobile.html',params)

    no_of_posts = 20
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category='mobile').filter(brand='infinix').aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    value = request.GET.get('mobile_price_range')
    value = request.GET.get('mobile_price_range')
    if value is None:
        brand_fil_mobile = Product.objects.filter(brand='infinix').filter(sub_category='mobile')        
    elif value =='price_under10000':
        brand_fil_mobile=Product.objects.filter(brand='infinix').filter(sub_category='mobile').filter(price__range=(1,10000)).order_by('-price')[::-1]
    elif value =='price_10000_to_15000':
        brand_fil_mobile=Product.objects.filter(brand='infinix').filter(sub_category='mobile').filter(price__range=(10000,15000)).order_by('-price')[::-1]
    elif value =='price_15000_to_25000':
        brand_fil_mobile=Product.objects.filter(brand='infinix').filter(sub_category='mobile').filter(price__range=(15000,25000)).order_by('-price')[::-1]
    elif value =='price_over_25000':
        brand_fil_mobile=Product.objects.filter(brand='infinix').filter(sub_category='mobile').filter(price__range=(25000,price_max)).order_by('-price')[::-1]
            
    length = len(brand_fil_mobile)
    brand_fil_mobile= brand_fil_mobile[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    brand_type = 'infinix'
    minMaxPrice=Product.objects.filter(brand='infinix').aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    brand_fill_filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,brand_fill_filtered_price),sub_category='mobile').filter(brand='infinix').order_by('-price')[::-1]
   
    params= {'brand_fil_mobile':brand_fil_mobile,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'value':value,'brand_type':brand_type,
    'ascending_prod_laptop':ascending_prod_laptop,'descending_prod_laptop':descending_prod_laptop,'price_range_filter':price_range_filter,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'mobile.html',params)

def mobile_brand_techno(request):
    sub_cat = 'mobile'
    brand_url = 'mobile_brand_techno'
    brand_type = 'techno'
    price_1= 10000
    price_2 = 15000
    price_3 = 20000
    img_height = 150
    img_width = 80
    no_of_posts = 20
    value = request.GET.get('mobile_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        brand_product = Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type)      
    elif value =='price_1':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(brand_product)
    brand_product = brand_product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    brand_price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).filter(brand=brand_type).order_by('-price')[::-1]
    length_filter = len(brand_price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    brand_price_range_filter = brand_price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'brand_product':brand_product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'brand_price_range_filter':brand_price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1),
    'brand_type':brand_type,'brand_url':brand_url}
    return render(request, 'mobile.html',params)

    no_of_posts = 20
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category='mobile').filter(brand='infinix').aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    value = request.GET.get('mobile_price_range')
    value = request.GET.get('mobile_price_range')
    if value is None:
        brand_fil_mobile = Product.objects.filter(brand='infinix').filter(sub_category='mobile')        
    elif value =='price_under10000':
        brand_fil_mobile=Product.objects.filter(brand='infinix').filter(sub_category='mobile').filter(price__range=(1,10000)).order_by('-price')[::-1]
    elif value =='price_10000_to_15000':
        brand_fil_mobile=Product.objects.filter(brand='infinix').filter(sub_category='mobile').filter(price__range=(10000,15000)).order_by('-price')[::-1]
    elif value =='price_15000_to_25000':
        brand_fil_mobile=Product.objects.filter(brand='infinix').filter(sub_category='mobile').filter(price__range=(15000,25000)).order_by('-price')[::-1]
    elif value =='price_over_25000':
        brand_fil_mobile=Product.objects.filter(brand='infinix').filter(sub_category='mobile').filter(price__range=(25000,price_max)).order_by('-price')[::-1]
            
    length = len(brand_fil_mobile)
    brand_fil_mobile= brand_fil_mobile[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    brand_type = 'infinix'
    minMaxPrice=Product.objects.filter(brand='infinix').aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    brand_fill_filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,brand_fill_filtered_price),sub_category='mobile').filter(brand='infinix').order_by('-price')[::-1]
   
    params= {'brand_fil_mobile':brand_fil_mobile,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'value':value,'brand_type':brand_type,
    'ascending_prod_laptop':ascending_prod_laptop,'descending_prod_laptop':descending_prod_laptop,'price_range_filter':price_range_filter,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'mobile.html',params)

def mobile_brand_techno(request): 
    sub_cat = 'mobile'
    brand_url = 'mobile_brand_techno'
    brand_type = 'techno'
    price_1= 10000
    price_2 = 15000
    price_3 = 20000
    img_height = 150
    img_width = 80
    no_of_posts = 20
    value = request.GET.get('mobile_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        brand_product = Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type)      
    elif value =='price_1':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(brand_product)
    brand_product = brand_product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    brand_price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).filter(brand=brand_type).order_by('-price')[::-1]
    length_filter = len(brand_price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    brand_price_range_filter = brand_price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'brand_product':brand_product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'brand_price_range_filter':brand_price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1),
    'brand_type':brand_type,'brand_url':brand_url}
    return render(request, 'mobile.html',params)

    no_of_posts = 20
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category='mobile').filter(brand='infinix').aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    value = request.GET.get('mobile_price_range')
    value = request.GET.get('mobile_price_range')
    if value is None:
        brand_fil_mobile = Product.objects.filter(brand='infinix').filter(sub_category='mobile')        
    elif value =='price_under10000':
        brand_fil_mobile=Product.objects.filter(brand='infinix').filter(sub_category='mobile').filter(price__range=(1,10000)).order_by('-price')[::-1]
    elif value =='price_10000_to_15000':
        brand_fil_mobile=Product.objects.filter(brand='infinix').filter(sub_category='mobile').filter(price__range=(10000,15000)).order_by('-price')[::-1]
    elif value =='price_15000_to_25000':
        brand_fil_mobile=Product.objects.filter(brand='infinix').filter(sub_category='mobile').filter(price__range=(15000,25000)).order_by('-price')[::-1]
    elif value =='price_over_25000':
        brand_fil_mobile=Product.objects.filter(brand='infinix').filter(sub_category='mobile').filter(price__range=(25000,price_max)).order_by('-price')[::-1]
            
    length = len(brand_fil_mobile)
    brand_fil_mobile= brand_fil_mobile[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    brand_type = 'infinix'
    minMaxPrice=Product.objects.filter(brand='infinix').aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    brand_fill_filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,brand_fill_filtered_price),sub_category='mobile').filter(brand='infinix').order_by('-price')[::-1]
   
    params= {'brand_fil_mobile':brand_fil_mobile,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'value':value,'brand_type':brand_type,
    'ascending_prod_laptop':ascending_prod_laptop,'descending_prod_laptop':descending_prod_laptop,'price_range_filter':price_range_filter,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'mobile.html',params)

def mobile_brand_huawei(request):
    sub_cat = 'mobile'
    brand_url = 'mobile_brand_huawei'
    brand_type = 'huawei'
    price_1= 10000
    price_2 = 15000
    price_3 = 20000
    img_height = 150
    img_width = 80
    no_of_posts = 20
    value = request.GET.get('mobile_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        brand_product = Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type)      
    elif value =='price_1':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        brand_product=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(brand_product)
    brand_product = brand_product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).filter(brand=brand_type).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    brand_price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).filter(brand=brand_type).order_by('-price')[::-1]
    length_filter = len(brand_price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    brand_price_range_filter = brand_price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'brand_product':brand_product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'brand_price_range_filter':brand_price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1),
    'brand_type':brand_type,'brand_url':brand_url}
    return render(request, 'mobile.html',params)

    no_of_posts = 20
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category='mobile').filter(brand='infinix').aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    value = request.GET.get('mobile_price_range')
    value = request.GET.get('mobile_price_range')
    if value is None:
        brand_fil_mobile = Product.objects.filter(brand='infinix').filter(sub_category='mobile')        
    elif value =='price_under10000':
        brand_fil_mobile=Product.objects.filter(brand='infinix').filter(sub_category='mobile').filter(price__range=(1,10000)).order_by('-price')[::-1]
    elif value =='price_10000_to_15000':
        brand_fil_mobile=Product.objects.filter(brand='infinix').filter(sub_category='mobile').filter(price__range=(10000,15000)).order_by('-price')[::-1]
    elif value =='price_15000_to_25000':
        brand_fil_mobile=Product.objects.filter(brand='infinix').filter(sub_category='mobile').filter(price__range=(15000,25000)).order_by('-price')[::-1]
    elif value =='price_over_25000':
        brand_fil_mobile=Product.objects.filter(brand='infinix').filter(sub_category='mobile').filter(price__range=(25000,price_max)).order_by('-price')[::-1]
            
    length = len(brand_fil_mobile)
    brand_fil_mobile= brand_fil_mobile[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    brand_type = 'infinix'
    minMaxPrice=Product.objects.filter(brand='infinix').aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    brand_fill_filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,brand_fill_filtered_price),sub_category='mobile').filter(brand='infinix').order_by('-price')[::-1]
   
    params= {'brand_fil_mobile':brand_fil_mobile,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'value':value,'brand_type':brand_type,
    'ascending_prod_laptop':ascending_prod_laptop,'descending_prod_laptop':descending_prod_laptop,'price_range_filter':price_range_filter,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'mobile.html',params)



# Top-electronics

def headphone(request):    
    sub_cat = 'headphone'
    price_1= 500
    price_2 = 1000
    price_3 = 2000
    no_of_posts = 20
    img_height=150
    img_width=150
    value = request.GET.get('headphone_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,
    'img_height':img_height,'img_width':img_width,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'top_electronics.html',params)

def smartwatch(request):
    sub_cat = 'smartwatch'
    price_1=500
    price_2 = 1000
    price_3 = 1500
    no_of_posts = 20
    img_height=120
    img_width=120
    value = request.GET.get('smartwatch_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'img_height':img_height,'img_width':img_width,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'top_electronics.html',params)

def camera(request):
    sub_cat = 'camera'
    price_1= 20000
    price_2 = 40000
    price_3 = 60000
    no_of_posts = 20
    img_height=120
    img_width=150
    value = request.GET.get('camera_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,
    'img_height':img_height,'img_width':img_width,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'top_electronics.html',params)

def printer(request):
    sub_cat = 'printer'
    price_1= 10000
    price_2 = 20000
    price_3 = 30000
    no_of_posts = 20
    img_height=150
    img_width=150
    value = request.GET.get('printer_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,
    'img_height':img_height,'img_width':img_width,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'top_electronics.html',params)

def home_theatre(request):
    sub_cat = 'home_theatre'
    price_1= 1500
    price_2 = 2000
    price_3 = 3000
    no_of_posts = 20
    img_height = 140
    img_width = 200
    value = request.GET.get('home_theatre_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'value':value,'sub_cat':sub_cat,'img_height':img_height,
    'img_width':img_width,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'top_electronics.html',params)

def computer_accessories(request):
    sub_cat = 'computer_accessories'
    price_1= 5000
    price_2 = 10000
    img_height=150
    img_width=150
    price_3 = 15000
    no_of_posts = 20
    value = request.GET.get('computer_accessories_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,
    'img_height':img_height,'img_width':img_width,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'top_electronics.html',params)

def router(request):
    sub_cat = 'router'
    price_1= 2000
    price_2 = 3000
    price_3 = 4000
    img_height = 140
    img_width = 200
    no_of_posts = 20
    value = request.GET.get('router_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'top_electronics.html',params)

# More Electronics prducts

def tablet_accessories(request):
    sub_cat = 'tablet_accessories'
    price_1= 2000
    price_2 = 3000
    price_3 = 4000
    img_height = 200
    img_width = 200
    no_of_posts = 20
    value = request.GET.get('tablet_accessories_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'top_electronics.html',params)

def gaming_accessories(request):
    sub_cat = 'gaming_accessories'
    price_1= 2000
    price_2 = 3000
    price_3 = 4000
    img_height = 200
    img_width = 200
    no_of_posts = 20
    value = request.GET.get('gaming_accessories_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'top_electronics.html',params)

def electronics_component(request):
    sub_cat = 'electronics_component'
    price_1= 2000
    price_2 = 3000
    price_3 = 4000
    img_height = 200
    img_width = 200
    no_of_posts = 20
    value = request.GET.get('electronics_component_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'top_electronics.html',params)

def computer_ssd(request):
    sub_cat = 'computer_ssd'
    price_1= 2000
    price_2 = 3000
    price_3 = 4000
    img_height = 200
    img_width = 200
    no_of_posts = 20
    value = request.GET.get('computer_ssd_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'top_electronics.html',params)

def graphics_card(request):
    sub_cat = 'graphics_card'
    price_1= 2000
    price_2 = 3000
    price_3 = 4000
    img_height = 200
    img_width = 200
    no_of_posts = 20
    value = request.GET.get('graphics_card_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'top_electronics.html',params)

def monitor(request):
    sub_cat = 'monitor'
    price_1= 2000
    price_2 = 3000
    price_3 = 4000
    img_height = 200
    img_width = 200
    no_of_posts = 20
    value = request.GET.get('monitor_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'top_electronics.html',params)

def pen_drive(request):
    sub_cat = 'pen_drive'
    price_1= 2000
    price_2 = 3000
    price_3 = 4000
    img_height = 200
    img_width = 200
    no_of_posts = 20
    value = request.GET.get('pen_drive_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'top_electronics.html',params)






def productview(request, myid):
    # mob_spe = Mobile.objects.filter(product_name=request.product_name)
    product=Product.objects.filter(id=myid)
    for i in product:
        mobile_name = i.product_name
        mob_spe = Mobile.objects.filter(product_name=mobile_name)
    for i in product:
        laptop_name = i.product_name
        lap_spe = Laptop.objects.filter(product_name=laptop_name)
        
    params ={'product':product[0],'mob_spe':mob_spe,'lap_spe':lap_spe}

    return render(request, "productview.html", params)


def productviewLaptop(request, myid):

    product=Product.objects.filter(id=myid)
    for i in product:
         laptop_name = i.product_name
         lap_spe = Laptop.objects.filter(product_name=laptop_name)

         return render(request, "productviewLaptop.html", {'product':product[0],'lap_spe':lap_spe})


def productViewMobile(request, myid):
    product=Product.objects.filter(id=myid)
    for i in product:
         mobile_name = i.product_name
         mob_spe = Laptop.objects.filter(product_name=mobile_name)

         return render(request, "productviewMobile.html", {'product':product[0],'mob_spe':mob_spe})


def beauty_health(request):
    product = Product.objects.filter(category=  'beauty_health')
    return render(request, 'beauty_health.html',{'product':product})


def wears_shoes(request):
    no_of_posts = 3
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    # print(page)
    
    product = Product.objects.filter(category=  'wears_shoes')
    length = len(product)
    product= product[(page-1)*no_of_posts: page*no_of_posts]

    if page>1:
        prev = page - 1
    else:
        prev = None
    
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    
    
    return render(request, 'wears_shoes.html', {'product':product,'prev': prev, 'nxt': nxt})

#Home-appliances

def kitchen_appliances(request):
    sub_cat = 'kitchen_appliances'
    price_1= 2000
    price_2 = 3000
    price_3 = 4000
    img_height = 120
    img_width = 120
    no_of_posts = 20
    value = request.GET.get('kitchen_appliances_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 

    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,
  
    'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'appliances.html',params)

def heater_fan_cooler(request):
    sub_cat = 'heater_fan_cooler'
    price_1= 2000
    price_2 = 3000
    price_3 = 8000
    img_height = 120
    img_width = 120
    no_of_posts = 20
    value = request.GET.get('heater_fan_cooler_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'appliances.html',params)

def lighting(request):
    sub_cat = 'lighting'
    price_1= 2000
    price_2 = 3000
    price_3 = 4000
    img_height = 120
    img_width = 120
    no_of_posts = 20
    value = request.GET.get('lighting_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'appliances.html',params)

def hardware_tools(request):
    sub_cat = 'hardware_tools'
    price_1= 2000
    price_2 = 3000
    price_3 = 4000
    img_height = 120
    img_width = 120
    no_of_posts = 20
    value = request.GET.get('hardware_tools_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'appliances.html',params)

def washing_machine(request):
    sub_cat = 'washing_machine'
    price_1= 10000
    price_2 = 15000
    price_3 = 25000
    img_height = 120
    img_width = 120
    no_of_posts = 20
    value = request.GET.get('washing_machine_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'appliances.html',params)

def regrigerator(request):
    sub_cat = 'regrigerator'
    price_1= 12000
    price_2 = 18000
    price_3 = 27000
    img_height = 120
    img_width = 120
    no_of_posts = 20
    value = request.GET.get('regrigerator_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'appliances.html',params)

def air_purifiers(request):
    sub_cat = 'air_purifiers'
    price_1= 5000
    price_2 =12000
    price_3 = 20000
    img_height = 120
    img_width = 120
    no_of_posts = 20
    value = request.GET.get('air_purifiers_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'appliances.html',params)

def television(request):
    sub_cat = 'television'
    price_1= 10000
    price_2 = 18000
    price_3 = 20000
    img_height = 120
    img_width = 120
    no_of_posts = 20
    value = request.GET.get('television_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'appliances.html',params)

def microwave(request):
    sub_cat = 'microwave'
    price_1= 10000
    price_2 = 18000
    price_3 = 20000
    img_height = 120
    img_width = 120
    no_of_posts = 20
    value = request.GET.get('microwave_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'appliances.html',params)

def ait_conditioner(request):
    sub_cat = 'ait_conditioner'
    price_1= 10000
    price_2 = 18000
    price_3 = 20000
    img_height = 120
    img_width = 120
    no_of_posts = 20
    value = request.GET.get('ait_conditioner_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'appliances.html',params)

def air_cooler(request):
    sub_cat = 'air_cooler'
    price_1= 10000
    price_2 = 18000
    price_3 = 20000
    img_height = 120
    img_width = 120
    no_of_posts = 20
    value = request.GET.get('air_cooler_price_range')
    page = request.GET.get('page')
    if page is None: 
        page = 1
    else:
        page = int(page)
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price')) 
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max') 
    
    if value is None:
        product = Product.objects.filter(sub_category=sub_cat)        
    elif value =='price_1':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(1,price_1)).order_by('-price')[::-1]
    elif value =='price_2':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_1,price_2)).order_by('-price')[::-1]
    elif value =='price_3':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_2,price_3)).order_by('-price')[::-1]
    elif value =='price_4':
        product=Product.objects.filter(sub_category=sub_cat).filter(price__range=(price_3,price_max)).order_by('-price')[::-1]
    length = len(product)
    product = product[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/ no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    page_len=math.ceil(length/ no_of_posts) 
    minMaxPrice=Product.objects.filter(sub_category=sub_cat).aggregate(Min('price'),Max('price'))
    min_price= Product.objects.aggregate(Min('price'))
    max_price= Product.objects.aggregate(Max('price'))
    filtered_price=request.GET.get('filter')
    price_min=minMaxPrice.get('price__min')
    price_max=minMaxPrice.get('price__max')
    price_range_filter = Product.objects.filter(price__range=(price_min,filtered_price),sub_category=sub_cat).order_by('-price')[::-1]
    length_filter = len(price_range_filter)
    page_len_filter=math.ceil(length_filter/ no_of_posts)
    
    price_range_filter = price_range_filter[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev_filter = page - 1
    else:
        prev_filter = None
    if page<math.ceil(length_filter/ no_of_posts):
        nxt_filter = page + 1
    else:
        nxt_filter = None

    if page_len>page:
        page_len= page + 2
    if page_len>8: 
        page_len=page_len-1
    

    if page_len_filter>page:
        page_len_filter= page + 2
    if page_len_filter>8: 
        page_len_filter=page_len_filter-1

    params= {'product':product,'prev':prev,'prev':prev, 'nxt':nxt,'min_price':min_price,'img_height':img_height,'img_width':img_width,'value':value,'sub_cat':sub_cat,
    'price_1':price_1,'price_2':price_2,'price_3':price_3,'price_range_filter':price_range_filter,'filtered_price':filtered_price,
    'prev_filter':prev_filter,'nxt_filter':nxt_filter,'price_range_filter':price_range_filter,'page_len_filter':range(1,page_len_filter+1) ,
    'max_price':max_price,'minMaxPrice':minMaxPrice,'nxt':nxt,'page_len':range(1,page_len+1)}

    return render(request, 'appliances.html',params)
