import logging
from django.utils.deprecation import MiddlewareMixin

# Настроим логгер
logger = logging.getLogger(__name__)

class RequestLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        logger.info(f"Request: {request.method} {request.path}")

    def process_response(self, request, response):
        logger.info(f"Response status: {response.status_code}")
        return response

    def process_exception(self, request, exception):
        logger.error(f"Exception: {exception}")
