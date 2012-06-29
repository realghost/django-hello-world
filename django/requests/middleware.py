from requests.models import RequestInfo


class RequestsMiddleware(object):
    """
    Middleware that stores all requests in DB.
    """
    def process_request(self,request):
        request_info = RequestInfo()
        request_info.ip = request.META.get('REMOTE_ADDR', '-')
        request_info.protocol = request.META.get('SERVER_PROTOCOL', '-')
        request_info.method = request.META.get('REQUEST_METHOD', '-')
        request_info.path = request.path
        request_info.referer = request.META.get('HTTP_REFERER', '-')
        request_info.response_status = 0
        request_info.response_tell = 0
        request_info.user_agent = request.META.get('HTTP_USER_AGENT', '-')
        request.request_info = request_info
        return None
        
    def process_response(self, request, response):
        """
        This function works after views and aims to store response status 
        end length
        """
        # Try-except block is needed because process_request may be not 
        # executed due to other middlewares
        #assert False        
        try:
            request_info =  request.request_info
        except AttributeError:
            self.process_request(request)
            request_info =  request.request_info
            
        request_info.response_status = response.status_code
        request_info.response_tell = response.tell()
        request_info.save()
        return response
        