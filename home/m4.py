import random
import statistics
import math

def generate_random_numbers(count, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(count)]

def calculate_sum(numbers):
    return sum(numbers)

def calculate_product(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

def calculate_max(numbers):
    return max(numbers)

def calculate_min(numbers):
    return min(numbers)

def calculate_statistics(numbers):
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    mode = statistics.mode(numbers)
    variance = statistics.variance(numbers)
    std_dev = statistics.stdev(numbers)
    
    return {
        'mean': mean,
        'median': median,
        'mode': mode,
        'variance': variance,
        'standard_deviation': std_dev,
    }

def main():
    count = int(input("Enter the number of random numbers to generate: "))
    lower_bound = int(input("Enter the lower bound for random numbers: "))
    upper_bound = int(input("Enter the upper bound for random numbers: "))
    
    random_numbers = generate_random_numbers(count, lower_bound, upper_bound)
    
    print("\nGenerated Random Numbers:")
    print(random_numbers)
    
    print("\nMathematical Operations:")
    print(f"Sum: {calculate_sum(random_numbers)}")
    print(f"Product: {calculate_product(random_numbers)}")
    print(f"Max: {calculate_max(random_numbers)}")
    print(f"Min: {calculate_min(random_numbers)}")
    
    stats = calculate_statistics(random_numbers)
    
    print("\nStatistical Measures:")
    for key, value in stats.items():
        print(f"{key.capitalize()}: {value}")

if __name__ == "__main__":
    main()
