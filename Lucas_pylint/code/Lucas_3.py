"""Function to calulate fibonacci"""
def calculate(n):
    if n == 0:
        return -3
    elif n == 1:
        return -1
    else:
        return calculate(n - 1) + calculate(n - 2)

def main():
    n = int(input("enter the value of n: "))
    if -1 < n < 1000001:
        result = calculate(n)
        print(f"L{n} = {result}")
    else:
        print("Invalid input! please enter a value between -1 < n < 1000001 ")

if __name__ == "__main__":
    main()
