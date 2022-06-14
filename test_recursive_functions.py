import recursive_functions
import math

def main():
    total =0
    # Test factorial
    print('Testing factorial.')
    assert recursive_functions.factorial(0)  == 1
    assert recursive_functions.factorial(1)  == math.factorial(1) == 1
    assert recursive_functions.factorial(2)  == math.factorial(2) == 2
    assert recursive_functions.factorial(5) == math.factorial(5) == 120
    assert recursive_functions.factorial(7) == math.factorial(7) == 5040
    print('All tests pass for `factorial` (✿◠‿◠)\n')
    total += 25

    # Test sum_recursively
    print('Testing sum_recursively.')
    assert recursive_functions.sum_recursively(0)  == 0
    assert recursive_functions.sum_recursively(1)  == sum(range(1+1)) == 1
    assert recursive_functions.sum_recursively(2)  == sum(range(2+1)) == 3
    assert recursive_functions.sum_recursively(10) == sum(range(10+1)) == 55
    print('All tests pass for `sum_recursively` (✿◠‿◠) ')
    total += 25
    
    # Test sumlist_recursively(l)
    print('Testing sumlist_recursively.')
    assert recursive_functions.sumlist_recursively([1,2,3]) == sum([1,2,3])
    assert recursive_functions.sumlist_recursively([42,16,99,102,1]) == sum([42,16,99,102,1])
    assert recursive_functions.sumlist_recursively([17,13,9,5,1]) == sum([17,13,9,5,1])
    print('All tests pass for r_sumlist (✿◠‿◠)\n')
    total += 25

    # Test reverse_recursively
    print('Testing reverse_recursively.')
    assert recursive_functions.reverse_recursively([1, 2, 3, 4]) == [4, 3, 2, 1]
    life = ['born', 'grow up', 'grow old']
    assert recursive_functions.reverse_recursively(life) == ['grow old', 'grow up', 'born']
    print('All tests pass for `reverse_recursively` (✿◠‿◠)\n')
    total += 25

    # Test multiply_recursively
    if total == 100:
        print('Testing multiply_recursively.')
        assert recursive_functions.multiply_recursively(5, 1) == 5*1 == 5
        assert recursive_functions.multiply_recursively(7, 4) == 7*4 == 28
        print('All tests pass for `multiply_recursively` (✿◠‿◠)\n')
        total+=5

    print("Total score: ", total)

main()
