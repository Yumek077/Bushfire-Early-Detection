# C Group - Confidence Threshold Study

## Objective

This experiment investigates how different confidence thresholds affect the wildfire smoke and fire detection performance of the YOLOv8n model.

The confidence threshold controls how strict the model is when deciding whether a detected object should be accepted as a valid prediction. Lower thresholds may detect more targets but can introduce more false positives, while higher thresholds produce cleaner predictions but may miss important wildfire targets.

---

# Experiment Settings

| Experiment | Confidence Threshold | Image Size | Epochs | Model |
|---|---|---|---|---|
| C1 | 0.25 | 640 | 50 | YOLOv8n |
| C2 | 0.50 | 640 | 50 | YOLOv8n |
| C3 | 0.70 | 640 | 50 | YOLOv8n |

Common training settings:

- Pretrained: True
- Batch Size: 16
- Seed: 42
- Device: NVIDIA Tesla T4
- Best Weights: B2_epoch50/best.pt

---

# Experiment Results

## C1 - Confidence 0.25

| Metric | Value |
|---|---|
| Precision | 0.766 |
| Recall | 0.710 |
| mAP50 | 0.687 |
| mAP50-95 | 0.404 |

### Analysis


The confidence threshold of 0.25 achieved the highest recall and the best overall performance within the confidence threshold experiments.

This setting allowed the model to detect more smoke and fire targets, especially smaller or less obvious wildfire regions. Although more prediction boxes may appear, the model missed fewer important targets.

For wildfire early detection tasks, maintaining strong recall is generally more important than maximizing prediction strictness.
---

## C2 - Confidence 0.50

| Metric | Value |
|---|---|
| Precision | 0.882 |
| Recall | 0.586 |
| mAP50 | 0.560 |
| mAP50-95 | 0.347 |

### Analysis


Increasing the confidence threshold to 0.50 significantly improved precision and reduced false positive detections.

However, recall dropped noticeably, meaning that a considerable number of wildfire targets were missed. This setting produced cleaner predictions but reduced overall detection sensitivity and mAP performance.

---

## C3 - Confidence 0.70

| Metric | Value |
|---|---|
| Precision | 0.950 |
| Recall | 0.383 |
| mAP50 | 0.376 |
| mAP50-95 | 0.255 |

### Analysis

The confidence threshold of 0.70 produced the highest precision, meaning predictions were very strict and clean.

However, recall dropped significantly, indicating that many smoke and fire targets were missed. Although predictions became more reliable individually, overall wildfire detection performance became much weaker.

---

# Comparison Analysis

| Experiment | Main Observation |
|---|---|
| C1 |Highest recall and best overall detection |
| C2 | Better precision but lower recall |
| C3 | Highest precision but severe missed detections |

Additional observations:

- Increasing confidence threshold improved precision.
- Increasing confidence threshold reduced recall.
- mAP performance decreased as confidence threshold became too strict.
- Higher confidence thresholds filtered out more wildfire targets.

---

# Conclusion


This experiment demonstrates a clear trade-off between precision and recall when adjusting confidence thresholds.

Lower confidence thresholds detect more wildfire smoke and fire targets but may introduce more false positives. Higher confidence thresholds produce cleaner predictions but significantly increase missed detections.

For wildfire early detection systems, missing smoke or fire targets is generally more dangerous than producing some additional prediction boxes.

Therefore, confidence threshold = 0.25 provides the best practical balance for wildfire early detection in this experiment, especially because it maintains the strongest recall performance.

---

# Best Configuration

## Best Practical Configuration

| Parameter | Value |
|---|---|
| Model | YOLOv8n |
| Confidence Threshold | 0.25 |
| Image Size | 640 |
| Epochs | 50 |
| Precision | 0.766 |
| Recall | 0.710 |
| mAP50 | 0.687 |
| mAP50-95 | 0.404 |

## Highest Precision

| Parameter | Value |
|---|---|
| Model | YOLOv8n |
| Confidence Threshold | 0.70 |
| Image Size | 640 |
| Epochs | 50 |
| Precision | 0.950 |
| Recall | 0.383 |
| mAP50 | 0.376 |
| mAP50-95 | 0.255 |