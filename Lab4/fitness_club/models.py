from datetime import datetime

from django.contrib.auth.models import User
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


class Instructor(models.Model):
    name = models.CharField(max_length=30)
    specialization = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='')

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
