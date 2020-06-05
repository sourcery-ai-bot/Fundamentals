from app import reverse_list

def test_reverse_list_01():
    test_list = ['a', 'b', 'c', 'd']
    expected = ['d', 'c', 'b', 'a']
    actual = reverse_list(test_list)

    if actual == expected:
        print("test reverse list passed!")
    else:
        print("FAILED: test reverse list failed.")
        print("Expected: {}".format(expected))
        print("Got: {}".format(actual))

def test_reverse_list_02():
    test_list = ['aa', 'bb', 'cc', 'dd']
    expected = ['dd', 'cc', 'bb', 'aa']
    actual = reverse_list(test_list)

    if actual == expected:
        print("test reverse list passed!")
    else:
        print("FAILED: test reverse list failed.")
        print("Expected: {}".format(expected))
        print("Got: {}".format(actual))


def run_tests():
    test_reverse_list_01()
    test_reverse_list_02()

run_tests()