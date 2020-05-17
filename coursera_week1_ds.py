"""
Problem 5: Maximum in Sliding Window

Problem Introduction Given a sequence 𝑎1, . . . , 𝑎𝑛 of integers and an integer 𝑚 ≤ 𝑛, find the maximum among {
𝑎𝑖, . . . , 𝑎𝑖+𝑚−1} for every 1 ≤ 𝑖 ≤ 𝑛 − 𝑚 + 1. A naive 𝑂(𝑛𝑚) algorithm for solving this problem scans
each window separately. Your goal is to design an 𝑂(𝑛) algorithm. Problem Description Input Format. The first line
contains an integer 𝑛, the second line contains 𝑛 integers 𝑎1, . . . , 𝑎𝑛 separated by spaces, the third line
contains an integer 𝑚. Constraints. 1≤𝑛≤105,1≤𝑚≤𝑛,0≤𝑎𝑖 ≤105 for all 1≤ 𝑖 ≤ 𝑛.

OutputFormat. Output max{𝑎𝑖,...,𝑎𝑖+𝑚−1} for every 1 ≤ 𝑖 ≤ 𝑛 − 𝑚 + 1.
"""


# arr is the array of input numbers and k is the number
def printMax(arr, n, k):
    maximum = 0
    for i in range(n - k + 1):
        maximum = arr[i]
        for j in range(1, k):
            if arr[i + j] > maximum:
                maximum = arr[i + j]
        print(str(maximum) + " ", end="")

    # Driver method


if __name__ == "__main__":
    arr_input = [12, 1, 78, 90, 57, 89, 56]
    length = len(arr_input)
    kx = 3
    printMax(arr_input, length, kx)