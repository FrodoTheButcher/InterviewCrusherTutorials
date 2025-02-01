from django.contrib import admin
from django.urls import path, include
from UsersApp.views import RegisterBookingView , RegisterUserView , query_bookings, UpdateRegistrationRequest ,MyTokenObtainPairView ,delete_user, get_all_registration_requests , get_users_registered
from RoomApp.views import RegisterRoomView, DeleteRoomView
from TasksApp.views import AssignTaskView, deleteTask
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from UsersApp.views import CheckBooking
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

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
    path("delete_task/<int:user_accessing_pk>/<int:task_id>/",deleteTask,name="deleteTask"),
    path("register_booking/", RegisterBookingView.as_view(), name="register_booking"),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("register_room/", RegisterRoomView.as_view(), name="register_room"),
        path("room/delete/<int:user_requesting>/<int:pk>/",DeleteRoomView.as_view(),name="DeleteRoomView"),
    path("register_user/",RegisterUserView.as_view(),name="register_user",),
    path('check_booking/<int:booking_id>/<int:user_id>/', CheckBooking.as_view(), name='check_booking'),
    path("query_bookings/<int:user_id>/",query_bookings,name="query_bookings"),
   path("user_registration/<int:pk>/<int:user_requesting_pk>", UpdateRegistrationRequest.as_view(), name="update_registration"),
    path("registrations_requests/",get_all_registration_requests,name="get_all_registration_requests"),
   path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("get_users/",get_users_registered,name="get_users_registered"),
    path("task/<int:user_accessing_pk>",AssignTaskView.as_view(),name="AssignTaskView"),
    path("users/delete/<int:user_id>/<int:user_requesting_id>/",delete_user,name="delete_user"),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
