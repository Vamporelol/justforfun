from typing import Union


class SearchNum:
    def search(self, numbers: Union[str, int]) -> int:
        hownums = 0
        for num in str(numbers):
            if num == "2":
                hownums += 1

        return hownums
