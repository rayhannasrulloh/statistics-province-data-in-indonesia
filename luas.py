import numpy as np

# Define the coefficient matrix and constants vector
A = np.array([
    [1, 1, 1, 1],
    [2, 3, 4, 5],
    [0, 1, 0, 2],
    [1, 2, 0, 1]
])

b = np.array([5, 1, 1, 3])

# Calculate the determinant of the coefficient matrix
det_A = np.linalg.det(A)
print(f"det(A) = {det_A}")

# Create matrices for each variable by replacing columns with b
A1 = A.copy()
A1[:, 0] = b
det_A1 = np.linalg.det(A1)
print(f"det(A1) = {det_A1}")

A2 = A.copy()
A2[:, 1] = b
det_A2 = np.linalg.det(A2)
print(f"det(A2) = {det_A2}")

A3 = A.copy()
A3[:, 2] = b
det_A3 = np.linalg.det(A3)
print(f"det(A3) = {det_A3}")

A4 = A.copy()
A4[:, 3] = b
det_A4 = np.linalg.det(A4)
print(f"det(A4) = {det_A4}")

# Apply Cramer's Rule
x1 = det_A1 / det_A
x2 = det_A2 / det_A
x3 = det_A3 / det_A
x4 = det_A4 / det_A

print("\nSolution:")
print(f"x1 = {x1}")
print(f"x2 = {x2}")
print(f"x3 = {x3}")
print(f"x4 = {x4}")

# Verify the solution
solution = np.array([x1, x2, x3, x4])
verification = A @ solution

print("\nVerification:")
print("Ax =", verification)
print("b =", b)
print("Is the solution correct?", np.allclose(verification, b))