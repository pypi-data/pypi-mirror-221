from __future__ import annotations

from functools import wraps
from v7e_utils.agil_connect.token import Token


def with_token(function, api_key:str | None=None, api_key_prefix:str='Api-Key'):
    """
    Set token of Authorization in request agil
    """
    
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            authorization = request.headers.get('Authorization', None)
            token = Token()
            if api_key:
                token.set_token(f'{api_key_prefix} {api_key}')
            elif authorization:
                token.set_token(authorization)
            return view_func(request, *args, **kwargs)
        return _wrapped_view

    return decorator