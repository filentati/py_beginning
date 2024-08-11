numerator =  int(input())
denominator = int(input())

def changed_div(numerator, denominator):
    try:
        quotient = numerator / denominator
        return denominator / quotient
    except ZeroDivisionError:
        return denominator

print(changed_div(numerator, denominator))
