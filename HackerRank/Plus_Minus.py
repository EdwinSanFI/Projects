def plusMinus(arr):
    arr.sort()
    positives = 0
    negatives = 0
    zeros = 0

    for i in arr:
        if i < 0:
            negatives+=1
        elif i == 0:
            zeros += 1
        else:
            positives += 1

    total = positives + negatives + zeros

    if positives > 0:
        fractionP = total / positives
        print("{:.5f}".format(1/fractionP))
    else:
        print("0.00000")

    if negatives > 0:
        fractionN = total / negatives
        print("{:.5f}".format(1/fractionN))
    else:
        print("0.00000")

    if zeros > 0:
        fractionZ = total / zeros
        print("{:.5f}".format(1/fractionZ))
    else:
        print("0.00000")

if __name__ == '__main__':
    test4 = [55, 48, 48, 45, 91, 97, 45, 1, 39, 54, 36, 6, 19, 35, 66, 36, 72,
    93, 38, 21, 65, 70, 36, 63, 39, 76, 82, 26, 67, 29, 24, 82, 62, 53, 1, 50, 47, 65, 67, 19, 66, 90, 77]
    # Expected output:
    # 1.000000
    # 0.000000
    # 0.000000

    # test8 = [-6, 1, 79, 17, 64, 94, 87, -77, 0, -26, 2, -94, 87, -81, -73, -28, 43, 0, -35, 39, -37, -49, -29, 93, 64, 54, 0, -73, -58,
    #  -100, 33, -75, -47, 35, -7, 0, 52, -37, -99, 58, -23, 70, -52, 18, 0, -79, -38, 45, -61, 45, 51, -48, 32, 0, -44, -56, 29, -74, -1, 92,
    #  -93, 23, 0, 55, -31, 75, -43, 20, 19, 58, -4, 0, 59, -80, 18, -74, 81, 63, 62, -92, 0, -23, 7, -91, 22, -1,
    #  38, -73, 79, 0, -2, 90, 80, 74, -74, -85, -48, 31, 0, -80]

    # Expected output:
    # 0.440000
    # 0.450000
    # 0.110000


    # test10 = [-100, 100, 0, 0, 0, -100, 100, 0, -100, 100, 100, 0, 0, 0, 0, -100, -100, -100, 0, -100, 0, 100, 100, -100, -100,
    # 100, 100, 100, 100, -100, -100, -100, -100, 100, 0, 0, 100, 0, 0, -100, -100, -100, -100, -100, -100, 100, 100, 0, 100, 100,
    #  -100, -100, -100, 0, 100, -100, 0, 100, 100, -100, 100, -100, 0, -100, -100, 100, 0, 0, -100, 0, -100, -100, 100, -100, 100,
    #  0, 100, -100, -100, -100, 100, 100, 100, 100, 0, -100, 0, 100, 100, 100, 0, -100, -100, 0, 0, 100, 0, -100, 100, 100]

    # Expected output:
    # 0.340000
    # 0.380000
    # 0.280000

    plusMinus(test4)