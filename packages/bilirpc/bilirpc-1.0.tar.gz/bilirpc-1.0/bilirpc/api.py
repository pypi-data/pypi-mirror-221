# -*- coding: UTF-8 -*-
"""
@File    :   BiliRpc -> api.py
@IDE     :   PyCharm
@Time    :   2022/9/23 17:34
@Author  :   DMC ,
"""
from typing import Optional

import grpc

from bilibili.app.dynamic.v2.dynamic_pb2 import (
    DynAllReq,
    DynamicType,
    DynSpaceReq,
    DynDetailReq,
    RepostListReq,
    PlayerArgs
)
from loguru import logger
from google.protobuf.json_format import MessageToJson

from bilibili.app.dynamic.v2.dynamic_pb2_grpc import DynamicStub
from bilirpc.tools import fakebuvid, make_metadata


async def get_follow_dynamic(update_baseline: Optional[str] = None, access_token: str = None):
    try:
        async with grpc.aio.secure_channel(
                "grpc.biliapi.net",
                grpc.ssl_channel_credentials()) as channel:
            stub = DynamicStub(channel=channel)
            if update_baseline:
                req = DynAllReq(
                    update_baseline=update_baseline, refresh_type=1)
            else:
                req = DynAllReq()
            resp = await stub.DynAll(req, metadata=make_metadata(buvid=fakebuvid(),
                                                                 access_token=access_token))
            exclude_list = [
                DynamicType.ad,
                DynamicType.live,
                DynamicType.live_rcmd,
                DynamicType.banner,
            ]
            dynamic_list = [
                dyn for dyn in resp.dynamic_list.list if dyn.card_type not in exclude_list
            ]
            return dynamic_list
    except Exception as e:
        return


async def get_dy_detail(dynamic_id):
    try:
        async with grpc.aio.secure_channel("grpc.biliapi.net",grpc.ssl_channel_credentials()) as channel:
            stub = DynamicStub(channel=channel)
            req = DynDetailReq(dynamic_id=dynamic_id,local_time=8)
            result = await stub.DynDetail(req, metadata=make_metadata(buvid=fakebuvid()))
            return result
    except Exception as e:
        logger.exception(e)
        return None

async def get_space_dynamic(uid):
    try:
        async with grpc.aio.secure_channel(
                "grpc.biliapi.net",
                grpc.ssl_channel_credentials()) as channel:
            stub = DynamicStub(channel=channel)
            req = DynSpaceReq(host_uid=uid, local_time=8)
            result = await stub.DynSpace(req, metadata=make_metadata(buvid=fakebuvid()))
            return result.list
    except Exception as e:
        return None


# async def main():
#     dynamic = await get_dy_detail("822264737156825136")
#     result =  await formate_message("grpc",json.loads(MessageToJson(dynamic.item)))
#     # dynamic = await get_space_dynamic(688053738)
#     print(result)

# if __name__ == "__main__":
#     import asyncio
#     import json
#     from dynamicadaptor.DynamicConversion import formate_message
    
#     asyncio.run(main())
