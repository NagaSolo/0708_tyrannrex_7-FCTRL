''' given N number, count the zeros of its factorial output

    input:
    T -> testcases, 0 <= T <= 10_000
    N -> number, 1 <= N <= 1_000_000_000

    processor:
    function Z(N) -> count the zeros of factorial N output

    output:
    non-negative Z(N)

    Example
    
    Sample Input:
    6
    3
    60
    100
    1024
    23456
    8735373
    
    Sample Output:
    0
    14
    24
    253
    5861
    2183837

'''

testcases = int(input())
for test in range(testcases):
    print(test)