a = input("Enter first number: ")
b = input("Enter second number: ")
def convert(x):
    if x.isdigit():             
        return int(x)
    if x.count('.') == 1:        
        left, right = x.split('.')
        if left.isdigit() and right.isdigit():
            return float(x)
    return None                  
x = convert(a)
y = convert(b)
if x is None or y is None:
    print("Error: Please enter valid numbers only.")
else:
    print("The sum is:", x + y)
