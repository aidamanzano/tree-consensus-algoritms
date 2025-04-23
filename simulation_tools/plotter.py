import pandas as pd
import matplotlib.pyplot as plt

def plotter(input_pathfile:str, saving_pathfile:str):
    #input_pathfile = "/Users/amm3117/Desktop/TPoP 3/Code/tree-consensus/tree-consensus-algoritms/agent-based-simulations/n200_combined_df.csv"
    # Loading CSV
    df = pd.read_csv(input_pathfile)  # Update path as needed

    # Filter valid trees and drop NaNs
    filtered_df = df[df["valid_tree"] == True].copy()
    filtered_df = filtered_df.dropna(subset=["responses_sum"])

    # Extract values
    a = filtered_df["p_accept"].values
    b = filtered_df["p_reject"].values
    c = filtered_df["p_ignore"].values
    z = filtered_df["responses_sum"].values

    # Plot
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(projection='ternary')

    t = ax.tricontourf(a, b, c, z, levels=12, cmap="viridis")

    ax.set_tlabel("p_accept")
    ax.set_llabel("p_reject")
    ax.set_rlabel("p_ignore")
    ax.set_title("Ternary Contour Plot (responses_sum | valid_tree=True)")

    fig.colorbar(t, ax=ax, label="responses_sum")
    plt.tight_layout()
    plt.show()
    # Save the figure
    plt.savefig(saving_pathfile)
    plt.close()
    
