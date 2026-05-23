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
Analysis

The 640×640 model achieved the best overall detection performance among all experiments. Precision, recall, and mAP50 all reached the highest values, while computational cost remained manageable.

This resolution provided a strong balance between feature detail and training efficiency.

## A3 - 768 × 768
Metric	Value
Precision	0.777
Recall	0.700
mAP50	0.773
mAP50-95	0.450
Analysis

The 768×768 model provided slightly improved localization performance (mAP50-95) compared with 640×640, but the improvement was negligible.

Training time and computational cost increased noticeably, while overall detection performance did not improve significantly.

This suggests that excessively large image sizes may not provide practical benefits for this wildfire detection dataset.

## Comparison Analysis
Experiment	Main Observation
A1	Faster training but reduced detection accuracy
A2	Best balance between accuracy and efficiency
A3	Slight localization gain with higher computational cost

Additional observations:

Increasing image size improved the model’s ability to detect detailed smoke and fire features.
Very small image sizes reduced detection performance.
Increasing image size beyond 640×640 did not significantly improve overall accuracy.
Larger image sizes required more computational resources and longer training time.
## Conclusion

This experiment demonstrates that image size has a significant impact on wildfire smoke detection performance.

Smaller image sizes reduce computational cost but may limit feature extraction capability, while excessively large image sizes increase training complexity without providing meaningful overall performance gains.

Among all tested configurations, 640×640 achieved the best balance between detection accuracy, training stability, and computational efficiency, making it the most suitable setting for this wildfire detection dataset.

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