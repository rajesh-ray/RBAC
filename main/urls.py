from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .views import user_role_assign, user_role_remove, user_access_check_for_action_type_and_resource

router = DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    url(r'^user_role_assign/$', user_role_assign),
    url(r'^user_role_remove/$', user_role_remove),
    url(r'^user_access_check_for_action_type_and_resource/$', user_access_check_for_action_type_and_resource),
]
