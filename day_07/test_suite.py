class TestSuite():
    def assert_equals(actual, expected):
        if actual == expected:
            print("test passed!")
        else:
            print("FAILED: test failed.")
            print("Expected: {}".format(expected))
            print("Got: {}".format(actual))
