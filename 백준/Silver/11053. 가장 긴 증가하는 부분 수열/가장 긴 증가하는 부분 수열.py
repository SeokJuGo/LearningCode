def dp_test(n,arr):
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j] :
                dp[i] = max(dp[i],dp[j]+1)
    return(max(dp))
n=int(input())
arr=list(map(int,input().split()))
print(dp_test(n,arr))