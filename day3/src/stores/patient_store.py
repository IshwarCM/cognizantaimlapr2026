from configuration.logger_configuration import configure_logger
from src.models.doctor import Doctor
from src.models.appointment import Appointment
from src.models.patient import Patient
from src.exceptions.patient_not_found_exception import PatientNotFoundException

logger = configure_logger()

class PatientStore:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient: Patient):
        self.patients.append(patient)
        logger.info(f"Patient added: {patient}")
    

    def get_patient_by_id(self, patient_id: int) -> Patient:
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
            else:
                logger.warning(f"Patient with ID {patient_id} not found.")
                raise PatientNotFoundException(f"Patient with ID {patient_id} not found.")
        
