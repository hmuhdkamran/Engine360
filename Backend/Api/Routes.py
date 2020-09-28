from .Auth.auth_routes import urlpatterns as auth_url_patters
from .Setup.roles import urlpatterns as routepatterns

urlpatterns = []
urlpatterns += auth_url_patters
urlpatterns += routepatterns
