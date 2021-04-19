from aiohttp import ClientSession


class AioHttp:
    """class for helping get the data from url using aiohttp."""

    @staticmethod
    async def get_json(link: str, **kwargs):
        """Get JSON data from the provided link."""
        async with ClientSession() as sess:
            async with sess.get(link, **kwargs) as resp:
                return await resp.json(), resp

    @staticmethod
    async def get_text(link: str, **kwargs):
        """Get Text data from the provided link."""
        async with ClientSession() as sess:
            async with sess.get(link, **kwargs) as resp:
                return await resp.text(), resp

    @staticmethod
    async def get_raw(link: str, **kwargs):
        """Get RAW data from the provided link."""
        async with ClientSession() as sess:
            async with sess.get(link, **kwargs) as resp:
                return await resp.read(), resp
