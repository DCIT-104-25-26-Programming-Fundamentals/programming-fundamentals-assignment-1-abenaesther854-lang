# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def read_matrix(name="matrix"):
    """Read an M x N matrix from the user, one row per line."""
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))

    matrix = []
    for i in range(1, rows + 1):
        row_values = input(f"Enter row {i}: ").split()
        row = [float(v) for v in row_values]

        # Basic validation: make sure the row has the right number of columns
        while len(row) != cols:
            print(f"Error: expected {cols} values, got {len(row)}. Try again.")
            row_values = input(f"Enter row {i}: ").split()
            row = [float(v) for v in row_values]

        matrix.append(row)

    return matrix


def display_matrix(matrix):
    """Print a matrix in a neat, aligned grid format."""
    for row in matrix:
        # :g keeps whole numbers looking clean (e.g. 3 instead of 3.0)
        formatted = [f"{value:g}" for value in row]
        # Right-align each value within a fixed width for a clean grid
        width = max(len(v) for r in matrix for v in [f"{x:g}" for x in r])
        print("  ".join(v.rjust(width) for v in formatted))
    print()


def transpose_matrix(matrix):
    """Return the transpose of a matrix using nested loops."""
    rows = len(matrix)
    cols = len(matrix[0])

    # Result has swapped dimensions: cols x rows
    result = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


def add_matrices(matrix_a, matrix_b):
    """Return the element-wise sum of two matrices of the same size."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return result


def multiply_matrices(matrix_a, matrix_b):
    """Return the matrix product A x B using nested loops."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    result = [[0] * cols_b for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total

    return result


def part_a_transpose():
    print("\n--- Part A: Transpose a Matrix ---")
    matrix = read_matrix("the matrix")

    print("\nOriginal Matrix:")
    display_matrix(matrix)

    print("Transposed Matrix:")
    display_matrix(transpose_matrix(matrix))


def part_b_add():
    print("\n--- Part B: Add Two Matrices ---")
    print("Matrix A:")
    matrix_a = read_matrix("Matrix A")

    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])

    print(f"\nMatrix B must be {rows_a} x {cols_a} to match Matrix A.")
    matrix_b = read_matrix("Matrix B")

    # Validate matching dimensions
    if len(matrix_b) != rows_a or len(matrix_b[0]) != cols_a:
        print("Error: Matrix B must be the same size as Matrix A.")
        return

    result = add_matrices(matrix_a, matrix_b)

    print("\nMatrix A:")
    display_matrix(matrix_a)
    print("Matrix B:")
    display_matrix(matrix_b)
    print("Sum (A + B):")
    display_matrix(result)


def part_c_multiply():
    print("\n--- Part C: Multiply Two Matrices ---")
    print("Matrix A (M x N):")
    matrix_a = read_matrix("Matrix A")

    cols_a = len(matrix_a[0])

    print(f"\nMatrix B must have {cols_a} rows (N) to match Matrix A's columns.")
    matrix_b = read_matrix("Matrix B")

    # Validate that A's columns match B's rows
    if len(matrix_b) != cols_a:
        print("Error: Number of columns in A must equal number of rows in B.")
        return

    result = multiply_matrices(matrix_a, matrix_b)

    print("\nMatrix A:")
    display_matrix(matrix_a)
    print("Matrix B:")
    display_matrix(matrix_b)
    print("Product (A x B):")
    display_matrix(result)


def main():
    print("Matrix Operations")
    print("1. Transpose a Matrix")
    print("2. Add Two Matrices")
    print("3. Multiply Two Matrices")

    choice = input("Choose an operation (1-3): ")

    if choice == "1":
        part_a_transpose()
    elif choice == "2":
        part_b_add()
    elif choice == "3":
        part_c_multiply()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()