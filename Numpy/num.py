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

def main():
    # 1. Convert list to one-dimensional numpy array
    original_list = [12.23, 13.32, 100, 36.32]
    log.info(f"Original List: {original_list}")
    log.info(f"One-dimensional numpy array: {numeric_list_to_array(original_list)}")
    # 2. Create a 3x3 matrix with values from 2 to 10
    log.info(f"3x3 Matrix:\n{create_matrix()}")
    # 3. Create null vector of size 10 and update sixth value to 11
    log.info(f"Null Vector with sixth value updated:\n{null_vector()}")

# Entry point
if __name__ == "__main__":
    main()
