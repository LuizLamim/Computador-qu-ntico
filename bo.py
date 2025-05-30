import matplotlib.pyplot as plt

def get_equation_string(h_val="h", k_val="k", a_val="a", b_val="b", result="1"):
    """
    Generates the string representation of the ellipse equation.
    """
    return f"(x-{h_val})²/({a_val})² + (y-{k_val})²/({b_val})² = {result}"

def display_equation_as_image(eq_string, filename="equation.png"):
    """
    Generates and saves an image of the equation using Matplotlib and LaTeX.
    """
    # Sanitize the string for LaTeX by escaping special characters if necessary,
    # though for this specific equation, it should be fine.
    # For more complex dynamic strings, you might need more robust sanitization.
    latex_eq = f"${eq_string.replace('²', '^{2}')}$" # Basic replacement for LaTeX superscripts

    fig, ax = plt.subplots(figsize=(6, 1.5)) # Adjust figsize as needed
    ax.text(0.5, 0.5, latex_eq, size=20, ha='center', va='center')
    ax.axis('off') # Hide the axes

    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"Equation saved as image: {filename}")
    # To display it in a Jupyter notebook or similar environment immediately:
    # plt.show()

if __name__ == "__main__":
    # --- Part 1: Get the equation as a simple string ---
    equation_str = get_equation_string()
    print("Plain text equation:")
    print(equation_str)
    print("-" * 30)

    # You can also substitute values for h, k, a, b:
    # equation_with_values = get_equation_string(h_val="2", k_val="3", a_val="5", b_val="4")
    # print("\nPlain text equation with values:")
    # print(equation_with_values)
    # print("-" * 30)

    # --- Part 2: Generate an image of the equation ---
    print("\nGenerating image of the equation...")
    # For the image, we'll use the generic form.
    # We need to format it slightly differently for Matplotlib's LaTeX rendering.
    # Specifically, use raw string (r"...") or escape backslashes if you use LaTeX commands.
    # The f-string approach above handles basic superscripts.

    # To make it look nice with proper fractions in LaTeX:
    latex_formatted_equation = r"$\frac{(x-h)^2}{a^2} + \frac{(y-k)^2}{b^2} = 1$"
    # Or, building it dynamically for LaTeX:
    h, k, a, b, result = "h", "k", "a", "b", "1"
    dynamic_latex_eq = rf"$\frac{{(x-{h})^2}}{{{a}^2}} + \frac{{(y-{k})^2}}{{{b}^2}} = {result}$"


    # Using the more nicely formatted LaTeX string for the image:
    display_equation_as_image(dynamic_latex_eq, "ellipse_equation.png")

    # If you wanted to post the simple string version as an image:
    # display_equation_as_image(equation_str, "ellipse_equation_simple.png")