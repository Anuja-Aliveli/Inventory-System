# Database field limits
CHAR_SHORT_LIMIT = 10
CHAR_MEDIUM_LIMIT = 25
CHAR_LONG_LIMIT = 50
CHAR_VERY_LONG_LIMIT = 255

# Database names
USER_AUTHENTICATION = 'user_authentication'

# Response Constants
MESSAGE = 'message'
ERROR = 'error'

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

# Field Constants
USER_ID = 'user_id'
USR = 'USR'
USER_NAME = 'user_name'
PASSWORD = 'password'
TOKEN = 'token'