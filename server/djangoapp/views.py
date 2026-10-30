from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Dealer, Review, CarMake
from .serializers import DealerSerializer, ReviewSerializer, CarMakeSerializer

@api_view(["GET"])
@permission_classes([AllowAny])
def dealers(request):
    return Response(DealerSerializer(Dealer.objects.all(), many=True).data)

@api_view(["GET"])
@permission_classes([AllowAny])
def dealer_detail(request, dealer_id):
    try: dealer = Dealer.objects.get(pk=dealer_id)
    except Dealer.DoesNotExist: return Response({"error":"Dealer not found"}, status=404)
    return Response(DealerSerializer(dealer).data)

@api_view(["GET"])
@permission_classes([AllowAny])
def dealers_by_state(request, state):
    qs = Dealer.objects.filter(state__iexact=state)
    return Response(DealerSerializer(qs, many=True).data)

@api_view(["GET"])
@permission_classes([AllowAny])
def dealer_reviews(request, dealer_id):
    qs = Review.objects.filter(dealer_id=dealer_id).order_by("-created_at")
    return Response(ReviewSerializer(qs, many=True).data)

@api_view(["POST"])
def add_review(request, dealer_id):
    if not Dealer.objects.filter(pk=dealer_id).exists(): return Response({"error":"Dealer not found"}, status=404)
    data = request.data.copy()
    data["dealer"] = dealer_id
    serializer = ReviewSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(["GET"])
@permission_classes([AllowAny])
def car_makes(request):
    return Response(CarMakeSerializer(CarMake.objects.all(), many=True).data)

@csrf_exempt
@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    data = request.data
    required = ["username", "first_name", "last_name", "email", "password"]
    if any(not data.get(k) for k in required): return Response({"error":"All five fields are required"}, status=400)
    if User.objects.filter(username=data["username"]).exists(): return Response({"error":"Username already exists"}, status=400)
    user = User.objects.create_user(username=data["username"], email=data["email"],
        password=data["password"], first_name=data["first_name"], last_name=data["last_name"])
    return Response({"message":"User registered","username":user.username}, status=201)

@csrf_exempt
@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    user = authenticate(request, username=request.data.get("username"), password=request.data.get("password"))
    if user is None: return Response({"error":"Invalid username or password"}, status=400)
    login(request, user)
    return Response({"message":"Login successful","username":user.username})

@api_view(["POST"])
def logout_user(request):
    logout(request)
    return Response({"message":"Logout successful"})

@api_view(["GET"])
@permission_classes([AllowAny])
def current_user(request):
    return Response({"authenticated": request.user.is_authenticated,
                     "username": request.user.username if request.user.is_authenticated else None})

@api_view(["POST"])
@permission_classes([AllowAny])
def analyze_review(request):
    text = str(request.data.get("review", "")).lower()
    if not text.strip(): return Response({"error":"review is required"}, status=400)
    positive = ["fantastic","great","excellent","good","amazing","wonderful","helpful","friendly","love"]
    negative = ["bad","poor","terrible","awful","worst","rude","hate","slow"]
    score = sum(w in text for w in positive) - sum(w in text for w in negative)
    sentiment = "positive" if score > 0 else "negative" if score < 0 else "neutral"
    return Response({"review":request.data.get("review"), "sentiment":sentiment, "score":score})
