import json


from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .cart import Cart
from apps.store.utilities import decrement_product_quantity, send_order_confirmation


