from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserRole, ResourceActionTypeRole
from decorators import check_user_exists, check_action_type_exists, check_resource_exists, check_role_exists


@api_view(['POST'])
@check_user_exists
@check_role_exists
def user_role_assign(request):
    user = request.user
    role = request.role
    if UserRole.objects.filter(user=user, role=role).exists():
        return Response({'status': False, 'message': 'User role already exist'}, status=HTTP_400_BAD_REQUEST)

    UserRole.objects.create(user=user, role=role)

    return Response({'status': True, 'message': 'User role successfully assigned'})


@api_view(['POST'])
@check_user_exists
@check_role_exists
def user_role_remove(request):
    user = request.user
    role = request.role

    if not UserRole.objects.filter(user=user, role=role).exists():
        return Response({'status': False, 'message': 'User role does not exist'}, status=HTTP_400_BAD_REQUEST)

    UserRole.objects.filter(user=user, role=role).delete()

    return Response({'status': True, 'message': 'User role successfully removed'})


@api_view(['GET'])
@check_user_exists
@check_resource_exists
@check_action_type_exists
def user_access_check_for_action_type_and_resource(request):
    user = request.user
    resource = request.resource
    action_type = request.action_type

    user_role_ids = ResourceActionTypeRole.objects.filter(resource=resource, action_type=action_type).\
        values_list('role__role_of_user_roles__user__id', flat=True)

    user_access_check = user.id in user_role_ids

    return Response({'status': True, 'user_access_check': user_access_check})
