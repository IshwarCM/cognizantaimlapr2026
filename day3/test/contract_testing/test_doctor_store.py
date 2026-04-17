import os 
import sys
import pytest
from src.stores.doctor_store import DoctorStore
from src.models.doctor import Doctor
from src.exceptions.doctor_not_found_exception import DoctorNotFoundException

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(PROJECT_ROOT)


def test_doctor_not_found_exception():
    store = DoctorStore()
    store.add_doctor(Doctor(id=1, name="Dr Smith", specialization="Cardiology"))

    with pytest.raises(DoctorNotFoundException):
        store.get_doctor_by_id(99)