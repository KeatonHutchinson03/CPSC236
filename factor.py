def get_valid_integer():
    while True:
        try:
            num = int(input("Please enter an integer between 1 and 5000: "))
            if 1 <= num <= 5000:
                return num
            else:
                print("Invalid integer. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def count_factors(n):
    factors = [i for i in range(1, n + 1) if n % i == 0]
    return len(factors), factors