
from .models import DatabaseRequest


class SavesRequestsMiddleware(object):
    """
    Middleware for saving http request into database
    """

    def process_request(self, request):
        """
        Overriding standard method
        """
        if request.is_ajax():
            pass
        else:
            DatabaseRequest.objects.create(
                path=request.path,
                method=request.method,
                user=request.user
            )
            return None
