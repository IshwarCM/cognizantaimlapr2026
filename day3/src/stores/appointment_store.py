from configuration.logger_configuration import configure_logger
from src.models.doctor import Doctor
from src.models.appointment import Appointment
from src.models.patient import Patient

logger = configure_logger() 

class AppointmentStore:
    def __init__(self):
        self.appointments = []

    def add_appointment(self, appointment: Appointment):
        self.appointments.append(appointment)
        logger.info(f"Appointment added: {appointment}")

    def get_appointments_by_patient_id(self, patient_id: int) -> list[Appointment]:
        apointments =  [appointment for appointment in self.appointments if appointment.patient_id == patient_id]
        return apointments

    def get_appointments_by_doctor_id(self, doctor_id: int) -> list[Appointment]:
        appointments = [appointment for appointment in self.appointments if appointment.doctor_id == doctor_id]
        return appointments

    def __str__(self):
        return f"Appointment Store with {len(self.appointments)} appointments."