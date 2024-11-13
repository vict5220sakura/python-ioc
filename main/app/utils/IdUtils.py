import random


class IdUtils:

    @staticmethod
    def salt(baseStr='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', length=10, split="") -> str:
        characters = random.sample(baseStr, length)
        return "".join(characters)

