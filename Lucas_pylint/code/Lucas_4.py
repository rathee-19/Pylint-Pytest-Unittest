"""Function to calulate fibonacci"""
def calculate(n):
    """This functions calculates fibonacce recursively"""
    if n == 0:
        return -3
    if n == 1:
        return -1
    return calculate(n - 1) + calculate(n - 2)

def main():
    """
    this is main function"""
    n = int(input("enter the value of n: "))
    if -1 < n < 1000001:
        result = calculate(n)
        print(f"L{n} = {result}")
    else:
        print("Invalid input! please enter a value between -1 < n < 1000001 ")

if __name__ == "__main__":
    main()
