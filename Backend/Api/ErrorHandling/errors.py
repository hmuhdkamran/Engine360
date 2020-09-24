from Handler.RequestHandler import FailureResponse


def handler404error(request, exception):
    return FailureResponse().bad_url_object()


def handler500error(request, exception=None):
    return FailureResponse().something_went_wrong()
