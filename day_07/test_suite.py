class TestSuite():
    def assert_equals(actual, expected, test_name=""):
        if actual == expected:
            print("test {} passed!".format(test_name))
        else:
            print("FAILED: test {} failed.".format(test_name))
            print("Expected: {}".format(expected))
            print("Got: {}".format(actual))
