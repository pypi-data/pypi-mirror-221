"""Download webtoons automatiallly or easily"""

import asyncio
import contextlib
from itertools import starmap
import logging

if __name__ in ("__main__", "B_Webtoon"):
    from A_FolderManager import FolderManager
    from D_NaverWebtoonScraper import NaverWebtoonScraper
    from E_BestChallengeScraper import BestChallengeScraper
    from F_WebtoonOriginalsScraper import WebtoonOriginalsScraper
    from G_WebtoonCanvasScraper import WebtoonCanvasScraper
    from H_TelescopeScraper import TelescopeScraper
    from I_BufftoonScraper import BufftoonScraper
    from J_NaverPostScraper import NaverPostScraper
    from K_NaverGameScraper import NaverGameScraper
    from L_LezhinComicsScraper import LezhinComicsScraper
else:
    from .A_FolderManager import FolderManager
    from .D_NaverWebtoonScraper import NaverWebtoonScraper
    from .E_BestChallengeScraper import BestChallengeScraper
    from .F_WebtoonOriginalsScraper import WebtoonOriginalsScraper
    from .G_WebtoonCanvasScraper import WebtoonCanvasScraper
    from .H_TelescopeScraper import TelescopeScraper
    from .I_BufftoonScraper import BufftoonScraper
    from .J_NaverPostScraper import NaverPostScraper
    from .K_NaverGameScraper import NaverGameScraper
    from .L_LezhinComicsScraper import LezhinComicsScraper

N = NAVER_WEBTOON = 'naver_webtoon'
B = BEST_CHALLENGE = 'best_challenge'
O = ORIGINALS = 'originals'  # noqa
C = CANVAS = 'canvas'
T = M = TELESCOPE = 'telescope'
BF = BUFFTOON = 'bufftoon'
P = POST = NAVER_POST = 'naver_post'
G = NAVER_GAME = 'naver_game'
L = LEZHIN = 'lezhin'


async def get_webtoon_platform(webtoon_id: int | str, is_auto_select=False) -> str | None:  # noqa
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
    webtoonscraper.IS_STABLE_CONNECTION = False

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
        title = title["content"].removesuffix(' | 만화경')
        title = None if title == "에러 페이지" else title
        if title:
            available_webtoon.append((TELESCOPE, title))
    # await skip_when_errored(telescope_fetch, TELESCOPE)

    # 버프툰
    async def bufftoon_fetch():
        title = (await webtoonscraper.get_internet('soup_select_one', f'https://bufftoon.plaync.com/series/{webtoon_id}', 'meta[property="og:title"]'))
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
        title_original = (await webtoonscraper.get_internet('soup_select_one', f'https://www.webtoons.com/en/fantasy/watermelon/list?title_no={webtoon_id}',
                                                            'meta[property="og:title"]'))
        title = title_original['content'] if title_original is not None else None
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

    # lezhin
    async def lezhin_fetch():
        # 불필요한 페칭 방지: int라면 어차피 lezhin일 수 없음. 이미 앞에서 걸리지긴 하지만 만약을 대비해 준비함.
        if isinstance(webtoon_id, int):
            return

        title = await webtoonscraper.get_internet('soup_select_one', f'https://www.lezhin.com/ko/{webtoon_id}',
                                                  'h2.comicInfo__title')

        if title is None:
            return

        available_webtoon.append((LEZHIN, title.text))

    # 전체 동시 실행
    if isinstance(webtoon_id, int):
        webtoon_getters = starmap(
            skip_when_errored,
            (
                (naver_webtoon_fetch, NAVER_WEBTOON),
                (best_challenge_fetch, BEST_CHALLENGE),
                (telescope_fetch, TELESCOPE),
                (bufftoon_fetch, BUFFTOON),
                (naver_game_fetch, NAVER_GAME),
                (originals_fetch, ORIGINALS),
                (canvas_fetch, CANVAS),
            )
        )
    else:
        logging.info('webtoon_id is string, so it checks if it is lezhin or not.')
        webtoon_getters = starmap(
            skip_when_errored,
            (
                (lezhin_fetch, LEZHIN),
            )
        )

    await asyncio.gather(*webtoon_getters)

    # 베스트 도전과 네이버 웹툰이 겹치고 둘의 제목이 같을 경우 베스트 도전을 배제함.
    nw_title, bc_title, bc_order = None, None, 0
    for i, (platform, title) in enumerate(available_webtoon):
        if platform == NAVER_WEBTOON:
            nw_title = title
        if platform == BEST_CHALLENGE:
            bc_title = title
            bc_order = i
    if nw_title == bc_title != None:  # noqa
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
                raise ValueError('Exceeded the range of webtoons.')
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
    elif webtoon_type.lower() == LEZHIN:
        webtoonscraper = LezhinComicsScraper()
    else:
        raise ValueError('webtoon_type should be among naver_webtoon, best_challenge, originals, canvas, bufftoon, telescope, naver_post, naver_game, and lezhin.')
    return webtoonscraper


async def get_webtoon_async(
        webtoon_id: int | tuple[int, int] | str,
        webtoon_type: None | str = None,
        *,
        merge: None | int = None,
        cookie: None | str = None,
        is_auto_select=False,
        episode_no_range: tuple[int, int] | int | None = None,
        authorization: None | str = None
) -> None:
    def set_cookie(cookie):
        webtoonscraper = BufftoonScraper()
        if cookie:
            webtoonscraper.COOKIE = cookie
        else:
            webtoonscraper.COOKIE = input(f'Enter cookie of {webtoon_id} (Enter nothing to proceed without cookie): ')
        return webtoonscraper

    if cookie is None and authorization is None:
        if isinstance(webtoon_id, tuple):
            webtoon_type = NAVER_POST
        elif webtoon_type is None:
            webtoon_type = await get_webtoon_platform(webtoon_id, is_auto_select)
            if webtoon_type is None:
                raise ValueError('You must select item.')

        if webtoon_type.lower() == BUFFTOON:
            webtoonscraper = set_cookie(cookie)
        else:
            webtoonscraper = await get_scraper_instance(webtoon_type)
    elif cookie is not None:
        webtoonscraper = set_cookie(cookie)
    elif authorization is not None:
        webtoonscraper = LezhinComicsScraper()
        webtoonscraper.AUTHORIZATION = authorization
    else:
        raise ValueError('Placeholder for later new ones.')

    await webtoonscraper.download_one_webtoon_async(webtoon_id, episode_no_range, merge=merge)


def get_webtoon(
        webtoon_id: int | tuple[int, int] | str,
        webtoon_type: None | str = None,
        *,
        merge: None | int = None,
        cookie: None | str = None,
        is_auto_select=False,
        episode_no_range: tuple[int, int] | int | None = None,
        authorization: None | str = None
) -> None:
    asyncio.run(get_webtoon_async(webtoon_id, webtoon_type, merge=merge, cookie=cookie, is_auto_select=is_auto_select, episode_no_range=episode_no_range, authorization=authorization))


if __name__ == '__main__':
    # asyncio.run(get_webtoon_platform(18))  # 네이버 게임
    asyncio.run(get_webtoon_platform(1022))  # 오리지널스
