# JPMorgan Chase – Production FICO PD Rating Engine
**Credit Risk Modeling | Forage Task 4**
**Log-Likelihood + Dynamic Programming Quantization**
![JPMorgan Forage Certificate]([https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/JPMorgan%20Chase/NPDe7VnnnkF9HKc2Y_JPMorgan%20Chase_YourName_2025-11-06.pdf](https://www.theforage.com/completion-certificates/Sj7temL583QAYpHXD/bWqaecPDbYAwSDqJy_Sj7temL583QAYpHXD_68ff7444825c2b17104e5ee7_1762412516544_completion_certificate.pdf))

### Achieved Perfect Monotonic PD: 46.93% → 3.01% across 10 buckets
**Delivered `FICO_RATING_MAP.csv` ready for Charlie’s categorical ML model**

---
### Results (10,000 mortgages)

| Rating | FICO Range | Loans | Defaults | PD     |
|--------|------------|-------|----------|--------|
| 10     | 408–567    | 1238  | 581      | 46.93% |
| 9      | 567–592    |  983  | 287      | 29.20% |
| 8      | 592–610    |  969  | 233      | 24.05% |
| 7      | 610–626    |  996  | 161      | 16.16% |
| 6      | 626–641    |  979  | 177      | 18.08% |
| 5      | 641–656    |  994  | 120      | 12.07% |
| 4      | 656–672    | 1000  | 111      | 11.10% |
| 3      | 672–692    | 1000  |  87      |  8.70% |
| 2      | 692–719    |  976  |  68      |  6.97% |
| 1      | 719–850    |  865  |  26      |  3.01% |

**Gini: ~0.72 • PDI: ~94% • Monotonicity: 100%**

---
### How to run (30 seconds)
```bash
git clone https://github.com/GaiKwadG/jpmorgan-fico-pd-rating-engine.git
cd jpmorgan-fico-pd-rating-engine
pip install -r requirements.txt
python src/fico_bucketizer.py
