import numpy as np
import log

log = log.logger_init('numpy_tasks')

def numeric_list_to_array(lst):
    """
    Description:
        This function converts a list of numeric values into a one-dimensional NumPy array.
    Parameters:
        lst: List of numeric values.
    Return:
        A one-dimensional NumPy array.
    """
    return np.array(lst)

def create_matrix():
    """
    Description:
        This function creates a 3x3 matrix with values ranging from 2 to 10.
    Return:
        A 3x3 matrix.
    """
    return np.arange(2, 11).reshape(3, 3)

def null_vector():
    """
    Description:
        This function creates a null vector of size 10 and updates the sixth value to 11.
    Return:
        Updated null vector.
    """
    vec = np.zeros(10)
    vec[5] = 11
    return vec

def reverse_array(arr):
    """
    Description:
        This function reverses the given array.
    Parameters:
        arr: Input array.
    Return:
        Reversed array.
    """
    return np.flip(arr)
def create_border_array():
    """
    Description:
        This function creates a 2D array with 1s on the border and 0s inside.
    Return:
        A 2D array with border of 1s.
    """
    arr = np.ones((5, 5))
    arr[1:-1, 1:-1] = 0
    return arr
def add_border_zeros(arr):
    """
    Description:
        This function adds a border filled with 0's around the existing array.
    Parameters:
        arr: Input 2D array.
    Return:
        New array with border of 0's.
    """
    return np.pad(arr, pad_width=1, mode='constant', constant_values=0)

def create_checkerboard():
    """
    Description:
        This function creates an 8x8 checkerboard pattern.
    Return:
        An 8x8 checkerboard pattern.
    """
    arr =np.zeros([8,8])
    arr[1::2,::2]=1
    arr[::2,1::2]=1
    return arr

def list_and_tuple_to_arrays(lst, tpl):
    """
    Description:
        This function converts a list and a tuple into arrays.
    Parameters:
        lst: Input list.
        tpl: Input tuple.
    Return:
        Tuple of arrays (from list and tuple).
    """
    return np.array(lst), np.array(tpl)

def append_values(arr, values):
    """
    Description:
        This function appends values to the end of the array.
    Parameters:
        arr: Input array.
        values: Values to append.
    Return:
        Updated array after appending.
    """
    return np.append(arr, values)

def real_imaginary_parts(arr):
    """
    Description:
        This function finds the real and imaginary parts of a complex number array.
    Parameters:
        arr: Input array of complex numbers.
    Return:
        Tuple of real and imaginary parts.
    """
    return np.real(arr), np.imag(arr)

def array_memory_info(arr):
    """
    Description:
        This function finds the number of elements, length of one element in bytes,
        and total bytes consumed by the elements of the array.
    Parameters:
        arr: Input array.
    Return:
        Tuple with size, length of one element in bytes, and total bytes consumed.
    """
    return arr.size, arr.itemsize, arr.nbytes

def common_values(arr1, arr2):
    """
    Description:
        This function finds common values between two arrays.
    Parameters:
        arr1: First array.
        arr2: Second array.
    Return:
        Array of common values.
    """
    return np.intersect1d(arr1, arr2)

def set_difference(arr1, arr2):
    """
    Description:
        This function finds the set difference of two arrays.
    Parameters:
        arr1: First array.
        arr2: Second array.
    Return:
        Array with unique values in arr1 not in arr2.
    """
    return np.setdiff1d(arr1, arr2)

def set_exclusive_or(arr1, arr2):
    """
    Description:
        This function finds the set exclusive-or of two arrays.
    Parameters:
        arr1: First array.
        arr2: Second array.
    Return:
        Array with unique values in only one of the arrays.
    """
    return np.setxor1d(arr1, arr2)

def compare_arrays(arr1, arr2):
    """
    Description:
        This function compares two arrays using numpy.
    Parameters:
        arr1: First array.
        arr2: Second array.
    Return:
        Comparison results as a dictionary.
    """
    return {
        'greater': arr1 > arr2,
        'greater_equal': arr1 >= arr2,
        'less': arr1 < arr2,
        'less_equal': arr1 <= arr2,
    }

def save_array_to_file(arr, filename):
    """
    Description:
        This function saves a NumPy array to a text file.
    Parameters:
        arr: Input array.
        filename: Output filename.
    """
    np.savetxt(filename, arr)
    
def create_flattened_array(arr):
    """
    Description:
        This function creates a contiguous flattened array.
    Parameters:
        arr: Input 2D array.
    Return:
        Flattened array.
    """
    return arr.flatten()

def change_array_dtype(arr, new_type):
    """
    Description:
        This function changes the data type of an array.
    Parameters:
        arr: Input array.
        new_type: Desired data type.
    Return:
        New array with changed data type.
    """
    return arr.astype(new_type)

def create_diagonal_ones():
    """
    Description:
        This function creates a 3D array with ones on the diagonal and zeros elsewhere.
    Return:
        3D diagonal ones array.
    """
    return np.eye(3)

