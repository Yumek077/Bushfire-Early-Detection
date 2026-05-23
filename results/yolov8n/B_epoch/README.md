# B Group - Epoch Comparison Experiment

## Objective

This experiment investigates how different training epochs affect the performance of the YOLOv8n wildfire smoke detection model.

After completing the A group image size experiments, the best image size (640×640) was selected and fixed for this stage. Only the number of training epochs was changed in this experiment.

---

# Experiment Settings

| Experiment | Epochs | Image Size | Batch Size | Model |
|---|---|---|---|---|
| B1 | 30 | 640 | 16 | YOLOv8n |
| B2 | 50 | 640 | 16 | YOLOv8n |
| B3 | 80 | 640 | 16 | YOLOv8n |

Common training settings:

- Pretrained: True
- AMP: True
- Workers: 8
- Seed: 42
- Device: NVIDIA Tesla T4

---

# Experiment Results

## B1 - 30 Epochs

| Metric | Value |
|---|---|
| Precision | 0.758 |
| Recall | 0.691 |
| mAP50 | 0.762 |
| mAP50-95 | 0.433 |

### Analysis

The 30-epoch model achieved acceptable detection performance but did not fully converge. Compared with later experiments, all major performance metrics remained lower.

This suggests that 30 epochs may be insufficient for fully learning wildfire smoke and fire features.

---

## B2 - 50 Epochs

| Metric | Value |
|---|---|
| Precision | 0.780 |
| Recall | 0.707 |
| mAP50 | 0.778 |
| mAP50-95 | 0.449 |

### Analysis

The 50-epoch model significantly improved over B1 in all performance metrics. Precision, recall, and mAP values became more stable, indicating that the model had reached a better convergence state.

This setting provided a strong balance between detection accuracy and training efficiency.

---

## B3 - 80 Epochs

| Metric | Value |
|---|---|
| Precision | 0.782 |
| Recall | 0.714 |
| mAP50 | 0.783 |
| mAP50-95 | 0.455 |

### Analysis

The 80-epoch model achieved the highest numerical performance across all evaluation metrics.

Compared with B2, precision, recall, mAP50, and mAP50-95 all improved slightly, indicating that additional training helped the model learn more robust wildfire smoke and fire features.

However, the improvements over the 50-epoch configuration were relatively small while training cost increased noticeably, suggesting diminishing returns from longer training.

---

# Comparison Analysis

| Experiment | Main Observation |
|---|---|
| B1 | Training was insufficient and the model had not fully converged |
| B2 | Best balance between accuracy and efficiency |
| B3 | Highest performance but only slight improvement |

Additional observations:

- Increasing training epochs improved overall detection performance.
- Smoke detection remained consistently strong across all experiments.
- Fire detection benefited more from additional training.
- Performance gains became smaller after 50 epochs.

---


# Conclusion

This experiment demonstrates that increasing the number of training epochs improves wildfire smoke detection performance up to a certain point.

The 30-epoch model did not fully converge and produced lower performance. Increasing to 50 epochs significantly improved detection accuracy and training stability. Extending training to 80 epochs produced the best numerical results, but the performance gains were relatively small compared with the additional computational cost.

Therefore, **50 epochs provides the best practical balance between accuracy and efficiency**, while **80 epochs achieves the highest absolute detection performance and can be preferred when computational cost is less important**.

---

# Best Configuration

## Best Trade-off

| Parameter | Value |
|---|---|
| Model | YOLOv8n |
| Epochs | 50 |
| Image Size | 640 |
| Batch Size | 16 |
| Precision | 0.780 |
| Recall | 0.707 |
| mAP50 | 0.778 |
| mAP50-95 | 0.449 |

## Best Absolute Performance

| Parameter | Value |
|---|---|
| Model | YOLOv8n |
| Epochs | 80 |
| Image Size | 640 |
| Batch Size | 16 |
| Precision | 0.782 |
| Recall | 0.714 |
| mAP50 | 0.783 |
| mAP50-95 | 0.455 |