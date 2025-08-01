
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)

def test_print_color_map_mismatches():
    import io
    import sys

    expected_lines = [
        "1 | White | Blue",
        "2 | White | Orange",
        "3 | White | Green",
        "4 | White | Brown",
        "5 | White | Slate",
        "6 | Red | Blue",
        "7 | Red | Orange",
        "8 | Red | Green",
        "9 | Red | Brown",
        "10 | Red | Slate",
        "11 | Black | Blue",
        "12 | Black | Orange",
        "13 | Black | Green",
        "14 | Black | Brown",
        "15 | Black | Slate",
        "16 | Yellow | Blue",
        "17 | Yellow | Orange",
        "18 | Yellow | Green",
        "19 | Yellow | Brown",
        "20 | Yellow | Slate",
        "21 | Violet | Blue",
        "22 | Violet | Orange",
        "23 | Violet | Green",
        "24 | Violet | Brown",
        "25 | Violet | Slate"
    ]

    # Capture the output of print_color_map
    captured_output = io.StringIO()
    sys.stdout = captured_output
    print_color_map()
    sys.stdout = sys.__stdout__

    output_lines = captured_output.getvalue().strip().split('\n')

    mismatches = []
    for idx, (expected, actual) in enumerate(zip(expected_lines, output_lines)):
        if expected != actual:
            mismatches.append(f"Line {idx+1}: expected '{expected}', got '{actual}'")

    if mismatches:
        print("Mismatches found:")
        for mismatch in mismatches:
            print(mismatch)
    else:
        print("No mismatches found!")

test_print_color_map_mismatches()
print("All is well (maybe!)")

#result = print_color_map()
#assert(result == 25)
#print("All is well (maybe!)")
