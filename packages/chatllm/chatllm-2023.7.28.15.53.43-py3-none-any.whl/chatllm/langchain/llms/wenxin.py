#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : wenxin
# @Time         : 2023/7/28 14:58
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :
from langchain.chat_models.base import BaseChatModel
from langchain.schema import BaseMessage, ChatResult, HumanMessage, AIMessage, SystemMessage, ChatMessage, \
    ChatGeneration

from meutils.pipe import *

from openai.api_resources.chat_completion import ChatCompletion as _ChatCompletion

import time

from openai import util
from openai.error import TryAgain
class ChatCompletion(_ChatCompletion):

    @classmethod
    def create(cls, *args, **kwargs):
        """
        Creates a new chat completion for the provided messages and parameters.

        See https://platform.openai.com/docs/api-reference/chat-completions/create
        for a list of valid parameters.
        """
        start = time.time()
        timeout = kwargs.pop("timeout", None)

        while True:
            try:
                return super().create(*args, **kwargs)
            except TryAgain as e:
                if timeout is not None and time.time() > start + timeout:
                    raise

                util.log_info("Waiting for model to warm up", error=e)
