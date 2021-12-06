from typing import Any, Dict, Tuple

from aiohttp import ClientResponse, ClientSession


class AioHttp:
    """class for helping get the data from url using aiohttp."""

    @staticmethod
    async def get_json(link: str, **kwargs) -> Tuple[Dict[str, Any], ClientResponse]:
        """Get JSON data from the provided link."""
        async with ClientSession() as sess, sess.get(link, **kwargs) as resp:
            return await resp.json(), resp

    @staticmethod
    async def get_text(link: str, **kwargs) -> Tuple[str, ClientResponse]:
        """Get Text data from the provided link."""
        async with ClientSession() as sess, sess.get(link, **kwargs) as resp:
            return await resp.text(), resp

    @staticmethod
    async def get_raw(link: str, **kwargs) -> Tuple[bytes, ClientResponse]:
        """Get RAW data from the provided link."""
        async with ClientSession() as sess, sess.get(link, **kwargs) as resp:
            return await resp.read(), resp
