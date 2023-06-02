import pytest

# Test case for reversing List1
def test_reverse_list1():
    List1 = [8, 9, 3, 6, 1, 10]
    List1.reverse()
    assert List1 == [10, 1, 6, 3, 9, 8]

# Test case for sorting List2
def test_sort_list2():
    List2 = [91, 67, 120, 34, 76, 54, 78, 87, 56, 64, 345]
    List2.sort()
    assert List2 == [34, 54, 56, 64, 67, 76, 78, 87, 91, 120, 345]

# Test case for copying List1 to List3
def test_copy_list1_to_list3():
    List1 = [8, 9, 3, 6, 1, 10]
    List3 = List1.copy()
    assert List3 == [8, 9, 3, 6, 1, 10]

# Test case for extracting index values from List2
def test_extract_index_values():
    List2 = [91, 67, 120, 34, 76, 54, 78, 87, 56, 64, 345]
    indexvalue = List2[2:6]
    assert indexvalue == [120, 34, 76, 54]
