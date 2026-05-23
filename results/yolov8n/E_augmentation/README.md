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
| Precision | 0.764 |
| Recall | 0.681 |
| mAP50 | 0.756 |
| mAP50-95 | 0.433 |

### Analysis

Strong augmentation reduced overall detection performance compared with the default augmentation strategy.

Precision, recall, and mAP metrics all decreased, suggesting that aggressive augmentation introduced additional visual noise and made the model less stable during wildfire smoke and fire detection.

This indicates that stronger augmentation did not improve generalization on the current wildfire dataset.

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

| Experiment | Main Observation                                    |
| E1         | Best overall detection performance  |
| E2         | Aggressive augmentation reduced
               overall performance |
| E3         | Stable performance but limited improvement |


Additional observations:

Additional observations:

- Strong augmentation reduced both precision and recall.
- Aggressive augmentation introduced additional training noise.
- Reduced Mosaic maintained relatively stable performance.
- Default augmentation achieved the best balance across all performance metrics.

---

# Recall and Generalization Discussion

## E2 - Strong Augmentation

Strong augmentation did not improve wildfire smoke detection performance on the current dataset.

Possible reasons include:

- Excessive visual distortion
- More unstable smoke texture representation
- Increased difficulty in feature learning

Observed effects:

- Precision decreased
- Recall decreased
- mAP performance decreased

This indicates that stronger augmentation made training less stable and did not improve practical wildfire detection performance in this experiment.

---

## E3 - Reduced Mosaic Strategy

E3 slightly improved training stability compared with aggressive augmentation.

Reducing Mosaic intensity helped preserve more realistic smoke texture continuity.

However, the improvement was limited on the current dataset and did not outperform the default augmentation strategy.

---

# Conclusion

This experiment demonstrates that augmentation strategy affects wildfire smoke detection behavior.

### Main Conclusions

- Strong augmentation reduced overall detection performance
- Reduced Mosaic maintained relatively stable performance
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

## Alternative Augmentation Setting

| Parameter | Value |
|---|---|
| Model | YOLOv8n |
| Augmentation | Strong |
| Image Size | 640 |
| Epochs | 50 |
| Precision | 0.764 |
| Recall | 0.681 |
| mAP50 | 0.756 |
| mAP50-95 | 0.433 |