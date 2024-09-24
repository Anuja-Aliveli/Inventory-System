from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from common import constants as ct
from common.utils import generate_id, get_latest_id
from products.products_serializer import ProductsSerializer
from products.products_model import ProductModel

# Add Product
@api_view(['POST'])
def add_product(request):
    product_details = request.data
    product_details[ct.USER] = request.user_id
    try:
        product_name = product_details.get(ct.PRODUCT_NAME)
        if ProductModel.objects.filter(product_name=product_name, user_id=product_details[ct.USER]).exists():
            return JsonResponse(
                {ct.ERROR: ct.PRODUCT_ALREADY_EXISTS},
                status=status.HTTP_400_BAD_REQUEST
            )
        latest_product = get_latest_id(ProductModel, ct.PRODUCT_ID)
        product_details[ct.PRODUCT_ID] = generate_id(ct.PRD, latest_product)
        print(product_details)
        serializer = ProductsSerializer(data=product_details)
        if serializer.is_valid():  
            serializer.save()
            return JsonResponse({ct.MESSAGE: ct.PRODUCT_CREATED_SUCCESSFULLY}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return JsonResponse({ct.ERROR: str(error)}, status=status.HTTP_400_BAD_REQUEST)
    
    
# Update Product details
@api_view(['PUT'])
def update_product_details(request, item_id):
    try:
        product_details = ProductModel.objects.get(product_id=item_id)
        serializer = ProductsSerializer(product_details, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({ct.MESSAGE: ct.PRODUCT_UPDATED_SUCCESSFULLY}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except ProductModel.DoesNotExist:
        return JsonResponse({ct.ERROR: ct.PRODUCT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)