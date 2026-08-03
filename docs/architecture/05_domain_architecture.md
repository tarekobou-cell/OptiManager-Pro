# OptiManager Pro

# Domain Architecture

Version : 2.0

Auteur : Mohamed Tarek BOUYAHIAOUI

Architecte : ChatGPT

---

# Vision

Le logiciel est organisé autour des métiers.

Chaque métier est indépendant.

Chaque métier est appelé :

Domain

---

# Domaines

Patient

Clinical

Prescription

Inventory

Workshop

Laboratory

Sales

Accounting

CRM

Administration

Reporting

AI

Cloud

---

# Chaque domaine possède

entities/

value_objects/

repositories/

services/

validators/

events/

commands/

queries/

dto/

exceptions/

tests/

---

# Exemple

domain/

patient/

entities/

Patient.py

PatientIdentity.py

PatientContact.py

PatientMedical.py

PatientInsurance.py

PatientPhoto.py

PatientDocument.py

---

value_objects/

PhoneNumber.py

Email.py

Address.py

NationalId.py

PatientNumber.py

Gender.py

BloodGroup.py

---

repositories/

PatientRepository.py

---

services/

PatientRegistrationService.py

PatientSearchService.py

PatientMergeService.py

PatientHistoryService.py

---

validators/

PatientValidator.py

PhoneValidator.py

EmailValidator.py

---

events/

PatientCreated.py

PatientUpdated.py

PatientArchived.py

---

commands/

CreatePatient.py

UpdatePatient.py

DeletePatient.py

---

queries/

FindPatient.py

SearchPatient.py

PatientStatistics.py

---

dto/

PatientDto.py

PatientSummaryDto.py

PatientDetailsDto.py

---

tests/

test_patient_registration.py

test_patient_search.py

---

Chaque domaine possède exactement cette organisation.

FIN