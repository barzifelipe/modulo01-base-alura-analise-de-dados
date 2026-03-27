coloniaA = 4
coloniaB = 10
dias = 0

while coloniaA < coloniaB:
    coloniaA += coloniaA * 0.03
    coloniaB += coloniaB * 0.015

    dias += 1

print(f"Serão necessários {dias} dias")