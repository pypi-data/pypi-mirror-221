"""Download webtoons automatiallly or easily"""

import asyncio
import contextlib
from itertools import starmap

if __name__ == "__main__":
    from NaverWebtoonScraper import NaverWebtoonScraper
    from FolderManager import FolderManager
    from WebtoonOriginalsScraper import WebtoonOriginalsScraper
    from BestChallengeScraper import BestChallengeScraper
    from WebtoonCanvasScraper import WebtoonCanvasScraper
    from TelescopeScraper import TelescopeScraper
    from BufftoonScraper import BufftoonScraper
    from NaverPostScraper import NaverPostScraper
    from NaverGameScraper import NaverGameScraper
else:
    from .NaverWebtoonScraper import NaverWebtoonScraper
    from .FolderManager import FolderManager
    from .WebtoonOriginalsScraper import WebtoonOriginalsScraper
    from .BestChallengeScraper import BestChallengeScraper
    from .WebtoonCanvasScraper import WebtoonCanvasScraper
    from .TelescopeScraper import TelescopeScraper
    from .BufftoonScraper import BufftoonScraper
    from .NaverPostScraper import NaverPostScraper
    from .NaverGameScraper import NaverGameScraper

N = NAVER_WEBTOON = 'naver_webtoon'
B = BEST_CHALLENGE = 'best_challenge'
O = ORIGINALS = 'originals'
C = CANVAS = 'canvas'
T = M = TELESCOPE = 'telescope'
BF = BUFFTOON = 'bufftoon'
P = POST = NAVER_POST = 'naver_post'
G = NAVER_GAME = 'naver_game'


async def get_webtoon_platform(webtoon_id: int, is_auto_select=False) -> str:
    # sourcery skip: low-code-quality
    """If webtoon is best challenge, this returns True. Otherwise, False."""
    loop = asyncio.get_running_loop()

    async def skip_when_errored(func, platform_name):
        try:
            # await func()
            await loop.run_in_executor(None, lambda: asyncio.run(func()))
            # print(f'Complete {platform_name}')
        except Exception as e:
            print(f'An error occured. Skipping {platform_name}')
            print(f'error: {e}')

    available_webtoon = []
    # 네이버 게임은 제목을 받는 데 특수한 함수가 필요하기 때문에 이 클래스를 이용
    webtoonscraper = NaverGameScraper()

    # 네이버 웹툰
    async def naver_webtoon_fetch():
        title = await webtoonscraper.get_internet('soup_select_one', f'https://comic.naver.com/webtoon/detail?titleId={webtoon_id}', 'span.text')
        with contextlib.suppress(AttributeError):
            title = title.text
            if title:
                available_webtoon.append((NAVER_WEBTOON, title))
    # await skip_when_errored(naver_webtoon_fetch, NAVER_WEBTOON)

    # 베스트 도전
    async def best_challenge_fetch():
        title = await webtoonscraper.get_internet('soup_select_one', f'https://comic.naver.com/bestChallenge/list?titleId={webtoon_id}',
                                                  'meta[property="og:title"]')
        with contextlib.suppress(AttributeError):
            title = title.get('content')
            if title:
                available_webtoon.append((BEST_CHALLENGE, title))
    # await skip_when_errored(best_challenge_fetch, BEST_CHALLENGE)

    # 만화경
    async def telescope_fetch():
        title = await webtoonscraper.get_internet('soup_select_one', f'https://www.manhwakyung.com/title/{webtoon_id}', 'meta[property="og:title"]')
        title = title["content"][:-6]
        title = None if title == "에러 페이지" else title
        if title:
            available_webtoon.append((TELESCOPE, title))
    # await skip_when_errored(telescope_fetch, TELESCOPE)

    # 버프툰
    async def bufftoon_fetch():
        title = await webtoonscraper.get_internet('soup_select_one', f'https://bufftoon.plaync.com/series/{webtoon_id}', 'meta[property="og:title"]')
        title = title["content"]
        title = None if title == "이야기 던전에 입장하라, 버프툰" else title
        if title:
            available_webtoon.append((BUFFTOON, title))
    # await skip_when_errored(bufftoon_fetch, BUFFTOON)

    # 네이버 게임
    async def naver_game_fetch():
        with contextlib.suppress(Exception):
            title, _ = await webtoonscraper._get_webtoon_infomation(webtoon_id)
            if title:
                available_webtoon.append((NAVER_GAME, title))
        webtoonscraper.IS_STABLE_CONNECTION = False
    # await skip_when_errored(naver_game_fetch, NAVER_GAME)

    # originals
    async def originals_fetch():
        title = await webtoonscraper.get_internet('soup_select_one', f'https://www.webtoons.com/en/fantasy/watermelon/list?title_no={webtoon_id}',
                                                  'meta[property="og:title"]')
        if title:
            available_webtoon.append((ORIGINALS, title))
    # await skip_when_errored(originals_fetch, ORIGINALS)

    # canvas
    async def canvas_fetch():
        title = await webtoonscraper.get_internet('soup_select_one', f'https://www.webtoons.com/en/challenge/meme-girls/list?title_no={webtoon_id}',
                                                  'meta[property="og:title"]')
        with contextlib.suppress(AttributeError):
            if title := title.get('content'):
                available_webtoon.append((CANVAS, title))

    # 전체 동시 실행
    webtoon_getters = starmap(
        skip_when_errored,
        (
            (naver_webtoon_fetch, NAVER_WEBTOON),
            (best_challenge_fetch, BEST_CHALLENGE),
            (telescope_fetch, TELESCOPE),
            (bufftoon_fetch, BUFFTOON),
            (naver_game_fetch, NAVER_GAME),
            (originals_fetch, ORIGINALS),
            (canvas_fetch, CANVAS)
        )
    )
    await asyncio.gather(*webtoon_getters)

    # 베스트 도전과 네이버 웹툰이 겹치고 둘의 제목이 같을 경우 베스트 도전을 배제함.
    for i, (platform, title) in enumerate(available_webtoon):
        if platform == NAVER_WEBTOON:
            nw_title = title
        if platform == BEST_CHALLENGE:
            bc_title = title
            bc_order = i
    with contextlib.suppress(UnboundLocalError):
        if nw_title == bc_title:
            del available_webtoon[bc_order]

    if (webtoon_length := len(available_webtoon)) == 1:
        print(f'Webtoon\'s platform is assumed to be {available_webtoon[0][0]}')
        return available_webtoon[0][0]
    elif webtoon_length == 0:
        print(f'There\'s no webtoon that webtoon ID is {webtoon_id}.')
    else:
        for i, (platform, name) in enumerate(available_webtoon, 1):
            print(f'{i}. {platform}: {name}')
        try:
            if not is_auto_select:
                platform_no = input('Multiple webtoon is searched. Please type number of webtoon you want to download(enter nothing to select no.1): ')
            else:
                platform_no = ''
            platform_no = 1 if platform_no == '' else int(platform_no)
            try:
                selected_platform, selected_webtoon = available_webtoon[platform_no - 1]
            except IndexError:
                print('Exceeded the range of webtoons.')
            print(f'Webtoon {selected_webtoon} is selected.')
            return selected_platform
        except ValueError as e:
            raise ValueError('Webtoon ID should be integer.') from e


