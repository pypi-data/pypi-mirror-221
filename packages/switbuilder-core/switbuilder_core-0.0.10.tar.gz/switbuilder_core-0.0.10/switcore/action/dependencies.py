from starlette.requests import Request

from switcore.action.schemas import SwitRequest


async def get_swit_request(
        request: Request,
):
    res: dict = await request.json()
    return SwitRequest(**res)
