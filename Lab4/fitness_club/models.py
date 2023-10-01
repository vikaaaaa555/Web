from datetime import datetime
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models
from django.urls import reverse


class Group(models.Model):
    name = models.CharField(max_length=30)
    client_name = models.ManyToManyField('Client')
    description = models.TextField()
    capacity = models.PositiveIntegerField(default=10)

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return f"Group {self.id}"


class Client(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField(default=1)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    groups = models.ManyToManyField(Group)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return f"Client {self.id}"


phone_number_validator = RegexValidator(
    regex=r'^\+375\(\d{2}\)\d{3}-\d{2}-\d{2}$',
    message='Phone number should be in the format: +375(xx)xxx-xx-xx'
)


class Instructor(models.Model):
    name = models.CharField(max_length=30)
    specialization = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=17, verbose_name='Phone number', blank=True, null=True,
                                    validators=[phone_number_validator])
    email = models.EmailField(max_length=100, verbose_name='Email', blank=True, null=True)
    photo = models.ImageField(upload_to='photos/instructors', default='')

    class Meta:
        verbose_name = "Instructor"
        verbose_name_plural = "Instructors"

    def __str__(self):
        return f"Instructor {self.id}"


class Lesson(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    instructors = models.ManyToManyField(Instructor)

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"

    def __str__(self):
        return f"Lesson {self.id}"


class Payment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(default=datetime.today)

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    def __str__(self):
        return f"Payment {self.id}"


class Membership(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default='')
    count = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name = "Membership"
        verbose_name_plural = "Memberships"

    def __str__(self):
        return f"Membership {self.id}"

    def get_absolute_url(self):
        return reverse('shopping_cart', kwargs={'membership_id': self.pk})


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='First name', null='True')
    last_name = models.CharField(max_length=100, verbose_name='Last name', null='True')
    rating = models.PositiveIntegerField(validators=[
             MinValueValidator(0, message='The rating should be no less 0.'),
             MaxValueValidator(5, message='The rating should be no more 5.'), ])
    feedback = models.TextField(blank=True, null=True, verbose_name='Feedback')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Creation time', null='True')


class Coupon(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default='')
    archive = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Coupon'
        verbose_name_plural = 'Coupons'

    def __str__(self):
        return self.name


class News(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default='')
    photo = models.ImageField(upload_to='photos/news', default='')

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


    def __str__(self):
        return f"News {self.id}"

    def get_absolute_url(self):
        return reverse('news_view', kwargs={'news_id': self.pk})



class Vocation(models.Model):
    vocation = models.CharField(max_length=30)
    description = models.TextField(default='')

    class Meta:
        verbose_name = 'Vocation'
        verbose_name_plural = 'Vocations'

    def __str__(self):
        return self.vocation


class FAQ(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='')

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.name

