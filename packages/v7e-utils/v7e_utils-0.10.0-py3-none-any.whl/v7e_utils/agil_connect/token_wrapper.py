from __future__ import annotations

from functools import wraps
from v7e_utils.agil_connect.token import Token


def with_token(api_key:str | None=None, api_key_prefix:str='Api-Key'):
    """
    
    """
    
    @wraps(function)
    def decorator(request, *args, **kwargs):
        authorization = request.headers.get('Authorization', None)
        token = Token()
        if api_key:
            token.set_token(f'{api_key_prefix} {api_key}')
        elif authorization:
            token.set_token(authorization)
        return function(request, *args, **kwargs)

    return decorator