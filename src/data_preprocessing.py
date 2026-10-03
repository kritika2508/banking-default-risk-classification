import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import resample


def missing_data_threshold(data, threshold=75):
    """Drop columns with missing values at or above the threshold percentage."""
    missing_data = pd.DataFrame(data.isna().sum(), columns=["missing_count"])
    missing_data["missing_perc"] = 100 * missing_data["missing_count"] / len(data)
    columns_to_be_deleted = missing_data[
        missing_data["missing_perc"] >= threshold
    ].index
    return data.drop(columns=columns_to_be_deleted)


def missing_data_treatment(data):
    """Fill categorical missing values with mode and numeric values with median."""
    for col in data.columns:
        if data[col].dtype == "object":
            data[col] = data[col].fillna(data[col].mode()[0])
        else:
            data[col] = data[col].fillna(data[col].median())
    return data


def unique_value_treatment(data):
    """Remove columns with one unique value or all unique values."""
    for col in list(data.columns):
        if data[col].nunique() == 1 or data[col].nunique() == len(data):
            del data[col]
    return data


def feature_engineering(data):
    """Create quartile buckets for sufficiently varied numeric columns."""
    for col in list(data.columns):
        if 100 * data[col].nunique() / len(data) > 5:
            if data[col].dtype != "object":
                data[f"{col}_bucket"] = pd.qcut(
                    data[col],
                    4,
                    labels=["b1", "b2", "b3", "b4"],
                    duplicates="drop",
                )
    return data


def label_encoding(data):
    """Encode categorical/category columns into numeric values."""
    for col in data.columns:
        if (data[col].dtype == "object") or (data[col].dtype == "category"):
            encoder = LabelEncoder()
            data[col] = encoder.fit_transform(data[col])
    return data


def resampling(data, target_column, minority_class_value, multiply):
    """Upsample the selected minority class by the requested multiplier."""
    data_minor = data[data[target_column] == minority_class_value]
    data_minor = resample(
        data_minor,
        n_samples=multiply * len(data_minor),
        random_state=42,
    )
    return pd.concat([data, data_minor], ignore_index=True)
