"""Tests for Doctor contract testing"""

import csv
import os
import sys
import pytest

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(PROJECT_ROOT)

from src.models.doctor import Doctor


@pytest.fixture
def initialize_doctor():
    """Initialize a doctor instance for testing"""
    return Doctor(id=1, name="John Doe", specialty="Cardiology")


def read_doctor_from_csv():
    """Read doctor data from CSV and return list of tuples"""

    csv_path = os.path.join(
        PROJECT_ROOT, "test", "doctors.csv"
    )

    test_data = []
    with open(csv_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            test_data.append(
                (int(row["id"]), row["name"], row["specialty"])
            )

    return test_data


def test_doctor_creation(initialize_doctor):
    """Test the creation of a Doctor instance"""
    doctor = initialize_doctor
    assert doctor.id == 1
    assert doctor.name == "John Doe"
    assert doctor.specialty == "Cardiology"


@pytest.mark.parametrize(
    "doctor_id, name, specialty",
    read_doctor_from_csv()
)
def test_parameterized_doctor_creation(doctor_id, name, specialty):
    """Test Doctor creation using CSV-driven data"""
    doctor = Doctor(id=doctor_id, name=name, specialty=specialty)

    assert doctor.id == doctor_id
    assert doctor.name == name
    assert doctor.specialty == specialty