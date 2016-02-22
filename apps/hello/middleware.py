
from .models import DatabaseRequest


class SavesRequestsMiddleware(object):
    """
    Middleware for saving http request into database
    """

    def process_request(self, request):
        """
        Overriding standard method
        """
        if request.is_ajax() or request.path == '/requests/':
            return

        user = request.user if request.user.is_authenticated() else None

        DatabaseRequest.objects.create(path=request.path,
                                       method=request.method,
                                       user=user)
