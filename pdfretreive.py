from musescore_scraper import MuseScraper
url = "https://musescore.com/perpetuality/scores/6782724"
#
def getPDF(url):
    with MuseScraper() as ms:
        pth = ms.to_pdf(url, output = "./pdf")
    return pth
#
#
# from musescore_scraper import AsyncMuseScraper
# from typing import Optional, List
# import asyncio
# from functools import partial
# from pathlib import Path as path_mod
#
# async def main(nmurl):
#     url = nmurl
#     Path = path_mod('./pdf')
#     urls: List[str] = [url]
#     outputs: List[Optional[None]] = [None] * len(urls)
#
#     def set_output(i: int, task: asyncio.Task) -> None:
#         outputs[i] = task.result()
#
#     async def run():
#         tasks: List[asyncio.Task] = []
#
#         async with AsyncMuseScraper() as ms:
#             for i in range(len(urls)):
#                 task: asyncio.Task = asyncio.create_task(ms.to_pdf(urls[i]))
#                 task.add_done_callback(partial(set_output, i))
#                 tasks.append(task)
#
#             result = await asyncio.gather(*tasks)
#
#         return result
#
#     asyncio.get_event_loop().run_until_complete(run())