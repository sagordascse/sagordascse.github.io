from django.db import models

# Create your models here.
class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    description=models.CharField(max_length=300)
    publish_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    contact_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=70,default="")
    phone=models.CharField(max_length=50,default="")
    description=models.CharField(max_length=500,default="")

    def __str__(self):
        return self.name

class myUserProductOrder(models.Model):
    order_id=models.AutoField(primary_key=True)
    product_json=models.CharField(max_length=1000,default="")
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=100,default="")
    email=models.CharField(max_length=100,default="")
    address=models.CharField(max_length=100,default="")
    city=models.CharField(max_length=100,default="")
    state=models.CharField(max_length=100,default="")
    zip_code=models.CharField(max_length=15,default="")
    phone_number=models.CharField(max_length=15,default="")

class trackerOrder(models.Model):
    updateId = models.AutoField(primary_key=True)
    orderId = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timeStamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:15] + "..."


