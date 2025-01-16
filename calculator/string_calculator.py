
def add(numbers: str) -> int:
    if numbers == "":
        return 0
    numbers = numbers.replace("\n",",")
    if "," in numbers:
        numbers_list = numbers.split(",")
        return sum(int(num) for num in numbers_list)
    return int(numbers)