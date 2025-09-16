# 5. Hospital Patient Management
def search_patients(patients, disease):
    return [p["Name"] for p in patients if p["Disease"].lower() == disease.lower()]

if __name__ == "__main__":
    patients = [
        {"Name": "Alice", "Age": 30, "Disease": "Flu"},
        {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
        {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
    ]

    search_disease = "Flu"
    print(f"Patients with {search_disease}: {search_patients(patients, search_disease)}")