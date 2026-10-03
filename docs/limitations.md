# Limitations

1. This is an academic classification exercise, not a production lending model.
2. The dataset is highly imbalanced and the notebook uses resampling; this can affect estimated performance.
3. The notebook uses a single train/test split rather than cross-validation and out-of-time validation.
4. Feature encoding and modelling choices should be revisited before deployment.
5. No probability calibration or business-cost-based threshold optimization is included.
6. No fairness assessment is performed across demographic groups.
7. Observational associations should not be interpreted as causal drivers of default.
8. Real-world lending deployment would require governance, explainability, privacy and regulatory controls.
