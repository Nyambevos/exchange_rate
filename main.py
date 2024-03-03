import platform
import asyncio
from datetime import timedelta, datetime

from src.privat_bank_API import PrivatBankAPI
from src.argparser import Argparser

#['CHF', 'CZK', 'EUR', 'GBP', 'PLN', 'USD']
CURRENCY = ['EUR', 'USD'] 

args = Argparser(
    description=(
        'Currency rates from Privat Bank.')
        ).parse_args()

pb = PrivatBankAPI()


async def main() -> None:

    exchangeRates = []

    for day in range(args.number_days):
        data = {}
        target_date = (
            datetime.now() - timedelta(days=day)
            ).strftime('%d.%m.%Y')
        
        received_data = await pb.get_exchange_rates(target_date)

        for exchangeRate in received_data['exchangeRate']:
            if exchangeRate['currency'] in CURRENCY:
                data[exchangeRate['currency']] = {
                    'sale': exchangeRate['saleRate'],
                    'purchase': exchangeRate['purchaseRate']}
  
        exchangeRates.append({received_data['date']: data})
    
    return exchangeRates


if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    print(asyncio.run(main()))
