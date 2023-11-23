from apis_acdhch_default_settings.urls import urlpatterns
from django.urls import path, include
from .views import CustomReferenceDetailView, TempTripleAutocomplete, TempEntityClassAutocomplete, CustomReferenceDeleteView
from .api import ReferenceViewSet, LabelViewSet
from django.contrib.auth.decorators import login_required
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'references', ReferenceViewSet)
router.register(r'labels', LabelViewSet)

customurlpatterns = [
    path("bibsonomy/references/<int:pk>", login_required(CustomReferenceDetailView.as_view()), name='referencedetail'),
    path('bibsonomy/tempentityclass-autocomplete/', TempEntityClassAutocomplete.as_view(), name="tempentityclass-autocomplete",),
    path('bibsonomy/temptriple-autocomplete/', TempTripleAutocomplete.as_view(), name="temptriple-autocomplete",),
    path('bibsonomy/references/<int:pk>/delete', login_required(CustomReferenceDeleteView.as_view()), name='referencedelete'),
]
urlpatterns = customurlpatterns + urlpatterns + [ path('custom/api/', include(router.urls)) ]
