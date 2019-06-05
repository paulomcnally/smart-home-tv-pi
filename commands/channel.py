from .tv import Tv


# Use to change channels on TV
class Channel:
    numbers = {
        '0': 'AAAAAQAAAAEAAAAJAw==',
        '1': 'AAAAAQAAAAEAAAAAAw==',
        '2': 'AAAAAQAAAAEAAAABAw==',
        '3': 'AAAAAQAAAAEAAAACAw==',
        '4': 'AAAAAQAAAAEAAAADAw==',
        '5': 'AAAAAQAAAAEAAAAEAw==',
        '6': 'AAAAAQAAAAEAAAAFAw==',
        '7': 'AAAAAQAAAAEAAAAGAw==',
        '8': 'AAAAAQAAAAEAAAAHAw==',
        '9': 'AAAAAQAAAAEAAAAIAw=='
    }


    # change channel
    @staticmethod
    def change(numbers):
        print(numbers)
        for number in numbers:
            Tv.command(Channel.numbers[number])
