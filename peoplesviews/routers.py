from rest_framework import routers
from choose.viewsets import ChoiceViewSet

router = routers.DefaultRouter()

router.register('choice', ChoiceViewSet)
