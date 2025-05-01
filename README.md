# Hospital Visitor Design Pattern

This project demonstrates the **Visitor Design Pattern** in Java, applied to a hospital system where different types of patients (Child, Adult, Senior) are handled by different visitors (Diagnosis and Billing). Each type of visitor performs a specific operation based on the type of patient.

## Project Overview

The Hospital Visitor system consists of:

- **Patient Types**: Different types of patients (Child, Adult, Senior) are represented as classes implementing a common `Patient` interface.
- **Visitors**: The `Visitor` interface defines operations to be performed on each patient type. In this example, there are two types of visitors:
  - **DiagnosisVisitor**: Responsible for diagnosing the patient based on age group.
  - **BillingVisitor**: Responsible for calculating the billing based on patient type.
  
This project demonstrates how the Visitor design pattern can help decouple the operations (diagnosis, billing) from the patient classes, making it easier to extend the system without modifying existing patient classes.

## Code Structure

- `Patient` Interface: An abstract class that defines the `accept` method, which allows visitors to perform operations on the patient.
- `ChildPatient`, `AdultPatient`, `SeniorPatient`: Concrete implementations of the `Patient` interface representing different types of patients.
- `Visitor` Interface: An abstract class defining the `visit` methods for each patient type.
- `DiagnosisVisitor` and `BillingVisitor`: Concrete visitor classes that implement the `Visitor` interface to perform operations on different types of patients.

## Example Output
```less
Diagnosing a child patient: Check-up and pediatric care.
Calculating billing for a child patient.
Diagnosing an adult patient: Routine exams and lifestyle advice.
Calculating billing for an adult patient.
Diagnosing a senior patient: Comprehensive geriatric evaluation.
Calculating billing for a senior patient.
```