async def get_scraper_instance(webtoon_type: str):
    if webtoon_type.lower() == NAVER_WEBTOON:
        webtoonscraper = NaverWebtoonScraper()
    elif webtoon_type.lower() == BEST_CHALLENGE:
        webtoonscraper = BestChallengeScraper()
    elif webtoon_type.lower() == ORIGINALS:
        webtoonscraper = WebtoonOriginalsScraper()
    elif webtoon_type.lower() == CANVAS:
        webtoonscraper = WebtoonCanvasScraper()
    elif webtoon_type.lower() == TELESCOPE:
        webtoonscraper = TelescopeScraper()
    elif webtoon_type.lower() == BUFFTOON:
        webtoonscraper = BufftoonScraper()
    elif webtoon_type.lower() == NAVER_POST:
        webtoonscraper = NaverPostScraper()
    elif webtoon_type.lower() == NAVER_GAME:
        webtoonscraper = NaverGameScraper()
    else:
        raise ValueError('webtoon_type should be among naver_webtoon, best_challenge, originals, canvas, telescope, and naver_game.')
    return webtoonscraper


async def get_webtoon_async(
        webtoon_id: int,
        webtoon_type: None | str = None,
        *,
        merge: None | int = None,
        cookie: None | str = None,
        member_no: None | int = None,
        is_auto_select=False
) -> None:

    if webtoon_type is None:
        webtoon_type = await get_webtoon_platform(webtoon_id, is_auto_select)
    webtoonscraper = await get_scraper_instance(webtoon_type)
    if webtoon_type.lower() == BUFFTOON or cookie is not None:
        if cookie is None:
            webtoonscraper.COOKIE = cookie
        else:
            webtoonscraper.COOKIE = input(f'Enter cookie of {webtoon_id} (Enter nothing to proceed without cookie): ')
    if webtoon_type.lower() == NAVER_POST or member_no is not None:
        if not member_no:
            member_no = int(input(f'Enter memberNo of {webtoon_id}: '))
        await webtoonscraper.download_one_webtoon_async(titleid=webtoon_id, member_no=member_no)
    else:
        await webtoonscraper.download_one_webtoon_async(titleid=webtoon_id)
    if merge:
        fd = FolderManager()
        fd.merge_webtoon_episodes(webtoonscraper.webtoon_dir)


def get_webtoon(
    webtoon_id: int,
    webtoon_type: str | None = None,
    *,
    merge: None | int | bool = None,
    cookie: None | str = None,
    member_no: None | int = None
) -> None:
    asyncio.run(get_webtoon_async(webtoon_id, webtoon_type, merge=merge, cookie=cookie, member_no=member_no))


if __name__ == '__main__':
    asyncio.run(get_webtoon_platform(18))  # 네이버 게임
