# A Group - Image Size Comparison Experiment
## Objective

This experiment investigates how different image sizes affect the performance of the YOLOv8n wildfire smoke detection model.

Image resolution directly influences feature extraction quality, computational cost, and detection accuracy. Three different image sizes were tested while keeping all other training settings unchanged.

# Experiment Settings
Experiment	Image Size	Epochs	Batch Size	Model
A1	512 × 512	50	16	YOLOv8n
A2	640 × 640	50	16	YOLOv8n
A3	768 × 768	50	16	YOLOv8n

Common training settings:

Pretrained: True
AMP: True
Workers: 8
Seed: 42
Device: NVIDIA Tesla T4

## Experiment Results
## A1 - 512 × 512
Metric	Value
Precision	0.763
Recall	0.686
mAP50	0.753
mAP50-95	0.434
## Analysis

The 512×512 model achieved relatively fast training speed with lower computational cost. However, the smaller image resolution limited the model’s ability to capture detailed wildfire smoke and fire features, especially for small or distant targets.

Detection accuracy was the lowest among all experiments, indicating that excessive downsampling reduced feature representation quality.

# A2 - 640 × 640
Metric	Value
Precision	0.780
Recall	0.707
mAP50	0.778
mAP50-95	0.449
## Analysis

## Analysis

The 640×640 model achieved strong overall detection performance and provided a good balance between precision, recall, and computational efficiency.

Although the 768×768 configuration produced slightly higher mAP values, the improvement was very limited while requiring higher computational cost and longer training time.

Therefore, 640×640 was considered the most practical configuration for later experiments.

## A3 - 768 × 768
Metric	Value
Precision	0.777
Recall	0.700
mAP50	0.780
mAP50-95	0.450
## Analysis

## Analysis

The 768×768 model achieved the highest mAP50 (0.780) and slightly improved mAP50-95 (0.450), indicating slightly better localization performance.

However, precision and recall did not improve compared with the 640×640 configuration, while training time and computational cost increased noticeably.

This suggests that larger image sizes may provide marginal accuracy gains but do not offer practical overall advantages for this wildfire detection dataset.

## Comparison Analysis
Experiment	Main Observation
A1	Lower image size reduced detection accuracy
A2	Best balance between accuracy and efficiency
A3	Slight mAP improvement with higher computational costcomputational cost

Additional observations:

Increasing image size improved the model’s ability to detect detailed smoke and fire features.
Very small image sizes reduced detection performance.
Increasing image size beyond 640×640 did not significantly improve overall accuracy.
Larger image sizes required more computational resources and longer training time.
## Conclusion

## Conclusion

This experiment demonstrates that image size has a significant influence on wildfire smoke detection performance.

Smaller image sizes reduce computational cost but may weaken feature extraction ability, especially for small or distant smoke targets. Larger image sizes can provide slight improvements in detection metrics, but they also require more training time and computational resources.

Although 768×768 achieved slightly higher mAP values, the improvement was marginal. Overall, 640×640 provided the best balance between detection performance, training efficiency, and practical usability, making it the preferred configuration for later experiments.

## Best Configuration
Parameter	Value
Model	YOLOv8n
Image Size	640 × 640
Epochs	50
Batch Size	16
Precision	0.780
Recall	0.707
mAP50	0.778
mAP50-95	0.449