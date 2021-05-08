# -*- coding: utf-8 -*-

def hash_mac(data, key=None):
    if key is None or not key:
        from app import AUTH_KEY
        key = AUTH_KEY
    import hmac
    return hmac.new(data.encode(), key.encode()).hexdigest()

def is_email(email):
    email = email.strip()
    if not email or not ('@' in email):
        return False

    import re
    if re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email):
        return True
    return False

def is_async(req):
    request_xhr_key = req.headers.get('X-Requested-With')
    if request_xhr_key and request_xhr_key.lower() == 'xmlhttprequest':
        return True
    return False

def is_logged(req):
    from app import AUTH_COOKIE_NAME
    _auth_cookie = req.cookies.get(AUTH_COOKIE_NAME)
    if not _auth_cookie:
        return None

    _eles = _auth_cookie.split("|")
    if len(_eles) != 3:
        return None

    _expired = _eles[1].strip()
    import time
    if _expired and int(_expired) < int(time.time()):
        return None

    _key = hash_mac(_eles[0] + "|" +  _expired)
    _hash = hash_mac(_eles[0] + "|" + _expired, _key)
    if _hash != _eles[2]:
        return None

    from ..models.user import User
    _user = User.query.filter(User.username == _eles[0]).first()
    if not bool(_user):
        return None

    return _user

