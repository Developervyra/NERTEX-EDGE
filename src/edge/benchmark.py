"""
NERTEX EDGE
Benchmark Engine

Measures inference latency and summarizes results.
"""

import statistics
import time


def benchmark_model(model, inputs, warmup_runs=10, test_runs=100):
    """
    Benchmark a model's prediction speed.

    Returns measured latency statistics in milliseconds.
    """

    if warmup_runs < 0 or test_runs <= 0:
        raise ValueError("Invalid benchmark run counts.")

    # Warm-up phase
    for _ in range(warmup_runs):
        model.predict(inputs)

    measurements = []

    # Measurement phase
    for _ in range(test_runs):
        start_time = time.perf_counter()

        model.predict(inputs)

        end_time = time.perf_counter()

        latency_ms = (end_time - start_time) * 1000
        measurements.append(latency_ms)

    return {
        "runs": test_runs,
        "mean_latency_ms": statistics.mean(measurements),
        "median_latency_ms": statistics.median(measurements),
        "min_latency_ms": min(measurements),
        "max_latency_ms": max(measurements),
        "stdev_latency_ms": (
            statistics.stdev(measurements)
            if len(measurements) > 1
            else 0.0
        ),
    }