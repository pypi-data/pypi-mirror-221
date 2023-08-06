import base64
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional, Type

from nonebot.adapters import Bot as BaseBot
from nonebot.message import event_postprocessor
from nonebot.typing import overrides
from nonebot_plugin_datastore import create_session

from ..config import plugin_config
from ..consts import (
    IMAGE_CACHE_DIR,
    RECORD_CACHE_DIR,
    VIDEO_CACHE_DIR,
    SupportedAdapter,
)
from ..message import (
    JsonMsg,
    MessageDeserializer,
    MessageSerializer,
    register_deserializer,
    register_serializer,
    serialize_message,
)
from ..model import MessageRecord

try:
    from nonebot.adapters.onebot.v11 import (
        Bot,
        GroupMessageEvent,
        Message,
        MessageEvent,
        MessageSegment,
    )

    @event_postprocessor
    async def record_recv_msg(bot: Bot, event: MessageEvent):
        record = MessageRecord(
            bot_type=bot.type,
            bot_id=bot.self_id,
            platform="qq",
            time=datetime.utcfromtimestamp(event.time),
            type=event.post_type,
            detail_type=event.message_type,
            message_id=str(event.message_id),
            message=serialize_message(bot, event.message),
            plain_text=event.message.extract_plain_text(),
            user_id=str(event.user_id),
            group_id=str(event.group_id)
            if isinstance(event, GroupMessageEvent)
            else None,
        )

        async with create_session() as session:
            session.add(record)
            await session.commit()

    if plugin_config.chatrecorder_record_send_msg:

        @Bot.on_called_api
        async def record_send_msg(
            bot: BaseBot,
            e: Optional[Exception],
            api: str,
            data: Dict[str, Any],
            result: Optional[Dict[str, Any]],
        ):
            if e or not result:
                return
            if api not in ["send_msg", "send_private_msg", "send_group_msg"]:
                return

            if api == "send_group_msg" or (
                api == "send_msg"
                and (
                    data.get("message_type") == "group"
                    or (data.get("message_type") == None and data.get("group_id"))
                )
            ):
                detail_type = "group"
            else:
                detail_type = "private"

            message = Message(data["message"])
            record = MessageRecord(
                bot_type=bot.type,
                bot_id=bot.self_id,
                platform="qq",
                time=datetime.utcnow(),
                type="message_sent",
                detail_type=detail_type,
                message_id=str(result["message_id"]),
                message=serialize_message(bot, message),
                plain_text=message.extract_plain_text(),
                user_id=str(bot.self_id),
                group_id=str(data.get("group_id", "")) or None,
            )

            async with create_session() as session:
                session.add(record)
                await session.commit()

    def cache_b64_msg(msg: Message):
        for seg in msg:
            if seg.type == "image":
                cache_b64_msg_seg(seg, IMAGE_CACHE_DIR)
            elif seg.type == "record":
                cache_b64_msg_seg(seg, RECORD_CACHE_DIR)
            elif seg.type == "video":
                cache_b64_msg_seg(seg, VIDEO_CACHE_DIR)

    def cache_b64_msg_seg(seg: MessageSegment, cache_dir: Path):
        def replace_seg_file(path: Path):
            seg.data["file"] = f"file:///{path.resolve()}"

        file = seg.data.get("file", "")
        if not file or not file.startswith("base64://"):
            return

        data = base64.b64decode(file.replace("base64://", ""))
        hash = hashlib.md5(data).hexdigest()
        filename = f"{hash}.cache"
        cache_file_path = cache_dir / filename
        cache_files = [f.name for f in cache_dir.iterdir() if f.is_file()]
        if filename in cache_files:
            replace_seg_file(cache_file_path)
        else:
            with cache_file_path.open("wb") as f:
                f.write(data)
            replace_seg_file(cache_file_path)

    class Serializer(MessageSerializer[Message]):
        @classmethod
        @overrides(MessageSerializer)
        def serialize(cls, msg: Message) -> JsonMsg:
            cache_b64_msg(msg)
            return super().serialize(msg)

    class Deserializer(MessageDeserializer[Message]):
        @classmethod
        @overrides(MessageDeserializer)
        def get_message_class(cls) -> Type[Message]:
            return Message

    adapter = SupportedAdapter.onebot_v11
    register_serializer(adapter, Serializer)
    register_deserializer(adapter, Deserializer)

except ImportError:
    pass
