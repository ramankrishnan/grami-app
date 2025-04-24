from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.utils.websocket_manager import ws_manager

router = APIRouter()

@router.websocket("/ws/driver")
async def driver_ws(websocket: WebSocket):
    await ws_manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()  # Optional: receive pings/messages
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)
