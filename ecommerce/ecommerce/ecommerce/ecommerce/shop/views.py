from django.http import HttpResponse
from django.shortcuts import render
from .models import product, Contact, myUserProductOrder, trackerOrder
from math import ceil
import json


def index(request):
    allproducts = []

    category_Products = product.objects.values("category")

    # here, set comprehension has been used. set discard duplicate category value
    categorys = {item["category"] for item in category_Products}

    # set(categorys) has converted into list. because, list is ordered sequence of element.
    for temp_category in list(categorys):
        products = product.objects.filter(category=temp_category)
        n = len(products)
        num_slides = n // 4 + ceil((n / 4) - (n // 4))
        allproducts.append([products, num_slides, range(1, num_slides)])

    params = {"all_products": allproducts}
    return render(request, "shop/index.html", params)


def searchMatch(query, item):
    if query in item.description.lower() or query in item.product_name.lower() or query in item.category.lower() or query in item.subcategory.lower():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search').lower()
    allproducts = []

    category_Products = product.objects.values("category")

    # here, set comprehension has been used. set discard duplicate category value
    categorys = {item["category"] for item in category_Products}

    # set(categorys) has converted into list. because, list is ordered sequence of element.
    for temp_category in list(categorys):
        productsTemp = product.objects.filter(category=temp_category)
        products = [item for item in productsTemp if searchMatch(query, item)]
        n = len(products)
        num_slides = n // 4 + ceil((n / 4) - (n // 4))
        if n != 0:
            allproducts.append([products, num_slides, range(1, num_slides)])

    params = {"all_products": allproducts, 'message': ""}
    if len(allproducts) == 0 or len(query) < 4:
        params = {'message': 'Please make sure to enter relevant search '}

    return render(request, "shop/search.html", params)


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        description = request.POST.get("description", "")
        if name != "" and email != "" and phone != "" and description != "":
            contact_info = Contact(name=name, email=email, phone=phone, description=description)
            contact_info.save()
            thank = True
        else:
            return HttpResponse("Fill up all field with correct value")
    return render(request, "shop/contact.html", {'thank': thank})


def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = myUserProductOrder.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = trackerOrder.objects.filter(orderId=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timeStamp})
                    response = json.dumps({"status":"success","updates":updates,"itemsJson":order[0].product_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')
    return render(request, "shop/tracker.html")


def productView(request, myid):
    allproducts = []

    category_Products = product.objects.values("category")

    # here, set comprehension has been used. set discard duplicate category value
    categorys = {item["category"] for item in category_Products}

    # set(categorys) has converted into list. because, list is ordered sequence of element.
    for temp_category in list(categorys):
        products = product.objects.filter(category=temp_category)
        n = len(products)
        num_slides = n // 4 + ceil((n / 4) - (n // 4))
        allproducts.append([products, num_slides, range(1, num_slides)])

    products = product.objects.filter(id=myid)
    params = {"all_products": allproducts, 'product': products[0]}
    return render(request, "shop/productView.html", params)


def check_out(request):
    thank = False
    id=0
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone_number = request.POST.get('phone', '')
        order = myUserProductOrder(product_json=items_json, name=name, email=email, address=address, city=city,
                                   state=state, zip_code=zip_code, phone_number=phone_number, amount=amount)

        if int(amount)!=0:
            order.save()
            thank = True
            id = order.order_id
        else:
            return HttpResponse("Buy some product.Then fill all information")


    return render(request, "shop/check_out.html", {'thank': thank, 'id': id})
