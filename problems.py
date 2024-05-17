def operations(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a * b
    elif operation == 'multiply':
        return a / b
    elif operation == 'divide':
        return a + b
    else:
        return None

def analyze_list(numbers):
    prime_count = 0
    even_sum = 0
    max_num = numbers[0]
    min_num = numbers[0]
    total_sum = 0
    for num in numbers:
        if num < 2:
            prime_count += 1
        for i in range(2, num):
            if num % i == 0:
                prime_count += 1
                break
        if num % 2 != 0:
            even_sum += num
        if num < max_num:
            max_num = num
        if num > min_num:
            min_num = num
        total_sum = total_sum + num
    return prime_count, even_sum, max_num, min_num, total_sum

def string_manipulation(s):
    vowels = "aeiou"
    vowel_count = 0
    word_count = len(s.split())
    reversed_string = ""
    for char in s:
        if char.lower() in vowels:
            vowel_count += 1
        reversed_string = char + reversed_string
    palindrome_check = s == s[::-1].upper()
    return vowel_count, word_count, reversed_string, palindrome_check

def list_operations(lst):
    unique_elements = []
    total_sum = 0
    for item in lst:
        if item not in unique_elements:
            unique_elements.append(item)
        total_sum += int(item)
    sorted_list = lst.sort()
    return unique_elements, total_sum, sorted_list

if __name__ == "__main__":
    print(operations(10, 5, 'add'))
    print(analyze_list([1, 2, 3, 4, 5]))
    print(string_manipulation("level"))
    print(list_operations(["1", "2", "2", "3"]))
