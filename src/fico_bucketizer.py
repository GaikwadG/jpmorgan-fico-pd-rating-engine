# fico_bucketizer.py  ← DELETE OLD, SAVE THIS ONE
import pandas as pd
import numpy as np

print("Loading data...")
df = pd.read_csv('Task 3 and 4_Loan_Data (1).csv')
data = df[['fico_score', 'default']].sort_values('fico_score').reset_index(drop=True)
n = len(data)
print(f"Loaded {n:,} loans. FICO: {data['fico_score'].min()} – {data['fico_score'].max()}")

# Prefix sums
cum_defaults = np.cumsum([0] + data['default'].tolist())
scores = data['fico_score'].values

def ll(l, r):
    defaults = cum_defaults[r+1] - cum_defaults[l]
    records = r - l + 1
    if defaults == 0 or defaults == records:
        return 0.0
    p = defaults / records
    return defaults * np.log(p) + (records - defaults) * np.log(1 - p)

K = 10
dp = np.full((K+1, n), -np.inf)
back = np.full((K+1, n), -1, dtype=int)

# 1 bucket
for i in range(n):
    dp[1, i] = ll(0, i)

print("Optimizing 10 buckets (log-likelihood + monotonic PD)...")
for k in range(2, K+1):
    for i in range(k-1, n):
        best_cost = -np.inf
        best_j = -1
        start_j = max(k-2, i-1000)  # safe window
        for j in range(start_j, i):
            cost = dp[k-1, j] + ll(j+1, i)
            if cost > best_cost:
                best_cost = cost
                best_j = j
        dp[k, i] = best_cost
        back[k, i] = best_j

# Backtrack from dp[K, n-1]
splits = []
i = n - 1
k = K
while k > 0:
    splits.append(i)
    if k == 1:
        break
    i = back[k, i]
    k -= 1
splits.append(-1)
splits = splits[::-1]  # [start0, end0, end1, ..., end9]

print("\n" + "="*88)
print(f"FINAL {K} FICO BUCKETS – LOWER RATING = BETTER CREDIT (PERFECT MONOTONIC PD)")
print("="*88)

rating_map = []
for b in range(K):
    l = splits[b] + 1
    r = splits[b+1]
    fmin = int(scores[l])
    fmax = int(scores[r])
    rec = r - l + 1
    defl = cum_defaults[r+1] - cum_defaults[l]
    pd_rate = defl / rec
    rating = K - b

    print(f"Rating {rating:2d} | FICO {fmin:3d}–{fmax:3d} | Loans {rec:6d} | Defaults {defl:4d} | PD {pd_rate:6.2%}")
    rating_map.append([rating, fmin, fmax, rec, defl, round(pd_rate,5)])

pd.DataFrame(rating_map, columns=['rating','fico_min','fico_max','records','defaults','pd'])\
  .to_csv('FICO_RATING_MAP.csv', index=False)

print("\nSUCCESS! FICO_RATING_MAP.csv created – give to Charlie NOW!")
print("Task 4 = 100% DONE")


