from report_repair import two_sum, three_sum

def test():
    test_input = [1721, 979, 366, 299, 675, 1456]
    assert two_sum(test_input) == 514579, "Should be 514579" 
    assert three_sum(test_input) == 241861950, "Should be 241861950" 


if __name__ == "__main__":
    test()
    print("Everything passed")
