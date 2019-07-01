from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from models import User, ActionType, Resource, Role


def check_user_exists(callback):
    def wrapper(*args, **kwargs):
        request = None
        for argument in args:
            if isinstance(argument, Request):
                request = argument
                break

        if request.method == 'GET':
            user_id = request.query_params.get('user_id')
        else:
            user_id = request.data.get('user_id')

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'status': False, 'message': 'User role does not exist'}, status=HTTP_400_BAD_REQUEST)

        request.user = user

        return callback(*args, **kwargs)

    return wrapper


def check_action_type_exists(callback):
    def wrapper(*args, **kwargs):
        request = None
        for argument in args:
            if isinstance(argument, Request):
                request = argument
                break

        if request.method == 'GET':
            action_type_id = request.query_params.get('action_type_id')
        else:
            action_type_id = request.data.get('action_type_id')

        try:
            action_type = ActionType.objects.get(id=action_type_id)
        except ActionType .DoesNotExist:
            return Response({'status': False, 'message': 'Action Type does not exist'}, status=HTTP_400_BAD_REQUEST)

        request.action_type = action_type

        return callback(*args, **kwargs)

    return wrapper


def check_resource_exists(callback):
    def wrapper(*args, **kwargs):
        request = None
        for argument in args:
            if isinstance(argument, Request):
                request = argument
                break

        if request.method == 'GET':
            resource_id = request.query_params.get('resource_id')
        else:
            resource_id = request.data.get('resource_id')

        try:
            resource = Resource.objects.get(id=resource_id)
        except Resource.DoesNotExist:
            return Response({'status': False, 'message': 'Resource does not exist'}, status=HTTP_400_BAD_REQUEST)

        request.resource = resource

        return callback(*args, **kwargs)

    return wrapper


def check_role_exists(callback):
    def wrapper(*args, **kwargs):
        request = None
        for argument in args:
            if isinstance(argument, Request):
                request = argument
                break

        if request.method == 'GET':
            role_id = request.query_params.get('role_id')
        else:
            role_id = request.data.get('role_id')

        try:
            role = Role.objects.get(id=role_id)
        except Role.DoesNotExist:
            return Response({'status': False, 'message': 'Role does not exist'}, status=HTTP_400_BAD_REQUEST)

        request.role = role

        return callback(*args, **kwargs)

    return wrapper

