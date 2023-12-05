from install_requirements import install_requirements

def fair_sharer(values, num_iterations, share=0.1):
    """
    Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neighbor of the rightmost field.

    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]

    Args:
        values (list or numpy array): 1D array of values
        num_iterations (int): Integer to set the number of iterations
        share (float): Fraction to share in each iteration (default is 0.1)
        
    Returns:
        list: Updated values after running the fair_sharer algorithm
    """
    install_requirements()
    for _ in range(num_iterations):
        # Find the index of the maximum value
        max_index = values.index(max(values))
        
        # Share the value with neighbors
        left_neighbor = (max_index - 1) % len(values)
        right_neighbor = (max_index + 1) % len(values)
        
        shared_value = share * values[max_index]
        values[left_neighbor] += shared_value
        values[right_neighbor] += shared_value
        
        # Reduce the shared value from the original position
        values[max_index] -= 2 * shared_value
    
    return values

# Test the function
# initial_values = [0, 1000, 800, 0]
# result = fair_sharer(initial_values, 2)
# print(result)
