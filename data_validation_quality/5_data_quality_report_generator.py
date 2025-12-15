def generate_report(missing, outliers):
    return {
        "missing_values": missing,
        "outliers": outliers,
        "status": "FAIL" if missing or outliers else "PASS"
    }

print(generate_report(3, 1))
