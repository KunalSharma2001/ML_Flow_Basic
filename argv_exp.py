import sys
alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
l1_ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5

print(alpha, l1_ratio)
# by default it will take 0.5 & 0.5 values.
# this code is taking diffeeper values of alpha and l1_ratio durinng runtime.