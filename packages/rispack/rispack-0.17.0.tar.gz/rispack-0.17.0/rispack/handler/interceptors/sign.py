import base64
import hashlib

from ecdsa import VerifyingKey
from ecdsa.util import sigdecode_der

from rispack.cache import GlobalCache
from rispack.handler import Request, Response
from rispack.handler.interceptors import BaseInterceptor
from rispack.logger import logger


class SignInterceptor(BaseInterceptor):
    SETTINGS = {
        "param_name": "sign",
        "header": "X-Signature",
        "required_headers": ["X-Signature", "X-ClientId", "X-RequestTime"],
        "authorizer": "credential_id",
    }

    def __init__(self, sign=None):
        self.cache = GlobalCache.instance()

    def __call__(self, request: Request):
        credential_id = request.authorizer.get(self.SETTINGS["authorizer"])

        for required in self.SETTINGS["required_headers"]:
            headers = [k.lower() for k in request.headers.keys()]

            if required.lower() not in headers:
                return Response.forbidden(f"Unable to locate {required} header")

        cache_key = f"PUBLICKEY#{credential_id}"
        logger.info(f"cache_key: {cache_key}")

        cache = self.cache.get(cache_key)

        if not cache:
            return Response.forbidden(f"Could not find public key")

        public_key = cache.data["public_key"]
        logger.info(public_key)

        message = self._get_message(request)
        logger.info("Message to sign:")
        logger.info(message)

        try:
            signature = self._find_header(request.headers)

            if not signature:
                return Response.forbidden(f"Could not find signature header")

            self._verify_signature(public_key, message, signature)
        except Exception as e:
            logger.error(e)
            return Response.forbidden("Invalid signature")

    def _get_message(self, request):
        return (
            request.headers["X-ClientId"]
            + request.headers["X-RequestTime"]
            + base64.b64encode(request.event["body"].encode()).decode()
        )

    def _verify_signature(self, public_key, message, signature):
        vk = VerifyingKey.from_pem(public_key)

        logger.info(signature)

        vk.verify(
            base64.b64decode(signature),
            message.encode(),
            hashfunc=hashlib.sha256,
            sigdecode=sigdecode_der,
        )

    def _find_header(self, headers):
        for header, value in headers.items():
            if header.lower() == self.SETTINGS["header"].lower():
                return value
