from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
return HttpResponse(""" <html> <head><title>Car Dealership Review Application</title></head> <body style="font-family: Arial; text-align:center; padding:50px;"> <h1>Car Dealership Review Application</h1> <h2>Welcome to our Dealership Platform!</h2> <p>Explore dealerships and read customer reviews.</p> <a href="/api/dealers/">View All Dealers</a> </body> </html>
""")

urlpatterns = [
path("", home, name="home"),
path("admin/", admin.site.urls),
path("api/", include("djangoapp.urls")),
]
