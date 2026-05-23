# F Group — Learning Rate Study

## 1. Objective

This experiment studies the effect of different learning rate strategies on the convergence behavior and final detection performance of the YOLOv8n wildfire detection model.

The purpose is to analyze:

- Training stability
- Convergence behavior
- mAP performance
- Precision and Recall balance
- Overall optimization effectiveness

---

## 2. Experiment Settings

### Base Configuration

- Model: YOLOv8n
- Image Size: 640
- Epochs: 50
- Batch Size: 16
- Confidence Threshold: 0.25
- IoU Threshold: 0.5
- AMP: True
- Pretrained: True
- Seed: 42

### Learning Rate Groups

| Experiment | Learning Rate Strategy |
|---|---|
| F1 | Default Learning Rate |
| F2 | Lower Learning Rate |
| F3 | Cosine Learning Rate |

### Learning Rate Parameters

| Experiment | lr0 | lrf | cos_lr |
|---|---|---|---|
| F1 | 0.01 | 0.01 | False |
| F2 | 0.005 | 0.01 | False |
| F3 | 0.01 | 0.01 | True |

---

## 3. Quantitative Results

| Experiment | Precision | Recall | mAP50 | mAP50-95 |
|---|---|---|---|---|
| F1 (Default LR) | 0.779 | 0.707 | 0.779 | 0.449 |
| F2 (Lower LR) | 0.776 | 0.707 | 0.779 | 0.452 |
| F3 (Cosine LR) | 0.764 | 0.711 | 0.774 | 0.448 |

---

## 4. Training Curve Analysis

### F1 — Default Learning Rate

The default learning rate produced stable and smooth convergence behavior.

#### Observations

- Training loss steadily decreased throughout training
- Validation loss remained stable after convergence
- Precision and Recall improved consistently
- mAP50 and mAP50-95 gradually converged

The default learning rate achieved a good balance between convergence speed and final performance.

---

### F2 — Lower Learning Rate

The lower learning rate experiment produced highly similar results compared with the default learning rate configuration.

#### Observations

- Training curves were highly similar to F1
- Final Precision and Recall values showed almost no difference
- mAP50 remained unchanged
- mAP50-95 improved slightly

This indicates that reducing the initial learning rate from 0.01 to 0.005 produced only a small localization improvement under the current YOLOv8n training configuration.

---

### F3 — Cosine Learning Rate

The cosine learning rate strategy produced stable convergence behavior.

#### Observations

- Training curves remained smooth and stable
- Recall was slightly higher than F1
- Precision and mAP values were slightly lower than F1

The cosine learning rate schedule did not show significant overall performance improvement on the current wildfire smoke detection dataset.

---

## 5. Confusion Matrix Analysis

### Smoke Detection

| Experiment | Smoke Accuracy |
|---|---|
| F1 | Stable |
| F2 | Stable |
| F3 | Slight fluctuation |

The default and lower learning rate strategies maintained stable smoke recognition behavior.

---

### Fire Detection

| Experiment | Fire Accuracy |
|---|---|
| F1 | Stable |
| F2 | Stable |
| F3 | Slight fluctuation |

No major differences were observed in fire detection behavior.

---

### Background Predictions

All three experiments showed relatively similar background prediction behavior.

No abnormal false detection patterns were observed.

---

## 6. Learning Rate Discussion

This experiment shows that the YOLOv8n wildfire detection model is relatively stable under different learning rate strategies.

### Main Findings

- Lower learning rate slightly improved mAP50-95
- Lower learning rate did not significantly improve overall detection performance
- Cosine learning rate did not provide clear overall benefits
- Default learning rate maintained a strong overall balance between precision, recall, and convergence stability

---

## 7. Final Conclusion

The F group experiments demonstrate that the current YOLOv8n configuration is not highly sensitive to learning rate changes.

Although the lower learning rate strategy achieved a slightly higher mAP50-95 value, the improvement was very limited and did not produce clear overall detection advantages.

The default learning rate configuration achieved:

- Strong Precision performance
- Stable convergence behavior
- Reliable overall detection results
- Balanced performance across all major metrics

Therefore, **Default Learning Rate (lr0 = 0.01)** remains the preferred standard training setting for later experiments in this project.