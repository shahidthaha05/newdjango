from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from.models import *

# Create your views here.


def shop_login(req):
    if 'shop' in req.session:
        if req.method=='POST':
            uname=req.POST['uname']
            password=req.POST['pswd']
            data=authenticate(username=uname,password=password)
            if data:
                login(req,data)
                req.session['shop']=uname
                return redirect(shop_home)
            
            
    else:
        return render(req,'login.html')
    

def shop_logout(req):
    req.session.flush()
    logout(req)
    return redirect(shop_login)

def shop_home(req):
    if 'shop' in req.sesssion:
        return render(req,'shop/home.html')
    else:
        return redirect(shop_login)
        
def add_product(req):
    if 'shop' in req.session:
        if req.method=='POST':
            id=req.POST['pro_id']
            name=req.POST['name']
            price=req.POST['price']
            offer_price=req.POST['offer_price']
            img=req.POST['img']
            dis=req.POST['dis']
            data=product.objects.create(pro_id=id,name=name,price=price,offer_price=offer_price,dis=dis,img=img)
            data.save()
            return redirect(shop_home)
        else:
            return render(req,'shop/add_pro.html')

        
    else:
        return render(shop_login)