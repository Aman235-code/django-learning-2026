import datetime
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class SimpleLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(f"[{datetime.datetime.now()}] Request URL : {request.path}")

    def process_response(self, request, response):
        print(f"[{datetime.datetime.now()}] response Status Code : {response.status_code}")
        return response
    
class BlockIpMiddleware(MiddlewareMixin):
    BLOCKED_IPS = [
        '127.0.0.1'
    ]

    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if ip in self.BLOCKED_IPS:
            return HttpResponse("Your IP is blocked", status=403)


