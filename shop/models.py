from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from django_countries.fields import CountryField
from django.db.models.signals import post_save


CATEGORY = (
    ('N', 'New'),
    ('BC', 'Best Choice')
)


ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)


class Item(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    item_image = models.ImageField(upload_to='Items/')
    label = models.CharField(choices=CATEGORY, max_length=2)
    description = models.TextField()
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.item_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.item_name)
            super(Item, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("product_details", kwargs={
            "slug": self.slug

        })

    def get_add_to_cart_url(self):
        return reverse('add_to_cart', kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.item_name}"

    def get_total(self):
        return self.quantity * self.item.price

    def get_final_price(self):
        return self.get_total()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(
        'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_items_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total


class BillingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    appartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=True)
    zip = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class ChoiceItem(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.FloatField()
    item_image = models.ImageField(upload_to='Choice_Item/')
    description = models.TextField()
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.item_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.item_name)
            super(ChoiceItem, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("product_details", kwargs={
            "slug": self.slug

        })


class PopularItem(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    item_image = models.ImageField(upload_to='Popular_Items/')
    description = models.TextField()
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.item_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.item_name)
            super(PopularItem, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse("product_details", kwargs={
            "slug": self.slug

        })


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username



class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username



def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=User)


class ContactForm(models.Model):
    message = models.TextField(max_length=1000)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name