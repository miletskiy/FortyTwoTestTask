
from .models import DatabaseRequest
from django.contrib.auth.models import User


class SavesRequestsMiddleware(object):
    """
    Middleware for saving http request into database
    """

    def process_request(self, request):
        """
        Overriding standard method
        """
        if request.is_ajax():
            return

        if request.user.is_authenticated():
            DatabaseRequest.objects.create(path=request.path,
                                           method=request.method,
                                           user=request.user)
        else:
            anonymoususer = User()
            DatabaseRequest.objects.create(path=request.path,
                                           method=request.method,
                                           user=anonymoususer)
