"""Tests for Patient contract testing"""

import csv
import os
import sys
import pytest
from datetime import date

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(PROJECT_ROOT)

from src.models.patient import Patient


@pytest.fixture
def initialize_patient():
    """Initialize a patient instance for testing"""
    return Patient(
        name="Aarav Menon",
        id=1001,
        dob=date(1985, 3, 12),
        disease="Diabetes"
    )


def read_patient_from_csv():
    """Read patient data from CSV and return list of tuples"""

    csv_path = os.path.join(
        PROJECT_ROOT, "test", "patients.csv"
    )

    test_data = []
    with open(csv_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            test_data.append(
                (
                    row["name"],
                    int(row["id"]),
                    date.fromisoformat(row["dob"]),
                    row["disease"],
                )
            )

    return test_data


def test_patient_creation(initialize_patient):
    """Test the creation of a Patient instance"""
    patient = initialize_patient
    assert patient.name == "Aarav Menon"
    assert patient.id == 1001
    assert patient.dob == date(1985, 3, 12)
    assert patient.disease == "Diabetes"


@pytest.mark.parametrize(
    "name, patient_id, dob, disease",
    read_patient_from_csv()
)
def test_parameterized_patient_creation(name, patient_id, dob, disease):
    """Test Patient creation using CSV-driven data"""
    patient = Patient(
        name=name,
        id=patient_id,
        dob=dob,
        disease=disease
    )
# pytest day3/test/contract_testing/test_patient.py
    assert patient.name == name
    assert patient.id == patient_id
    assert patient.dob == dob
    assert patient.disease == disease