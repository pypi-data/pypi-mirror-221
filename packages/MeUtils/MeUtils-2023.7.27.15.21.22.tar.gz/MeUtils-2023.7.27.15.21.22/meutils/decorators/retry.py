#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : MeUtils.
# @File         : retry
# @Time         : 2021/3/18 2:57 下午
# @Author       : yuanjie
# @WeChat       : 313303303
# @Software     : PyCharm
# @Description  : 
from meutils.pipe import *
from tenacity import retry, wait_fixed, stop_after_attempt, wait_exponential, retry_if_exception_type, before_sleep_log
import logging

logger = logging.getLogger(__name__)


# def embed_with_retry(embeddings: OpenAIEmbeddings, **kwargs: Any) -> Any:
#     """Use tenacity to retry the embedding call."""
#     retry_decorator = _create_retry_decorator(embeddings)
#
#     @retry_decorator
#     def _embed_with_retry(**kwargs: Any) -> Any:
#         response = embeddings.client.create(**kwargs)
#         return _check_response(response)
#
#     return _embed_with_retry(**kwargs)
def create_retry_decorator() -> Callable[[Any], Any]:  # todo: Retrying
    """
    @create_retry_decorator()
    def fn():
        pass

    :return:
    """
    import openai
    max_retries = 3
    min_seconds = 4
    max_seconds = 10
    # Wait 2^x * 1 second between each retry starting with
    # 4 seconds, then up to 10 seconds, then 10 seconds afterwards
    return retry(
        reraise=True,
        stop=stop_after_attempt(max_retries),
        wait=wait_exponential(multiplier=1, min=min_seconds, max=max_seconds),
        retry=(
                retry_if_exception_type(openai.error.Timeout)
                | retry_if_exception_type(openai.error.APIError)
                | retry_if_exception_type(openai.error.APIConnectionError)
                | retry_if_exception_type(openai.error.RateLimitError)
                | retry_if_exception_type(openai.error.ServiceUnavailableError)
        ),
        before_sleep=before_sleep_log(logger, 30),
    )


def wait_retry(n=3):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        @retry(wait=wait_fixed(n))
        def wait():
            logger.warning("retry")
            if wrapped(*args, **kwargs):  # 知道检测到True终止
                return True

            raise Exception

        return wait()

    return wrapper


# from meutils.cmds import HDFS
# HDFS.check_path_isexist()


if __name__ == '__main__':
    s = time.time()  # 1616145296
    print(s)
    e1 = s + 10
    e2 = e1 + 10


    @wait_retry(5)
    def f(e):
        return time.time() > e  # 变的


    def run(e):
        f(e)
        print(f"task {e}")


    # for e in [e2, e1]:
    #     print(run(e))
    #
    # print("耗时", time.time() - s)

    [e1, e2, 1000000000000] | xProcessPoolExecutor(run, 2)
