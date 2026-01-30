def greet(name:str) -> str:
    return f"Hello, {name}"

def add(a: int, b:int) -> int:
    return a + b

print(greet("Khaleel"))
print(add(3,5))

def calculate_tax(amount: float, tax_rate: float = 0.1) -> float:
    return amount * tax_rate

total = 100
tax = calculate_tax(total)

print("Ta: {tax}")

def safe_divide(a: float, b: float) -> float:
    try:
        return a/b
    except ZeroDivisionError:
        return 0.0
    
print(safe_divide(10,2))
print(safe_divide(10,0))


from math_utils import multiply

print(multiply(4,5))