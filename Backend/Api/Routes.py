from .Auth.auth_routes import urlpatterns as auth_url_patters
from .Setup.setup_routes import urlpatterns as setup_url_patters

urlpatterns = []
urlpatterns += auth_url_patters
urlpatterns += setup_url_patters
