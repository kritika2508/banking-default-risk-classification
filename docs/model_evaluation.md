# Model Evaluation Framework

## Why accuracy is not enough

The target is highly imbalanced: approximately 0.9% of observations are defaulters. A model could therefore achieve high accuracy while failing to identify a meaningful share of the minority class.

## Metrics

### Recall

`TP / (TP + FN)`

Measures the proportion of actual defaulters identified by the model.

### Precision

`TP / (TP + FP)`

Measures the proportion of predicted defaulters who are actually defaulters.

### F1

`2 × Precision × Recall / (Precision + Recall)`

Provides a single measure balancing precision and recall.

### Confusion Matrix

| | Actual Non-default | Actual Default |
|---|---|---|
| Predicted Non-default | True Negative | False Negative |
| Predicted Default | False Positive | True Positive |

The preferred operating threshold depends on the relative business cost of these errors.
