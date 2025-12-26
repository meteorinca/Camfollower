import numpy as np

def calculate_circle_profile(radius=1.0, points=360):
    """
    Returns a constant radius profile for testing.
    """
    return [radius] * points

def get_profile(text):
    """
    Routes the input text to the appropriate profile generator.
    For MVP, validates '0' or 'Circle' as basic test cases.
    """
    if text.lower() == "circle" or text == "0":
        # Return a simple circle profile
        # In a real cam, this would be the base radius
        return calculate_circle_profile(radius=50) # 50mm radius
    
    if text == "1":
        # "1" is a vertical line. 
        # On a polar cam, this might be a single lobe?
        # Let's just return a sinusodal bump for visual interest for now
        # until we implement full path mapping.
        indices = np.linspace(0, 2*np.pi, 360)
        # Base radius 40, one bump of +20
        radii = 40 + 20 * np.sin(indices)
        return radii.tolist()

    # Default fallback
    return calculate_circle_profile(radius=30)
