expected_cols = {"id", "name", "age"}
actual_cols = {"id", "name"}

missing = expected_cols - actual_cols
print("Missing Columns:", missing)
