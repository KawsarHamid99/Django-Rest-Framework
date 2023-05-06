from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

class JsckRateThrottle(UserRateThrottle):
    scope="jack"