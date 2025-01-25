from django.contrib import admin
from django.urls import path, include
from .views import RegisterBookingView, RegisterRoomView , RegisterUserView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
# Configure the schema view for Swagger and Redoc
schema_view = get_schema_view(
   openapi.Info(
      title="API Documentation",
      default_version='v1',
      description="Detailed description of the API functionalities",
      terms_of_service="https://www.yourwebsite.com/terms/",
      contact=openapi.Contact(email="contact@yourapi.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register_booking/", RegisterBookingView.as_view(), name="register_booking"),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("register_room/", RegisterRoomView.as_view(), name="register_room"),
    path("register_user/",RegisterUserView.as_view(),name="register_user",)
]
