import sys


def usage(code):
    print("""USAGE
    ./307multigrains.py n1 n2 n3 n4 po pw pc pb ps
DESCRIPTION
    n1\tnumber of tons of fertilizer F1
    n2\tnumber of tons of fertilizer F2
    n3\tnumber of tons of fertilizer F3
    n4\tnumber of tons of fertilizer F4
    po\tprice of one unit of oat
    pw\tprice of one unit of wheat
    pc\tprice of one unit of corn
    pb\tprice of one unit of barley
    ps\tprice of one unit of soy""")
    sys.exit(code)


if len(sys.argv) != 10:
    usage(84)

n1 = float(sys.argv[1])
n2 = float(sys.argv[2])
n3 = float(sys.argv[3])
n4 = float(sys.argv[4])
po = float(sys.argv[5])
pw = float(sys.argv[6])
pc = float(sys.argv[7])
pb = float(sys.argv[8])
ps = float(sys.argv[9])

oat_qty = min(n1, n2, n3 // 2, n4)
wheat_qty = min(n2 * 2, n3, n4)
corn_qty = min(n1, n4 // 3)
barley_qty = min(n2, n3, n4)
soy_qty = min(n1 * 2, n4 * 2)

production_value = (oat_qty * po) + (wheat_qty * pw) + (corn_qty * pc) + (barley_qty * pb) + (soy_qty * ps)
while True:
    oat_qty -= 1
    if oat_qty < 0:
        oat_qty += 1
        break
    new_cost = (oat_qty * po) + (wheat_qty * pw) + (corn_qty * pc) + (barley_qty * pb) + (soy_qty * ps)
    new_production_value = (oat_qty * po) + (wheat_qty * pw) + (corn_qty * pc) + (barley_qty * pb) + (soy_qty * ps)
    if new_production_value > production_value:
        production_value = new_production_value
    else:
        oat_qty += 1
        break

print(f"Resources: {int(n1)} F1, {int(n2)} F2, {int(n3)} F3, {int(n4)} F4\n")

print(f"Oat: {oat_qty} units at ${int(po)}/units")
print(f"Wheat: {wheat_qty} units at ${int(pw)}/units")
print(f"Corn: {corn_qty} units at ${int(pc)}/units")
print(f"Barley: {barley_qty} units at ${int(pb)}/units")
print(f"Soy: {soy_qty} units at ${int(ps)}/units\n")

print(f"Total production value: ${production_value}")
