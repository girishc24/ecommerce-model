from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subcategories', blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='products')

    def __str__(self):
        return self.name



class Attribute(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


    

class AttributeValue(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='values')
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = ('attribute', 'value')

    def __str__(self):
        return f"{self.attribute.name}: {self.value}"



class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    attributes = models.ManyToManyField(AttributeValue, related_name='product_variants')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)

    class Meta:
        unique_together = ('product', 'price')

    def __str__(self):
        attribute_values = ", ".join([str(attr) for attr in self.attributes.all()])
        return f"{self.product.name} - {attribute_values} - Price: {self.price}"

