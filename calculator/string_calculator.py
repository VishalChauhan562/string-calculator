
def add(numbers: str) -> int:
    if numbers == "":
        return 0
    if numbers.startswith("//"):
        delimiter = numbers[2]
        numbers = numbers[4:]  
        numbers = numbers.replace(delimiter, ",")

    numbers = numbers.replace("\n",",")
    if "," in numbers:
        numbers_list = numbers.split(",")
        numbers_int = [int(num) for num in numbers_list]
        negative_nums = [num for num in numbers_int if num < 0 ]
        if negative_nums:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negative_nums))}")
        return sum(numbers_int)
    return int(numbers)