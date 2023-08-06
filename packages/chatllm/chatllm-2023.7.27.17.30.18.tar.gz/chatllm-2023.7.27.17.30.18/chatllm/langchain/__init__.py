#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : __init__.py
# @Time         : 2023/6/30 16:37
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :

from meutils.pipe import *
from meutils.cache_utils import diskcache


def init(verbose=-1):
    try:
        import openai
        openai.Embedding.create = set_cache(openai.Embedding.create, verbose=verbose)
    except Exception as e:
        logger.error(e)

    # try:
    #     import dashscope # 返回对象不支持序列化
    #     dashscope.TextEmbedding.call = set_cache(dashscope.TextEmbedding.call, verbose=verbose)
    # except Exception as e:
    #     logger.error(e)

    # 流式会生成不了
    # openai.Completion.create = diskcache(
    #     openai.Completion.create,
    #     location=f"{OPENAI_CACHE}_Completion",
    #     verbose=verbose,
    #     ttl=24 * 3600
    # )
    #
    # openai.ChatCompletion.create = diskcache(
    #     openai.ChatCompletion.create,
    #     location=f"{OPENAI_CACHE}_ChatCompletion",
    #     verbose=verbose,
    #     ttl=24 * 3600
    # )


def set_cache(fn, verbose=-1):
    CACHE = os.getenv("CHATLLM_CACHE", "~/.cache/chatllm_cache")

    location = f"""{CACHE}__{str(fn).split()[-1].replace("'", "").replace(">", "")}"""

    return diskcache(fn, location=location, verbose=verbose)


if __name__ == '__main__':
    init()
    from langchain.embeddings import OpenAIEmbeddings

    print(OpenAIEmbeddings().embed_query(text='chatllm'))
