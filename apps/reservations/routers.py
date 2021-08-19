from rest_framework import routers

from .views import ClientViewSet, RoomViewSet, ReservationViewSet, InvoiceViewSet

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet, basename='clients')
router.register(r'rooms', RoomViewSet, basename='rooms')
router.register(r'reservations', ReservationViewSet, basename='reservations')
router.register(r'invoices', InvoiceViewSet, basename='invoices')

urlpatterns = router.urls
