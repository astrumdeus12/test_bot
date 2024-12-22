from ...dto.request_model import RequestSchema
from ..settings import get_async_session
from ..models.request_model import Request




async def create_request(new_request : RequestSchema):
    async for session in get_async_session():
        async with session.begin():
            request = Request(user_tg_id = new_request.user_tg_id, message = new_request.message, answer = new_request.answer)
            session.add(request)
            await session.commit()