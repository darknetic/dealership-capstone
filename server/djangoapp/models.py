from django.db import models
class Dealer(models.Model):
    full_name = models.CharField(max_length=160)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, db_index=True)
    phone = models.CharField(max_length=40, blank=True)
    website = models.URLField(blank=True)
    def __str__(self): return self.full_name

class Review(models.Model):
    dealer = models.ForeignKey(Dealer, related_name="reviews", on_delete=models.CASCADE)
    name = models.CharField(max_length=120, blank=True)
    review = models.TextField()
    purchase = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"Review for {self.dealer}"

class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self): return self.name

class CarModel(models.Model):
    make = models.ForeignKey(CarMake, related_name="models", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField(default=2025)
    def __str__(self): return f"{self.make} {self.name}"
