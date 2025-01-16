
def add(numbers: str) -> int:
    if numbers == "":
        return 0
    if numbers.startswith("//"):
        if numbers[2] == "[":
            closing_bracket = numbers.find("]")
            delimiter = numbers[3:closing_bracket]
            numbers = numbers[closing_bracket + 2:] 
        else:
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

        valid_nums = [num for num in numbers_int if num <= 1000]  
        
        return sum(valid_nums)
    return int(numbers)