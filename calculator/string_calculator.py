
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
        return sum(int(num) for num in numbers_list)
    return int(numbers)