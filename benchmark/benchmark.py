import time
import csv
from pathlib import Path
from statistics import mean
from ultralytics import YOLO

IMAGE_DIR = Path("data")
OUTPUT_CSV = Path("benchmark_results.csv")

MODELS = {
    "YOLOv8n": "../backend/app/models/yolov8n.pt",
    "YOLOv8s": "../backend/app/models/yolov8s.pt",
    "RT-DETR": "../backend/app/models/transformer.pt",
}

IMG_SIZE = 512
WARMUP_RUNS = 5
BENCHMARK_ROUNDS = 3


def benchmark_model(name, model_path, image_paths):
    print(f"\nBenchmarking {name}...")

    model = YOLO(model_path)

    round_avg_times = []

    for round_idx in range(BENCHMARK_ROUNDS):
        print(f"  Round {round_idx + 1}/{BENCHMARK_ROUNDS}")

        # Warmup
        for img in image_paths[:WARMUP_RUNS]:
            model.predict(
                source=str(img),
                imgsz=IMG_SIZE,
                verbose=False
            )

        times = []

        for img in image_paths:
            start = time.perf_counter()

            model.predict(
                source=str(img),
                imgsz=IMG_SIZE,
                verbose=False
            )

            end = time.perf_counter()
            times.append(end - start)

        round_avg_time = mean(times)
        round_avg_times.append(round_avg_time)

        print(
            f"    Round {round_idx + 1} average: "
            f"{round_avg_time * 1000:.2f} ms/image, "
            f"{1 / round_avg_time:.2f} FPS"
        )

    final_avg_time = mean(round_avg_times)
    final_fps = 1 / final_avg_time

    return {
        "model": name,
        "num_images": len(image_paths),
        "rounds": BENCHMARK_ROUNDS,
        "avg_time_sec": final_avg_time,
        "avg_time_ms": final_avg_time * 1000,
        "fps": final_fps,
    }


def main():
    image_paths = (
        list(IMAGE_DIR.glob("*.jpg")) +
        list(IMAGE_DIR.glob("*.jpeg")) +
        list(IMAGE_DIR.glob("*.png"))
    )

    if not image_paths:
        raise FileNotFoundError(f"No images found in {IMAGE_DIR}")

    print(f"Found {len(image_paths)} images.")
    print(f"Running {BENCHMARK_ROUNDS} benchmark rounds per model.")

    results = []

    for name, model_path in MODELS.items():
        result = benchmark_model(name, model_path, image_paths)
        results.append(result)

        print(
            f"\n{name} final result: "
            f"{result['avg_time_ms']:.2f} ms/image, "
            f"{result['fps']:.2f} FPS"
        )

    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "model",
                "num_images",
                "rounds",
                "avg_time_sec",
                "avg_time_ms",
                "fps"
            ]
        )
        writer.writeheader()
        writer.writerows(results)

    print(f"\nSaved benchmark results to {OUTPUT_CSV}")


if __name__ == "__main__":
    main()