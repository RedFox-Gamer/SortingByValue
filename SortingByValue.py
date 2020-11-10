marks = {
    "Apple":     100,
    "Orange":    25,
    "Pineapple": 55,
    "Banana":    70,
}
d = {k: v for k, v in sorted(marks.items(), key=lambda item: item[1])}
print(d)

