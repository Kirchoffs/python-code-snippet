import matplotlib.pyplot as plt

def leading_digit(n: int) -> int:
    while n >= 10:
        n //= 10
    return n

max_n = 1_000_000

leading_one_count = 0
ratios = []
xs = []

for i in range(1, max_n + 1):
    if leading_digit(i) == 1:
        leading_one_count += 1
    ratios.append(leading_one_count / i)
    xs.append(i)

benford_1 = 0.30103
print(f"Benford's Law predicts leading digit 1 proportion: {benford_1:.5f}")
print(f"Observed average leading digit 1 proportion: {sum(ratios) / len(ratios):.5f}")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize = (12, 8))

# linear scale
ax1.plot(xs, ratios, label = "Observed")
ax1.axhline(
    benford_1,
    linestyle = "--",
    label = "Benford ≈ 0.301"
)
ax1.set_xlabel("i (linear scale)")
ax1.set_ylabel("Proportion of leading digit = 1")
ax1.set_title("Linear Scale X-axis")
ax1.legend()
ax1.grid(True)

# log scale
ax2.plot(xs, ratios, label = "Observed")
ax2.axhline(
    benford_1,
    linestyle = "--",
    label = "Benford ≈ 0.301"
)
ax2.set_xscale("log")
ax2.set_xlabel("i (log scale)")
ax2.set_ylabel("Proportion of leading digit = 1")
ax2.set_title("Log Scale X-axis")
ax2.legend()
ax2.grid(True, which = "both")

plt.suptitle("Leading Digit = 1 Proportion in [1, i]", fontsize = 14)
plt.tight_layout()
plt.show()
