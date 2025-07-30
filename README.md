# 📘 PART 1: Introduction to NumPy

📘 Summary
This project provides a beginner-friendly introduction to NumPy, a powerful Python library used for numerical and scientific computing. The script demonstrates how to create and work with NumPy arrays, focusing on the fundamentals.

✅ Topics Covered
Python Lists vs NumPy Arrays

Python lists can store mixed data types.

NumPy arrays are more memory-efficient and require uniform data types.

Array Creation Methods

np.array() – Convert lists to arrays

np.arange() – Create a range of values (1D arrays)

np.zeros() – Create arrays filled with zeros

np.full() – Create arrays filled with a specific value

Multi-dimensional Arrays

Create 2D arrays using tuples for shape

Example: np.zeros((2, 3)) creates a 2×3 matrix of zeros

Using .shape

Returns a tuple representing the array's dimensions

Helps identify the structure of 1D, 2D, or nD arrays

🧠 Key Insight
np.arange() only creates 1D arrays; use .reshape() to convert to multi-dimensional arrays.

.shape is essential for understanding and debugging array structures.


## 📚 NumPy Slicing and Indexing – Summary PART 2

This part covers essential techniques to access and slice data in NumPy arrays, both 1D and 2D.

### ✅ Key Concepts

- **1D Array Slicing**  
  Extract portions of arrays using `start:stop` indexing, e.g., `array[2:]` returns elements from index 2 to the end.

- **Negative Indexing and Slicing**  
  Use negative indices to count from the end of the array.  
  Reverse arrays with `array[::-1]`.  
  Slice parts using negative indices like `array[-6:-2]`.

- **Slicing with Steps**  
  Access elements with specific intervals using `array[::step]`, e.g., every second element via `array[::2]`.

- **2D Arrays and Shape**  
  `.shape` shows the dimensions of 2D arrays as `(rows, columns)`.

- **Indexing 2D Arrays**  
  Access elements using either `array[row][col]` or the preferred `array[row, col]`.

- **Slicing 2D Arrays**  
  Slice submatrices using `array[row_start:row_stop, col_start:col_stop]`.


