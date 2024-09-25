# Database field limits
CHAR_SHORT_LIMIT = 10
CHAR_MEDIUM_LIMIT = 25
CHAR_LONG_LIMIT = 50
CHAR_VERY_LONG_LIMIT = 255

# Database names
USER_AUTHENTICATION = 'user_authentication'
PRODUCTS = 'products'

# Response Constants
MESSAGE = 'message'
ERROR = 'error'
DATA = 'data'

# User Statements
USER_LOGIN_SUCCESSFUL = 'User Login successful'
USER_NOT_FOUND = 'User not found'
USER_REGISTER_SUCCESSFUL = 'User registered successfully'

# JWT Token Errors
JWT_INVALID_TOKEN = 'Invalid Token'
JWT_TOKEN_EXPIRED = 'Token Expired'
JWT_TOKEN_REQUIRED = 'Token Required'
TOKEN_NOT_REQUIRED_FOR_URLS = ['/register/', '/login/']

# Password validation Error Statments
PASSWORD_LENGTH_ERROR = 'Password should be more than 6 characters'
PASSWORD_TYPES_ERROR = 'Use Atleast 1 capital letter, symbol, number'
PASSWORD_CAPITAL_ERROR = 'Use Atleast 1 capital letter'
PASSWORD_SYMBOL_ERROR = 'Use Atleast 1 symbol'
PASSWORD_NUMBER_ERROR = 'Use Atleast 1 Number'

# Login Validation Error Statments
LOGIN_INVALID_DATA_ERROR = 'Invalid Email or Password'
LOGIN_USER_DOES_NOT_EXISTS = 'User Does Not Exists'

# Products Validation
PRODUCT_CREATED_SUCCESSFULLY = 'Product created successfully'
PRODUCT_DELETED_SUCCESSFULLY = 'Product deleted successfully'
PRODUCT_CREATION_FAILED = 'Product creation failed'
PRODUCT_ALREADY_EXISTS = 'A product with this name already exists.'
PRODUCT_ID_REQUIRED = 'Product ID is required'
PRODUCT_NOT_FOUND = 'Product not found'
PRODUCT_UPDATED_SUCCESSFULLY = 'Product updated successfully'

# Field Constants
USER_ID = 'user_id'
USER_NAME = 'user_name'
PASSWORD = 'password'
TOKEN = 'token'
USER = 'user'
PRODUCT_NAME = 'product_name'
PRODUCT_ID = 'product_id'
USR = 'USR'
PRD = 'PRD'

# Request methods
POST = 'POST'
PUT = 'PUT'
GET = 'GET'
DELETE = 'DELETE'

# Apps
PRODUCTS ='products'
AUTHENTICATION = 'authentication'

# Logger Stmts
UPDATING_PRODUCT_DETAILS = 'Updating product details for product_id:'
FETCHING_PRODUCT_DETAILS = 'Fetching product details for product_id:'
DELETING_PRODUCT_DETAILS = 'Deleting product with product_id:'
VALIDATION_PRODUCT_ERROR = 'Validation error for product:'
RECEIVED_PRODUCT_DETAILS = 'Received product details:'
RECEIVED_USER_DETAILS = 'Received user details'

# CACHE
TIME_OUT=60*5