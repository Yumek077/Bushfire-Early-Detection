# E Group - Augmentation Strategy Study

## Objective

This experiment investigates how different data augmentation strategies affect the performance and generalization ability of the YOLOv8n wildfire smoke detection model.

Wildfire smoke is a difficult detection target because it often has blurry boundaries, weak texture features, semi-transparent appearance, and strong similarity to clouds or fog.

This experiment aims to evaluate whether different augmentation strategies can improve wildfire smoke detection performance.

---

# Experiment Settings

## Base Configuration

- Model: YOLOv8n
- Image Size: 640
- Epochs: 50
- Batch Size: 16
- Confidence Threshold: 0.25
- Seed: 42
- AMP: True
- Pretrained: True

---

# Augmentation Groups

| Experiment | Strategy |
|---|---|
| E1 | Default Augmentation |
| E2 | Strong Augmentation |
| E3 | Reduced Mosaic Strategy |

---

# Experiment Results

## E1 - Default Augmentation

| Metric | Value |
|---|---|
| Precision | 0.780 |
| Recall | 0.707 |
| mAP50 | 0.778 |
| mAP50-95 | 0.449 |

### Analysis

The default YOLOv8 augmentation pipeline achieved the best overall detection performance among all augmentation experiments.

It provided a strong balance between precision, recall, and localization accuracy.

---

## E2 - Strong Augmentation

| Metric | Value |
|---|---|
| Precision | 0.761 |
| Recall | 0.744 |
| mAP50 | 0.756 |
| mAP50-95 | 0.433 |

### Analysis

Strong augmentation achieved the highest recall among all experiments.

This suggests that aggressive augmentation improved the model’s sensitivity to difficult wildfire smoke and fire targets.

However, precision and mAP performance decreased, indicating that the model produced more unstable predictions and false positives.

---

## E3 - Reduced Mosaic Strategy

| Metric | Value |
|---|---|
| Precision | 0.766 |
| Recall | 0.697 |
| mAP50 | 0.770 |
| mAP50-95 | 0.447 |

### Analysis

Reducing Mosaic intensity maintained relatively stable detection performance.

Compared with E2, predictions became more stable, but the overall performance still did not exceed the default augmentation strategy.

---

# Comparison Analysis

| Experiment | Main Observation |
|---|---|
| E1 | Best overall detection performance |
| E2 | Highest recall but more unstable predictions |
| E3 | Stable performance but limited improvement |

Additional observations:

- Strong augmentation improved recall but reduced precision.
- Aggressive augmentation increased model sensitivity.
- Reduced Mosaic maintained stable smoke texture learning.
- Default augmentation achieved the best balance across all performance metrics.

---

# Recall and Generalization Discussion

## E2 - Strong Augmentation

E2 achieved the highest recall (0.744), indicating that the model became more sensitive to wildfire smoke and fire targets.

Possible advantages include:

- Better distant smoke detection
- Improved robustness under lighting variation
- Better adaptability to complex wildfire scenes

However:

- Precision decreased
- mAP performance decreased
- More unstable predictions appeared

This indicates that stronger augmentation made the model more aggressive but less precise.

---

## E3 - Reduced Mosaic Strategy

E3 slightly improved training stability compared with aggressive augmentation.

Reducing Mosaic intensity helped preserve more realistic smoke texture continuity.

However, the improvement was limited on the current dataset and did not outperform the default augmentation strategy.

---

# Conclusion

This experiment demonstrates that augmentation strategy affects wildfire smoke detection behavior.

### Main Conclusions

- Strong augmentation improved recall and sensitivity
- Strong augmentation also reduced precision and overall mAP
- Reduced Mosaic maintained stable performance
- Default YOLOv8 augmentation achieved the best overall balance

The results suggest that:

> More aggressive augmentation is not always better for wildfire smoke detection.

Among all augmentation strategies, the default YOLOv8 augmentation pipeline achieved the best balance between:

- Precision
- Recall
- mAP performance
- Training stability

Therefore, the project will continue using the default YOLOv8 augmentation strategy for later experiments.

---

# Best Configuration

## Best Overall Performance

| Parameter | Value |
|---|---|
| Model | YOLOv8n |
| Augmentation | Default |
| Image Size | 640 |
| Epochs | 50 |
| Precision | 0.780 |
| Recall | 0.707 |
| mAP50 | 0.778 |
| mAP50-95 | 0.449 |

## Highest Recall

| Parameter | Value |
|---|---|
| Model | YOLOv8n |
| Augmentation | Strong |
| Image Size | 640 |
| Epochs | 50 |
| Precision | 0.761 |
| Recall | 0.744 |
| mAP50 | 0.756 |
| mAP50-95 | 0.433 |