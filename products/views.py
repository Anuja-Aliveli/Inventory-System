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
def update_product_details(data,item_id):
    try:
        product_details = ProductModel.objects.get(product_id=item_id)
        serializer = ProductsSerializer(product_details, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({ct.MESSAGE: ct.PRODUCT_UPDATED_SUCCESSFULLY}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except ProductModel.DoesNotExist:
        return JsonResponse({ct.ERROR: ct.PRODUCT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)

# Get Project details
def get_project_details(item_id):
    try:
        product_details = ProductModel.objects.get(product_id=item_id)
        serializer = ProductsSerializer(product_details)
        return JsonResponse({ct.DATA: serializer.data}, status=status.HTTP_200_OK)
    except ProductModel.DoesNotExist:
        return JsonResponse({ct.ERROR: ct.PRODUCT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    except Exception as error:
        return JsonResponse({ct.ERROR: str(error)}, status=status.HTTP_400_BAD_REQUEST)

# Delete Product details
def delete_product_details(item_id):
    try:
        product_details = ProductModel.objects.get(product_id=item_id)
        product_details.delete()
        return JsonResponse({ct.MESSAGE: ct.PRODUCT_DELETED_SUCCESSFULLY}, status=status.HTTP_200_OK)
    
    except ProductModel.DoesNotExist:
        return JsonResponse({ct.ERROR: ct.PRODUCT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as error:
        return JsonResponse({ct.ERROR: str(error)}, status=status.HTTP_400_BAD_REQUEST)

# Product Details
@api_view(['PUT', 'GET', 'DELETE'])
def product_details(request, item_id):
    if not item_id:
        return JsonResponse({ct.ERROR: ct.PRODUCT_ID_REQUIRED}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        return update_product_details(request.data, item_id)
    elif request.method == 'GET':
        return get_project_details(item_id)
    elif request.method == 'DELETE':
        return delete_product_details(item_id)