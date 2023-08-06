from datetime import datetime
from functools import wraps

import jwt
import pytz
from jwt import DecodeError
from rest_framework import status
from rest_framework.response import Response

from common_bidso.utils.datetime import parse_iso_format


def jwt_login_required(allowed_user_types=None, email_verif_required=False):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(self, request, *args, **kwargs):
            try:
                try:
                    token = request.META["HTTP_BEARER"]
                except KeyError:
                    return Response(
                        {
                            "message": "JWT token missing",
                            "status": "error",
                            "response": None,
                        },
                        status.HTTP_401_UNAUTHORIZED,
                    )

                with open("authbidso/apps/common/data/public_key.pem", "rb") as file:
                    public_key = file.read()

                decoded_token = jwt.decode(token, public_key, algorithms=["RS256"])

                user = decoded_token["user"]
                expire_dt = decoded_token["expires_at"]

                if datetime.now(tz=pytz.UTC) >= parse_iso_format(expire_dt):
                    return Response(
                        {
                            "message": "Token expired",
                            "status": "error",
                            "response": None,
                        },
                        status.HTTP_401_UNAUTHORIZED,
                    )

                if not user or user.get("user_type") is None:
                    return Response(
                        {
                            "message": "Invalid Token",
                            "status": "error",
                            "response": None,
                        },
                        status.HTTP_401_UNAUTHORIZED,
                    )

                if allowed_user_types is not None and user.get("user_type") not in allowed_user_types:
                    return Response(
                        {
                            "message": "Unauthorized access of {}, method only allows {}".format(
                                user.get("user_type"), ", ".join(allowed_user_types)
                            ),
                            "status": "error",
                            "response": None,
                        },
                        status.HTTP_401_UNAUTHORIZED,
                    )

                if email_verif_required and not user.get("email_verified"):
                    return Response(
                        {
                            "message": "email id not verified",
                            "status": "error",
                            "response": None,
                        },
                        status.HTTP_401_UNAUTHORIZED,
                    )

                return view_func(self, request, *args, **kwargs, user = user)
            except DecodeError:
                return Response(
                    {"message": "Invalid Token", "status": "error", "response": None},
                    status.HTTP_401_UNAUTHORIZED,
                )

        return wrapper

    return decorator
