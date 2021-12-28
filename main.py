def avg(nums):
    sum = 0
    for i in nums:
        sum += i
    average = (sum / len(nums))
    return average


if __name__ == '__main__':

    nums = list(map(int, input().split()))
    res = avg(nums)
    print(f'{res:.2f}')