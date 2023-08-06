from django.urls import path
from .views import CirclesJoinableViewset, CirclesRequestableViewset, CircleAccessRequestServerNotificationView, CircleAccessRequestFilteredByUserViewSet
from .models import Circle, CircleAccessRequest
from djangoldp.models import Model


urlpatterns = [
    path('circles/joinable/', CirclesJoinableViewset.urls(model_prefix="circles-joinable",
        model=Circle,
        lookup_field=Model.get_meta(Circle, 'lookup_field', 'pk'),
        permission_classes=Model.get_meta(Circle, 'permission_classes', []),
        fields=Model.get_meta(Circle, 'serializer_fields', []),
        nested_fields=Model.get_meta(Circle, 'nested_fields', []))),
    path('circles/requestable/', CirclesRequestableViewset.urls(model_prefix="circles-requestable",
        model=Circle,
        lookup_field=Model.get_meta(Circle, 'lookup_field', 'pk'),
        permission_classes=Model.get_meta(Circle, 'permission_classes', []),
        fields=Model.get_meta(Circle, 'serializer_fields', []),
        nested_fields=Model.get_meta(Circle, 'nested_fields', []))),
    path('circleaccessrequests/inbox/', CircleAccessRequestServerNotificationView.as_view(), name='circle-notifications-inbox'),
    path('circleaccessrequests/me/', CircleAccessRequestFilteredByUserViewSet.urls(model_prefix="circlesaccessrequests-me",
        model=CircleAccessRequest,
        lookup_field=Model.get_meta(CircleAccessRequest, 'lookup_field', 'pk'),
        permission_classes=Model.get_meta(CircleAccessRequest, 'permission_classes', []),
        fields=Model.get_meta(CircleAccessRequest, 'serializer_fields', []),
        nested_fields=Model.get_meta(CircleAccessRequest, 'nested_fields', []))),
]
