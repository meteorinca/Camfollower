import matplotlib.pyplot as plt
import numpy as np
import geometry
import os

def normalize_profile(profile):
    """
    Ensure the profile is a valid list of numbers suitable for plotting.
    """
    return np.array(profile)

def plot_profile(profile, name="cam_profile"):
    """
    Plots the cam profile in polar coordinates.
    """
    theta = np.linspace(0, 2*np.pi, len(profile))
    
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, profile)
    ax.set_rmax(max(profile) * 1.2)
    ax.set_rticks([min(profile), max(profile)])  # Less radial ticks
    ax.grid(True)
    
    ax.set_title(f"Cam Profile: {name}", va='bottom')
    
    output_file = f"{name}.png"
    plt.savefig(output_file)
    print(f"Saved plot to {output_file}")
    plt.close()

def main():
    print("Running Geometry Validation...")
    
    # Test Case 1: Circle
    print("Generating 'Circle' profile...")
    circle_profile = geometry.get_profile("Circle")
    plot_profile(circle_profile, "test_circle")
    
    # Test Case 2: Number '1'
    print("Generating '1' profile...")
    one_profile = geometry.get_profile("1")
    plot_profile(one_profile, "test_one")
    
    print("Validation Complete.")

if __name__ == "__main__":
    main()
