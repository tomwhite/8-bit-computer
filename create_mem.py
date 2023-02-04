mem = {}
with open("in2.txt") as f:
    for line in f:
        if line.startswith("#"):
            continue
        a, b = line.strip().split(",")
        mem[int(a, 2)] = int(b, 2)

for k, v in sorted(mem.items()):
    print(f"{k}: {v}")