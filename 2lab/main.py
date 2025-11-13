

if __name__ == "__main__":
    pass def convert_currency(rates, amount, path):
    p = path.split()
    m = float(p[0])
    r = f"{int(m)} {p[1]}"
    
    for i in range(1, len(p)-1):
        for x in rates:
            a, b, v = x.split()
            if a == p[i] and b == p[i+1]:
                m *= float(v)
                r += f" -> {int(m)} {b}"
                break
        else:
            return f"Ошибка: нет курса {p[i]} -> {p[i+1]}"
    
    return r
rates = ["r d 0.01", "d e 1", "e f 0.98"]
path = "1000 r d e"
print(convert_currency(rates, 1000, path))