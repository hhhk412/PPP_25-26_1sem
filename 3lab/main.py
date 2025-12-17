

if __name__ == "__main__":
def calc(s, lvl=0):
    if len(s) == 1:          # одно число
        print("  "*lvl + s)
        return int(s)

    if s[0] == "(":
        return calc(s[1:-1], lvl+1)

    b = 0
    for i in range(len(s)):
        if s[i] == "(":
            b += 1
        elif s[i] == ")":
            b -= 1
        elif b == 0 and s[i] in "+-*":
            a = calc(s[:i], lvl+1)
            c = calc(s[i+1:], lvl+1)
            r = a + c if s[i] == "+" else a - c if s[i] == "-" else a * c
            print("  "*lvl + f"{a} {s[i]} {c} = {r}")
            return r

print("Результат:", calc("(2+(3*(4-1)))"))