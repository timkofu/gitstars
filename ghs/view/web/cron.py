
import os
import re

from starlette.requests import Request
from starlette.endpoints import HTTPEndpoint
from starlette.exceptions import HTTPException
from starlette.responses import PlainTextResponse

from ghs.controller.stars.update import Update


class UpdateStars(HTTPEndpoint):  # type: ignore

    async def get(self, request: Request) -> PlainTextResponse:

        cron_auth_token: str = request.path_params.get('cron_auth_token')

        if cron_auth_token and (cron_auth_token == os.getenv('CRON_AUTH_TOKEN')):
            await Update().stars()
            return PlainTextResponse("1")
        else:
            raise HTTPException(403, detail='Invalid auth token.')
