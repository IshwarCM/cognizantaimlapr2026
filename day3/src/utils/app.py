import sys
import os
from datetime import date, datetime

# Get absolute path of project root (day3)
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../")
)

# Add project root to sys.path if not already present
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from configuration.logger_configuration import configure_logger

# Stores
from src.stores.doctor_store import DoctorStore
from src.stores.patient_store import PatientStore
from src.stores.appointment_store import AppointmentStore

# Models
from src.models.doctor import Doctor
from src.models.patient import Patient
from src.models.appointment import Appointment

"""
Entry point for the application.
This module initializes the application and runs the main logic.
"""

logger = configure_logger()


def run():
    logger.info("Running the application...")

    # Initialize stores
    doctor_store = DoctorStore()
    patient_store = PatientStore()
    appointment_store = AppointmentStore()

    # Add Doctor
    doctor = Doctor(
        name="Dr. Alice",
        id=1,
        specialty="Neurology"
    )
    doctor_store.add_doctor(doctor)

    # Add Patient
    patient = Patient(
        name="Bob Williams",
        id=101,
        dob=date(1988, 3, 12),
        disease="Migraine"
    )
    patient_store.add_patient(patient)

    # Add Appointment
    appointment = Appointment(
        id=1001,
        patient_id=patient.id,
        doctor_id=doctor.id,
        date=datetime(2026, 4, 20),
        time=datetime.strptime("11:00", "%H:%M")
    )
    appointment_store.add_appointment(appointment)

    logger.info("Application finished successfully.")


# Handle entry point for the application
if __name__ == "__main__":
    run()