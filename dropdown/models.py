from django.db import models


class Category(models.Model):
    name_cat = models.CharField(max_length=250)

    def __str__(self):
        return self.name_cat


class Subcategory(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE,
                            verbose_name='category')
    name_subcat = models.CharField(max_length=250)

    def __str__(self):
        return self.name_subcat


class Good(models.Model):
    subcat = models.ForeignKey(Subcategory, on_delete=models.CASCADE,
                               verbose_name='subcategory')
    name_good = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name_good


class OrderItem(models.Model):
    order = models.ForeignKey("dropdown.Order", on_delete=models.CASCADE, verbose_name="order")
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='cat')
    subcat = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='subcat')
    name_good = models.ForeignKey(Good, on_delete=models.CASCADE, verbose_name='good')
    quantity = models.PositiveIntegerField(default=0)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f'{self.name_good} + {self.quantity}'


class Order(models.Model):
    order_id = models.PositiveIntegerField(unique=True)
    order_date = models.DateTimeField(auto_now=True)
    total_quantity = models.PositiveIntegerField(default=0)
    total_amount = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return str(self.order_id)


class AllowedCombination(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcat = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    good = models.ForeignKey(Good, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cat} {self.subcat} {self.good}'

    class Meta:
        ordering = ['pk']
