from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Sales
from .serializers import CommissionPlanSerializer, SalesSerializer, SellersSerializer, CheckCommissionSerializer, \
    UserSerializer


@api_view(["POST"])
@permission_classes([AllowAny])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        if serializer.save():
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def sellers(request):
    if request.method == "POST":
        serializer = SellersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"id": serializer.data["id"]}, status=status.HTTP_201_CREATED)
        return Response({"message": "Bad request. Please check syntax and try again"},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def commissions(request):
    if request.method == "POST":
        serializer = CommissionPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"id": serializer.data["id"]}, status=status.HTTP_201_CREATED)
        return Response({"message": "Bad request. Please check syntax and try again"},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def month_commission(request):
    if request.method == "POST":
        try:
            calc = Sales()
            calculated_amount = calc.calc_commission(
                request.data["sellers_id"], request.data["amount"])
        except:
            return Response({"message": "Bad request. Please check syntax and try again"},
                            status=status.HTTP_400_BAD_REQUEST)
        request.data["commission"] = calculated_amount
        serializer = SalesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"id": serializer.data["id"], "commission": serializer.data["commission"], },
                            status=status.HTTP_201_CREATED)
        return Response({"message": "Bad request. Please check syntax and try again"},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def vendedores(request, month):
    if request.method == "GET":
        rs = Sales()
        return Response(rs.return_sellers(month))


@api_view(["POST"])
def check_commission(request):
    if request.method == "POST":
        serializer = CheckCommissionSerializer(data=request.data)
        if serializer.is_valid():
            cc = Sales()
            return Response(cc.check_commission(request.data["sellers_id"], request.data["amount"]),
                            status=status.HTTP_201_CREATED)
        return Response({"message": "Bad request. Please check syntax and try again"},
                        status=status.HTTP_400_BAD_REQUEST)
