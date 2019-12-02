from app.lib.core.remote_call import fetch

from app.config import CALLBACK


async def trigger_callback(payload):
    """ trigger callback to many urls """
    results = []
    callbacks = CALLBACK["URLS"].split(",")
    for callback in callbacks:
        request = {"url": callback, "method": "POST", "json": payload}
        response, status_code = await fetch(request)
        results.append(status_code)
    return results