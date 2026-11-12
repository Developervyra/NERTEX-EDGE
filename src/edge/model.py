"""
NERTEX EDGE
Lightweight AI Inference Model

Initial experimental implementation.
Uses a simple logistic model for inference testing.
"""

import math


class TinyLinearModel:
    """A lightweight logistic inference model."""

    def __init__(self, weights, bias=0.0):
        if not weights:
            raise ValueError("Weights cannot be empty.")

        self.weights = list(weights)
        self.bias = float(bias)

    def predict_proba(self, inputs):
        """Calculate the probability for a single input."""

        if len(inputs) != len(self.weights):
            raise ValueError(
                "Input dimensions must match model weights."
            )

        total = self.bias

        for weight, value in zip(self.weights, inputs):
            total += float(weight) * float(value)

        # Numerically stable sigmoid function
        if total >= 0:
            probability = 1.0 / (1.0 + math.exp(-total))
        else:
            exp_value = math.exp(total)
            probability = exp_value / (1.0 + exp_value)

        return probability

    def predict(self, inputs, threshold=0.5):
        """Return a binary prediction."""

        probability = self.predict_proba(inputs)
        return int(probability >= threshold)