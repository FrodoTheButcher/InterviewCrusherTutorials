from django.contrib import admin
from django.urls import path, include
from UsersApp.views import RegisterBookingView , RegisterUserView , query_bookings, UpdateRegistrationRequest
from RoomApp.views import RegisterRoomView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from UsersApp.views import CheckBooking
from django.conf import settings
from django.conf.urls.static import static
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
    path("register_user/",RegisterUserView.as_view(),name="register_user",),
    path('check_booking/<int:booking_id>/<int:profile_id>/', CheckBooking.as_view(), name='check_booking'),
    path("query_bookings/<int:profile_id>/",query_bookings,name="query_bookings"),
    path("user_registration/<int:pk>/",UpdateRegistrationRequest.as_view(),name="update_registration")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
