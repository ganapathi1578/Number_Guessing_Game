l = 0.0
u = 100.0

digits = int(input("How many decimal digits should I guess with? "))

print(f"Think of a number between {l} and {u} with up to {digits} decimal digits.")

while True:
    mid = round((l + u) / 2, digits)
    
    c = int(input(f"Is it {mid}?\nType 1 for yes, 0 for no: "))
    if not c:
        c = int(input(f"Is it greater than {mid}?\nType 1 for yes, 0 for no: "))
        if c:
            l = mid
        else:
            u = mid
    else:
        print(f"I guessed it correctly! You thought of {mid}. That was fun!")
        break
