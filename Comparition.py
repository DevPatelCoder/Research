import time


def direct_cyclic_convolution(X, H):

    N = len(X)

    Y = [0] * N

    multiplication_count = 0
    addition_count = 0

    start_time = time.perf_counter()

    for i in range(N):

        for k in range(N):

            # h[(i-k) mod N]
            product = H[(i - k) % N] * X[k]

            multiplication_count += 1

            if k == 0:
                Y[i] = product

            else:
                Y[i] = Y[i] + product
                addition_count += 1

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    return (
        Y,
        multiplication_count,
        addition_count,
        execution_time
    )


# ============================================================
# TEST
# ============================================================

X = [1, 2, 3, 4]
H = [5, 6, 0, 0]


Y, M, A, T = direct_cyclic_convolution(X, H)


print("========================================")
print("DIRECT CYCLIC CONVOLUTION")
print("========================================")

print("X =", X)
print("H =", H)

print()
print("Output Y =", Y)

print()
print("Number of multiplications =", M)
print("Number of additions       =", A)
print("Execution time            =", T, "seconds")

"""-------------------------------------------------------------------------------------------------"""

import time


def agarwal_cooley_N4(X, H):

    # ========================================================
    # A TRANSFORM
    # ========================================================

    a0 = ((H[0] + H[2]) + (H[1] + H[3])) / 4

    a1 = ((H[0] - H[2]) - (H[1] - H[3])) / 4

    a2 = (H[0] - H[2]) / 2

    a3 = ((H[0] - H[2]) - (H[1] - H[3])) / 2

    a4 = ((H[0] - H[2]) + (H[1] - H[3])) / 2


    # ========================================================
    # B TRANSFORM
    # ========================================================

    b0 = (X[0] + X[2]) + (X[1] + X[3])

    b1 = (X[0] - X[2]) - (X[1] - X[3])

    b2 = (X[0] - X[2]) + (X[1] - X[3])

    b3 = X[0] - X[2]

    b4 = X[1] - X[3]


    # ========================================================
    # FIVE MULTIPLICATIONS
    # ========================================================

    m0 = a0 * b0
    m1 = a1 * b1
    m2 = a2 * b2
    m3 = a3 * b3
    m4 = a4 * b4


    # ========================================================
    # OUTPUT RECONSTRUCTION
    # ========================================================

    y0 = m0 + m1 + (m2 - m4)

    y1 = m0 - m1 + (m2 - m3)

    y2 = m0 + m1 - (m2 - m4)

    y3 = m0 - m1 - (m2 - m3)


    return [y0, y1, y2, y3]


# ============================================================
# TEST
# ============================================================

X = [1, 2, 3, 4]
H = [5, 6, 0, 0]


start_time = time.perf_counter()

Y = agarwal_cooley_N4(X, H)

end_time = time.perf_counter()

execution_time = end_time - start_time


# ============================================================
# PAPER'S OPERATION COUNTS
# ============================================================

multiplication_count = 5
addition_count = 15


print("========================================")
print("AGARWAL-COOLEY N=4 CONVOLUTION")
print("========================================")

print("X =", X)
print("H =", H)

print()
print("Output Y =", Y)

print()
print("Number of multiplications =", multiplication_count)
print("Number of additions       =", addition_count)
print("Execution time            =", execution_time, "seconds")

"""----------------------------------------------------------------------------------------------------------"""
# ============================================================
# COMPARISON
# ============================================================

direct_multiplications = 16
direct_additions = 12

optimized_multiplications = 5
optimized_additions = 15


multiplication_reduction = (
    (direct_multiplications - optimized_multiplications)
    / direct_multiplications
) * 100


addition_increase = (
    (optimized_additions - direct_additions)
    / direct_additions
) * 100


print()
print("========================================")
print("OPERATION COUNT COMPARISON")
print("========================================")

print()

print("                     Direct     Agarwal-Cooley")

print(
    "Multiplications      ",
    direct_multiplications,
    "          ",
    optimized_multiplications
)

print(
    "Additions            ",
    direct_additions,
    "          ",
    optimized_additions
)

print()

print(
    "Multiplication reduction =",
    multiplication_reduction,
    "%"
)

print(
    "Addition increase        =",
    addition_increase,
    "%"
)
