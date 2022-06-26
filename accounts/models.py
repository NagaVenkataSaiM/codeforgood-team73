from django.db import models



# Create your models here.
class Patient(models.Model):
		profile_of = models.CharField(primary_key=True,max_length=100, blank=True, default='')
		name=models.CharField(max_length=100, blank=True, default='')
		gender=models.CharField(max_length=10, blank=True, default='')
		age = models.IntegerField()
		contact=models.BigIntegerField()

class CartItem(models.Model):
	cart_owner=models.CharField(max_length=200)
	product_name = models.CharField(max_length=200)
	product_price = models.FloatField()
	product_quantity = models.PositiveIntegerField()

class Product(models.Model):
    """Product items"""

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    """Order for product item"""

    product = models.ForeignKey(
        Product, max_length=200, blank=True, on_delete=models.DO_NOTHING
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

