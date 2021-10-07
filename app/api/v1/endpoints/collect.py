from typing import Any

from fastapi import APIRouter, Query, Body, Request
from app.utils import request_parse


router = APIRouter()


@router.post("/")
async def collect_event(
    request: Request,
    v: str = Query('', min_length=1, description="The version of the log client library."),
    tid: str = Query('', title="", min_length=36, description="A unique value for the event. Used to filter duplicate events."),
    sid: str = Query('', min_length=36, description="User session uuid, should expire on the client after 10 minutes of no user action."),
    sdid: str = Query('', min_length=36, description="User session uuid. Unlike sid, it is a device-dependent value that does not have an expiration time."),
    cid: str = Query('', min_length=20, description="This is the client key issued by the Lubycon DevOps Guild. Each team has a unique value."),
    pl: str = Query('', min_length=10, description="The full url of the page where the event occurred"),
    an: str = Query('', min_length=3, description="The name of the application. It is for classification of web, app, admin, etc."),
    ett: int = Query('', g=1633000000, l=2548000000, description="The timestamp value at which the event occurred. must be sent to KST"),
    view: str = Body('', description="The name of the page the user is viewing."),
    action: str = Body('', description="An alias for a user action. For example, 'click', 'impression'"),
) -> Any:
    """
    [Client Event Log Collection API]
    - Loaded into Big Query asynchronously through the data pipeline.
    - The collected data can be visualized and analyzed through BI tools provided by DevOps Guild.
    """
    body = await request.json()
    data = {
        'v': v,
        'tid': tid,
        'sid': sid,
        'sdid': sdid,
        'cid': cid,
        'pl': pl,
        'an': an,
        'ett': ett,
        'view': view,
        'action': action,
        'ch': request.client.host,
        'rf': request.headers.get('referer'),
        **await request_parse.get_user_agent_data(request.headers.get('user-agent', '')),
        **body,
    }
    data = await request_parse.dict_values_convert_string(data)

    return {
        "message": "success",
        "data": data,
    }
