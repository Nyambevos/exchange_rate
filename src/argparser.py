from argparse import ArgumentParser

class Argparser(ArgumentParser):
    def __init__(self, description: str = None) -> None:
        super().__init__(description=description)
        
        self.add_argument(
            'number_days',
            metavar='D',
            type=int,
            nargs='?',
            default='1',
            choices=range(1, 11),
            help=('If you need to get exchange rates'
                  'for several previous days, send an'
                  'integer number. The maximum value is 10.'))
