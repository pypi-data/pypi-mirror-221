from rispack.cache import GlobalCache
from rispack.handler import Request, Response
from rispack.handler.interceptors import BaseInterceptor
from rispack.logger import logger


class OtpInterceptor(BaseInterceptor):
    SETTINGS = {
        "param_name": "otp",
        "headers": ["X-Authorization-Otp"],
        "authorizer": "auth_id",
    }

    @classmethod
    def get_param_name(cls):
        return "otp"

    def __init__(self, settings):
        self.cache = GlobalCache.instance()

        if not isinstance(settings, dict):
            return

        if settings.get("authorizer"):
            self.SETTINGS["authorizer"] = settings["authorizer"]

    def __call__(self, request: Request):
        auth_id = request.authorizer.get(self.SETTINGS["authorizer"])
        token = self._find_header(request.headers)

        if not token:
            return Response.forbidden(f"Invalid {self.SETTINGS['header']} header")

        cache_key = f"OTP#{auth_id}"
        cache = self.cache.get(cache_key)

        if not cache:
            return Response.forbidden(f"Could not find otp on global cache")

        otp = cache.data["otp"]

        if otp != token:
            return Response.forbidden("Invalid OTP")

    def _find_header(self, headers):
        valid_headers = [h.lower() for h in self.SETTINGS["headers"]]

        for header, value in headers.items():
            if header.lower() in valid_headers:
                return value
