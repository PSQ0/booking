200     success
201     created
400     request not valid
401     auth
403     permission
404     not found
405     method not allowd(get, post)
500     server side error


Client
  |
  | HTTP GET /api/v1/services/
  |
  v
Django URL Router
  |
  v
ServicesListAPIView
  |
  v
ServiceOffering.objects.filter(...)
  |
  v
ServiceOfferingSerializer(..., many=True)
  |
  v
serializer.data
  |
  v
DRF Response + JSON Renderer
  |
  v
HTTP 200 + JSON

-----------------

User
ProviderProfile
ServiceOffering
AvailabilitySlot
Booking