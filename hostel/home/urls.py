from rest_framework import routers
from django.urls import path, include
from .views import api_view_list_hotels, api_view_hotel_detail,api_update_hotel,api_post_hotel,api_delete_hotel,api_view_list_bookings
from .views import HotelList
from . import views

# router = routers.DefaultRouter()
# router.register('hotels', views.HotelViewset)
# router.register('manager',views.ManagerViewset)
# router.register('guest',views.GuestViewset)
# router.register('room',views.RoomViewset)
# router.register('booking',views.BookingViewset)
# urlpatterns = [
#      path('', include(router.urls)),
# ]

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('contact',views.contact,name='contact'),
    path('room1',views.room1,name='room1'),
    path('<int:id>',views.rooms,name='rooms'),

    path('hotel/', api_view_list_hotels, name = 'list_hotels'),
    path('hotel/<pk>/',HotelList.as_view(),name="list_hotel"),
    path('hotel/', HotelList.as_view(), name="list_hotel"),

    path('hotel/<int:pk>/', api_view_hotel_detail, name='detail_hotel'),
    path('hotel/<int:pk>/update/',api_update_hotel,name='update_hotel'),
    path('hotel/post/',api_post_hotel,name='post_hotel'),
    path('hotel/<int:pk>/delete',api_delete_hotel,name='delete_hotel'),
    path('booking/', api_view_list_bookings, name='list_booking'),
    path('managers', views.api_view_list_managers, name='list_managers'),
    path('guests',views.api_view_list_guests, name='list_guest'),
    path('rooms', views.api_view_list_rooms, name='list_room'),
    path('bookings', views.api_view_list_bookings, name='list_booking'),
]

