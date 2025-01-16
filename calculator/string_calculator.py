
def add(numbers: str) -> int:
    if numbers == "":
        return 0
    if "," in numbers:
        numbers_list = numbers.split(",")
        return int(numbers_list[0]) + int(numbers_list[1])
    return int(numbers)