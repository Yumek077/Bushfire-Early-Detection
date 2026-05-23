# D Group - Seed Stability Study

## Objective

This experiment investigates the stability and reproducibility of the YOLOv8n wildfire smoke detection model under different random seeds.

Deep learning training contains random initialization and stochastic behavior. This experiment aims to verify whether the current best YOLOv8n configuration can produce stable results across multiple training runs.

---

# Experiment Settings

## Base Configuration

- Model: YOLOv8n
- Image Size: 640
- Epochs: 50
- Batch Size: 16
- Confidence Threshold: 0.25
- AMP: True
- Pretrained: True

## Seed Groups

| Experiment | Random Seed |
|---|---|
| D1 | 42 |
| D2 | 43 |
| D3 | 44 |

---

# Experiment Results

## D1 - Seed 42

| Metric | Value |
|---|---|
| Precision | 0.780 |
| Recall | 0.707 |
| mAP50 | 0.778 |
| mAP50-95 | 0.449 |

### Analysis

The baseline seed (42) achieved the strongest overall performance in this seed stability experiment and served as the reference configuration for later comparisons.

This result indicates that the default training configuration already provided stable and reliable wildfire detection performance.

---

## D2 - Seed 43

| Metric | Value |
|---|---|
| Precision | 0.763 |
| Recall | 0.712 |
| mAP50 | 0.771 |
| mAP50-95 | 0.447 |

### Analysis

Compared with D1, the model produced nearly identical results. Precision and recall changed only slightly, while mAP performance remained the same.

This indicates very stable training behavior.

---

## D3 - Seed 44

| Metric | Value |
|---|---|
| Precision | 0.772 |
| Recall | 0.700 |
| mAP50 | 0.773 |
| mAP50-95 | 0.444 |

### Analysis

The third seed also achieved very similar detection performance.

Although some metrics fluctuated slightly, the differences remained very small and within expected random variation.

---

# Comparison Analysis

| Experiment | Main Observation |
|---|---|
| D1 | Baseline reference performance |
| D2 | Almost identical to D1 |
| D3 | Slight metric fluctuation but overall stable |

Additional observations:

- Precision remained in a narrow range (0.763–0.780)
- Recall remained stable (0.700–0.712)
- mAP50 changed only slightly (0.771–0.778)
- mAP50-95 remained highly consistent (0.444–0.449)

---

# Stability Discussion

This experiment demonstrates that the YOLOv8n wildfire smoke detection model is relatively stable across different random seeds.

The performance differences between D1, D2, and D3 were small, indicating that the final detection results were not strongly affected by random initialization.

Compared with parameter tuning experiments (A/B/C), the D group focuses on:

- Training reproducibility
- Stability validation
- Reliability of final model performance

The highly similar metrics across all experiments indicate that the model has good robustness during training.

---

# Conclusion

The D group experiments confirm that the current YOLOv8n wildfire smoke detection configuration is stable across different random seeds.

All three experiments achieved very similar:

- Precision
- Recall
- mAP50
- mAP50-95

This indicates that the current training configuration is reliable and reproducible for later deployment and further optimization.

Therefore, the project will continue using:

**Seed = 42**

as the default training setting for future experiments.

---

# Recommended Configuration

| Parameter            | Value     |
| -------------------- | --------- |
| Model                | YOLOv8n   |
| Seed                 | 42        |
| Image Size           | 640       |
| Epochs               | 50        |
| Batch Size           | 16        |
| Confidence Threshold | 0.25      |
| Precision            | 0.780 |
| Recall               | 0.707 |
| mAP50                | 0.778 |
| mAP50-95             | 0.449 |
