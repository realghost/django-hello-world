from datetime import datetime
from django.shortcuts import render_to_response
from django_hello_world.requests.models import RequestInfo


def requests_show(request, count=10):
    """
    Shows last count requests
    """    
    # request.request_info is used as first request in the list. Try to get it
    try:
        current_request =  request.request_info
        current_request.datetime = datetime.now()
    except AttributeError:
#        error_message = "A problem with RequestsMiddleware. Current request"+\
#                        " is not registred"
        current_request = []
        count += 1
    # Get previous requests stored in db
    db_requests = RequestInfo.objects.order_by('-datetime')[:count-1]    # Concatenate requests and generate response
    requests = [current_request] + list(db_requests)
    response = render_to_response('requests.html', {'requests':requests})
    # New response.tell() has another value. Therefore a new response with
    # correct values must be calculated
    while response.tell() != current_request.response_tell and \
          response.status_code != current_request.response_tell:
        current_request.response_status = response.status_code
        current_request.response_tell = response.tell()
        requests = [current_request] + list(db_requests)
        response = render_to_response('requests.html', {'requests':requests})
    return response

