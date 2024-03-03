import aiohttp

class PrivatBankAPI:
    BASE_URL = "https://api.privatbank.ua"

    async def get_exchange_rates(self, date):
        url = f"{self.BASE_URL}/p24api/exchange_rates?json&date={date}"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        return data
                    else:
                        raise Exception(f"Failed to fetch data, status code: {response.status}")
        except aiohttp.ClientConnectorError as err:
                print(f'Connection error: {url}', str(err))
                
                

    
