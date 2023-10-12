import aiohttp


async def jservice_request(qtt: int):
    """
    Get request to https://jservice.io/api/random?count={qtt}
    :param qtt: int
    :return: json
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://jservice.io/api/random?count={qtt}') as resp:
            return await resp.json()
