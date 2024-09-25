from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.cache import cache
from common import constants as ct
from common.utils import generate_id, get_latest_id
from products.products_serializer import ProductsSerializer
from products.products_model import ProductModel
import logging

logger = logging.getLogger(ct.PRODUCTS)

# Add Product
@api_view([ct.POST])
def add_product(request):
    product_details = request.data
    product_details[ct.USER] = request.user_id
    logger.debug(f"{ct.RECEIVED_PRODUCT_DETAILS} {product_details}")
    try:
        product_name = product_details.get(ct.PRODUCT_NAME)
        if ProductModel.objects.filter(product_name=product_name, user_id=product_details[ct.USER]).exists():
            logger.error(f"{ct.PRODUCT_ALREADY_EXISTS}")
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
            logger.info(f"{ct.PRODUCT_UPDATED_SUCCESSFULLY} {product_details[ct.PRODUCT_ID]}")
            return JsonResponse({ct.MESSAGE: ct.PRODUCT_CREATED_SUCCESSFULLY}, status=status.HTTP_201_CREATED)
        else:
            logger.error(f"{ct.VALIDATION_PRODUCT_ERROR} : {serializer.errors}")
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        logger.error(f"{str(error)} {product_details[ct.PRODUCT_ID]}")
        return JsonResponse({ct.ERROR: str(error)}, status=status.HTTP_400_BAD_REQUEST)

@api_view([ct.GET])
def get_products_list(request):
    products_list = ProductModel.objects.all()
    serializer = ProductsSerializer(products_list, many=True)
    if not products_list:
        return JsonResponse({ct.MESSAGE: ct.PRODUCT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    return JsonResponse({ct.DATA: serializer.data}, status=status.HTTP_200_OK)

# Update Product details
def update_product_details(data,item_id):
    try:
        item_cache_data = cache.get(item_id)
        product_details = ProductModel.objects.get(product_id=item_id)
        serializer = ProductsSerializer(product_details, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"{ct.PRODUCT_UPDATED_SUCCESSFULLY} {item_id}")
        if item_cache_data:
            cache.set(item_id, serializer.data, timeout=ct.TIME_OUT)
            return JsonResponse({ct.MESSAGE: ct.PRODUCT_UPDATED_SUCCESSFULLY}, status=status.HTTP_200_OK)
        else:
            logger.error(f"{ct.VALIDATION_PRODUCT_ERROR} {item_id}: {serializer.errors}")
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except ProductModel.DoesNotExist:
        logger.error(f"{ct.PRODUCT_NOT_FOUND} {item_id}")
        return JsonResponse({ct.ERROR: ct.PRODUCT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)

# Get Project details
def get_project_details(item_id):
    try:
        item_cache_data = cache.get(item_id)
        if not item_cache_data:
            product_details = ProductModel.objects.get(product_id=item_id)
            serializer = ProductsSerializer(product_details)
            logger.error(f"{ct.VALIDATION_PRODUCT_ERROR} {item_id}: {serializer.data}")
            cache.set(item_id, serializer.data, timeout=ct.TIME_OUT)  # Cache for 15 minutes
        return JsonResponse({ct.DATA: serializer.data}, status=status.HTTP_200_OK)
    except ProductModel.DoesNotExist:
        logger.error(f"{ct.PRODUCT_NOT_FOUND} {item_id}")
        return JsonResponse({ct.ERROR: ct.PRODUCT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    except Exception as error:
        logger.error(f"{str(error)} {item_id}")
        return JsonResponse({ct.ERROR: str(error)}, status=status.HTTP_400_BAD_REQUEST)

# Delete Product details
def delete_product_details(item_id):
    try:
        item_cache_data = cache.get(item_id)
        if item_cache_data:
            cache.delete(item_id)
        product_details = ProductModel.objects.get(product_id=item_id)
        product_details.delete()
        logger.error(f"{ct.PRODUCT_DELETED_SUCCESSFULLY} {item_id}")
        return JsonResponse({ct.MESSAGE: ct.PRODUCT_DELETED_SUCCESSFULLY}, status=status.HTTP_200_OK)
    
    except ProductModel.DoesNotExist:
        logger.error(f"{ct.PRODUCT_NOT_FOUND} {item_id}")
        return JsonResponse({ct.ERROR: ct.PRODUCT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as error:
        logger.error(f"{str(error)} {item_id}")
        return JsonResponse({ct.ERROR: str(error)}, status=status.HTTP_400_BAD_REQUEST)

# Product Details
@api_view([ct.PUT, ct.GET, ct.DELETE])
def product_details(request, item_id):
    logger.debug(f"{ct.RECEIVED_PRODUCT_DETAILS} {item_id}")
    if not item_id:
        logger.warning(ct.PRODUCT_ID_REQUIRED)
        return JsonResponse({ct.ERROR: ct.PRODUCT_ID_REQUIRED}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == ct.PUT:
        logger.info(f"{ct.UPDATING_PRODUCT_DETAILS} {item_id}")
        return update_product_details(request.data, item_id)
    elif request.method == ct.GET:
        logger.info(f"{ct.FETCHING_PRODUCT_DETAILS} {item_id}")
        return get_project_details(item_id)
    elif request.method == ct.DELETE:
        logger.info(f"{ct.DELETING_PRODUCT_DETAILS} {item_id}")
        return delete_product_details(item_id)