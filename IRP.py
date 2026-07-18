import numpy as np

try:
    import matplotlib.pyplot as plt
    HAVE_MPL = True
except ImportError:
    HAVE_MPL = False

def siebel_stieler(G, Rm):
    a = 3.7010
    b = -0.4659
    return 1.0 + a * np.sqrt(G) * (Rm ** b)

# Data (Tables 5 and 6)
group6_data = [
    (650.0, 0.2937, 1.0563),  # G6-A
    (575.0, 1.25,   1.3072),  # G6-B
    (525.0, 0.5974, 1.1965),  # G6-C
    (600.0, 4.3866, 1.3270),  # G6-D
]
lit_data = [
    (1562.0, 2.0, 1.2865),
    (206.0,  2.0, 1.5942),
    (210.0,  2.0, 1.3043),
    (639.0,  2.0, 1.1892),
    (707.0,  2.0, 1.1458),
    (707.0,  3.6, 1.3333),
]

all_data = group6_data + lit_data
Rm_data = np.array([d[0] for d in all_data])
G_data  = np.array([d[1] for d in all_data])
n_exp   = np.array([d[2] for d in all_data])

n_pred = siebel_stieler(G_data, Rm_data)

# Fit quality
residuals = n_exp - n_pred
SS_res = np.sum(residuals**2)
SS_tot = np.sum((n_exp - np.mean(n_exp))**2)
R2 = 1.0 - SS_res / SS_tot
rel_errors = np.abs(residuals) / n_exp
avg_rel_err = np.mean(rel_errors) * 100.0

print("Using published Siebel–Stieler parameters: a = 3.7010, b = -0.4659")
print(f"R^2 = {R2:.4f}")
print(f"Average relative error = {avg_rel_err:.1f} %\n")

print("Data points (Rm, G, n_exp, n_pred, rel_error):")
for Rm_i, G_i, ne, npred, err in zip(Rm_data, G_data, n_exp, n_pred, rel_errors):
    print(
        f"  Rm={Rm_i:6.1f} MPa, G={G_i:5.3f}  "
        f"n_exp={ne:6.4f}, n_pred={npred:6.4f}, err={err*100:5.1f} %"
    )

if HAVE_MPL:
    G_plot = np.linspace(0.2, 5.0, 200)
    Rm_list = [200, 400, 600, 800, 1000, 1500]

    plt.figure(figsize=(6, 4))
    for Rm_val in Rm_list:
        n_curve = siebel_stieler(G_plot, Rm_val)
        plt.plot(G_plot, n_curve, label=f"Rm = {Rm_val} MPa")
    plt.xlabel("Relative stress gradient G [1/mm]")
    plt.ylabel("Support factor n")
    plt.title("Design chart: n vs G for various Rm")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    Rm_plot = np.linspace(200, 1600, 200)
    G_list = [0.3, 1.0, 2.0, 3.0, 4.0]

    plt.figure(figsize=(6, 4))
    for G_val in G_list:
        n_curve = siebel_stieler(G_val, Rm_plot)
        plt.plot(Rm_plot, n_curve, label=f"G = {G_val} 1/mm")
    plt.xlabel("Tensile strength Rm [MPa]")
    plt.ylabel("Support factor n")
    plt.title("Design chart: n vs Rm for various G")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.show()
else:
    print("\nmatplotlib not available – skipping plots.")