from pyradix import sort


def test_sort(array1):
    array_for_radix_sort = array1[:]
    array_for_qsort = array1[:]
    assert sorted(array_for_qsort) = sort(array_for_radix_sort)
