from fastapi import APIRouter

message_route = APIRouter()

@message_route.route("/{id}")
def _get_message():
    pass