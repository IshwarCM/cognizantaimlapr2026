from configuration.logger_configuration import configure_logger
from src.models.doctor import Doctor
from src.models.appointment import Appointment
from src.models.patient import Patient
from src.exceptions.doctor_not_found_exception import DoctorNotFoundException

logger = configure_logger()

class DoctorStore:
    def __init__(self):
        self.doctors = []

    def add_doctor(self, doctor: Doctor):
        self.doctors.append(doctor)
        logger.info(f"Doctor added: {doctor}")

    def get_doctor_by_id(self, doctor_id: int) -> Doctor:
        for doctor in self.doctors:
            if doctor.id == doctor_id:
                return doctor
            else:
                logger.warning(f"Doctor with ID {doctor_id} not found.")
                raise DoctorNotFoundException(f"Doctor with ID {doctor_id} not found.")


    def get_doctors_by_specialization(self, specialization: str) -> list[Doctor]:
        return [doctor for doctor in self.doctors if doctor.specialization == specialization]
    
    def get_all_doctors(self) -> list[Doctor]:
        return self.doctors

    def __str__(self):
        return f"Doctor Store with {len(self.doctors)} doctors."