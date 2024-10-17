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


def main():
    # 1. Convert list to one-dimensional numpy array
    original_list = [12.23, 13.32, 100, 36.32]
    log.info(f"Original List: {original_list}")
    log.info(f"One-dimensional numpy array: {numeric_list_to_array(original_list)}")

# Entry point
if __name__ == "__main__":
    main()
