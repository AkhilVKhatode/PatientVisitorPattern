from abc import ABC, abstractmethod


class Patient(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ChildPatient(Patient):
    def accept(self, visitor):
        visitor.visit(self)


class AdultPatient(Patient):
    def accept(self, visitor):
        visitor.visit(self)


class SeniorPatient(Patient):
    def accept(self, visitor):
        visitor.visit(self)


class Visitor(ABC):
    @abstractmethod
    def visit(self, child_patient):
        pass

    @abstractmethod
    def visit(self, adult_patient):
        pass

    @abstractmethod
    def visit(self, senior_patient):
        pass


class DiagnosisVisitor(Visitor):
    def visit(self, child_patient):
        print("Diagnosing a child patient: Check-up and pediatric care.")

    def visit(self, adult_patient):
        print("Diagnosing an adult patient: Routine exams and lifestyle advice.")

    def visit(self, senior_patient):
        print("Diagnosing a senior patient: Comprehensive geriatric evaluation.")


class BillingVisitor(Visitor):
    def visit(self, child_patient):
        print("Calculating billing for a child patient.")

    def visit(self, adult_patient):
        print("Calculating billing for an adult patient.")

    def visit(self, senior_patient):
        print("Calculating billing for a senior patient.")


# Client code
if __name__ == "__main__":
    # Create a list of patients
    patients = [ChildPatient(), AdultPatient(), SeniorPatient()]

    # Create visitors for different operations
    diagnosis_visitor = DiagnosisVisitor()
    billing_visitor = BillingVisitor()

    # Each patient accepts the visitors to perform the operations
    for patient in patients:
        patient.accept(diagnosis_visitor)
        patient.accept(billing_visitor)
