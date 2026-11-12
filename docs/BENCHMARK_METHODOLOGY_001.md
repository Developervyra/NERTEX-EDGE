NERTEX EDGE

Benchmark Methodology 001

Document ID: NER-EDGE-BM-001
Project: NERTEX EDGE
Status: Proposed — Not Yet Executed

---

1. Purpose

This document establishes a consistent methodology for measuring and comparing AI inference performance before and after optimization.

The objective is to ensure that experimental results are fair, measurable, and reproducible.

2. Benchmark Objectives

The benchmark will evaluate:

1. Inference latency.
2. Memory consumption.
3. Model storage size.
4. Predictive accuracy.
5. Energy consumption, if reliable measurement is available.

3. Baseline Requirements

Before applying any optimization, the original model must be tested.

The baseline record must include:

- Model name and version.
- Dataset and version.
- Hardware specifications.
- Operating system.
- Programming language and library versions.
- Model configuration.
- Measurement conditions.

4. Experimental Procedure

Each experiment will follow the same general procedure:

1. Load the selected model.
2. Prepare the evaluation dataset.
3. Perform warm-up runs.
4. Execute repeated inference measurements.
5. Record latency and memory usage.
6. Evaluate predictive accuracy.
7. Save the results.
8. Repeat the process for the optimized model.

5. Measurement Rules

Inference Latency

Measure the time required for model inference.

Report the mean and variation across repeated measurements.

Memory Consumption

Record memory usage during inference using the same measurement method for each experiment.

Model Size

Record the storage size of the original and optimized model files.

Predictive Accuracy

Use the same evaluation dataset and metric for both models.

Energy Consumption

Report energy measurements only when suitable measurement equipment or reliable instrumentation is available.

6. Fair Comparison Requirements

- Use identical evaluation data.
- Keep hardware conditions consistent.
- Use equivalent measurement procedures.
- Document software versions.
- Avoid selectively reporting favorable results.
- Record unsuccessful experiments.
- Distinguish measured results from estimates.

7. Result Reporting Format

Each experiment should record:

Metric| Baseline| Optimized
Model size| Pending| Pending
Mean latency| Pending| Pending
Peak memory| Pending| Pending
Accuracy| Pending| Pending
Energy| Pending| Pending

No values should be entered until measurements have actually been performed.

8. Performance Improvement Calculation

For latency:

Improvement percentage =

((Baseline latency − Optimized latency) / Baseline latency) × 100

A positive result indicates lower inference latency.

Accuracy must be evaluated separately to identify any quality reduction.

9. Reproducibility

Every benchmark must include enough information for another researcher to reproduce the experiment.

Experiment logs, configurations, scripts, and results should be maintained in the repository.

10. Limitations

Benchmark results are specific to their experimental conditions.

Results obtained on one device must not automatically be generalized to all hardware.

11. Current Status

Methodology: Documented
Experiments: Not started
Results: Not available

---

NERTEX EDGE — Research. Optimize. Innovate.