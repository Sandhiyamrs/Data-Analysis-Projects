import pandas as pd

EXPECTED_SCHEMA = {
    "id": "int64",
    "feature1": "float64",
    "feature2": "float64",
    "target": "int64"
}

def validate_schema(df, expected_schema):
    errors = []
    for col, dtype in expected_schema.items():
        if col not in df.columns:
            errors.append(f"Missing column: {col}")
        elif str(df[col].dtype) != dtype:
            errors.append(
                f"Column {col} has dtype {df[col].dtype}, expected {dtype}"
            )
    return errors

if __name__ == "__main__":
    df = pd.read_csv("datasets/dataset1.csv")
    issues = validate_schema(df, EXPECTED_SCHEMA)

    if issues:
        print("Schema validation failed:")
        for issue in issues:
            print("-", issue)
    else:
        print("Schema validation passed.")