def specific_array():
    """
    Description:
        This function creates a specific array pattern.
    Return:
        The specified array pattern.
    """
    return np.array([[0, 0, 0],
                     [1, 0, 0],
                     [1, 1, 0],
                     [1, 1, 1]])
    
def concatenate_arrays(arr1, arr2):
    """
    Description:
        This function concatenates two 2-dimensional arrays.
    Parameters:
        arr1: First 2D array.
        arr2: Second 2D array.
    Return:
        Concatenated 2D array.
    """
    return np.concatenate((arr1, arr2), axis=1)

def make_array_read_only(arr):
    """
    Description:
        This function makes an array immutable (read-only).
    Parameters:
        arr: Input array.
    Return:
        Read-only array.
    """
    arr.setflags(write=False)
    return arr

def multiply_elements(arr, factor):
    """
    Description:
        This function multiplies every element of the array by a given factor.
    Parameters:
        arr: Input array.
        factor: Multiplication factor.
    Return:
        New array with multiplied elements.
    """
    return arr * factor




def main():
    # 1. Convert list to one-dimensional numpy array
    original_list = [12.23, 13.32, 100, 36.32]
    log.info(f"Original List: {original_list}")
    log.info(f"One-dimensional numpy array: {numeric_list_to_array(original_list)}")
    # 2. Create a 3x3 matrix with values from 2 to 10
    log.info(f"3x3 Matrix:\n{create_matrix()}")
    # 3. Create null vector of size 10 and update sixth value to 11
    log.info(f"Null Vector with sixth value updated:\n{null_vector()}")
    # 4. Reverse an array
    arr_to_reverse = np.arange(12, 38)
    log.info(f"Reversed array:\n{reverse_array(arr_to_reverse)}")
    # 5. Create 2D array with 1 on the border and 0 inside
    log.info(f"2D Array with border of 1:\n{create_border_array()}")
    # 6. Add border of 0's around an existing array
    existing_array = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    log.info(f"Array with border of 0's:\n{add_border_zeros(existing_array)}")
    # 7. Create an 8x8 matrix with a checkerboard pattern
    log.info(f"Checkerboard Pattern:\n{create_checkerboard()}")
    # 8. Convert list and tuple into arrays
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    tpl = (8, 4, 6, 1, 2, 3)
    list_arr, tuple_arr = list_and_tuple_to_arrays(lst, tpl)
    log.info(f"List to Array: {list_arr}")
    log.info(f"Tuple to Array: {tuple_arr}")
    # 9. Append values to an array
    arr_to_append = np.array([10, 20, 30])
    log.info(f"Array after appending values:\n{append_values(arr_to_append, [40, 50, 60, 70, 80, 90])}")
    # 10. Find real and imaginary parts of complex numbers
    complex_arr = np.array([1 + 0j, 0.707 + 0.707j])
    real_part, imag_part = real_imaginary_parts(complex_arr)
    log.info(f"Real Part: {real_part}, Imaginary Part: {imag_part}")
    # 11. Find size, length of one element in bytes, and total bytes consumed
    arr_info = np.array([1, 2, 3], dtype=np.float64)
    size, itemsize, nbytes = array_memory_info(arr_info)
    log.info(f"Array Info - Size: {size}, Item Size: {itemsize}, Total Bytes: {nbytes}")
    # 12. Find common values between two arrays
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([4, 5, 6, 7, 8])
    log.info(f"Common Values: {common_values(arr1, arr2)}")
    # 13. Find the set difference of two arrays
    log.info(f"Set Difference: {set_difference(arr1, arr2)}")
    # 14. Find the set exclusive or of two arrays
    log.info(f"Set Exclusive OR: {set_exclusive_or(arr1, arr2)}")
    # 15. Compare two arrays
    arr3 = np.array([1, 2, 3, 4])
    arr4 = np.array([3, 2, 1, 0])
    log.info(f"Array Comparison Results: {compare_arrays(arr3, arr4)}")
    # 16. Save array to file
    save_array_to_file(arr3, 'array_output.txt')
    # 17. Create a contiguous flattened array
    two_d_array = np.array([[1, 2], [3, 4], [5, 6]])
    log.info(f"Flattened Array: {create_flattened_array(two_d_array)}")
    # 18. Change array data type
    log.info(f"Changed Array Data Type:\n{change_array_dtype(arr_info, np.int32)}")
    # 19. Create a diagonal array
    log.info(f"Diagonal Ones Array:\n{create_diagonal_ones()}")
    # 20. Create a specific pattern array
    log.info(f"Specific Array Pattern:\n{specific_array()}")
    # 21. Concatenate two arrays
    arr5 = np.array([[1, 2], [3, 4]])
    arr6 = np.array([[5, 6], [7, 8]])
    log.info(f"Concatenated Array:\n{concatenate_arrays(arr5, arr6)}")
    # 22. Make an array read-only
    read_only_arr = make_array_read_only(arr_info.copy())
    log.info(f"Read-Only Array:\n{read_only_arr}")
    # 23. Multiply elements of an array
    log.info(f"Array after multiplication:\n{multiply_elements(arr_info, 2)}")


# Entry point
if __name__ == "__main__":
    main()
