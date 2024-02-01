class Patient:
    def __init__(self, patient_id, name, age, gender, contact) -> None:
        self.__patient_id = patient_id
        self.__age = age
        self.__name = name
        self.__gender = gender
        self.__contact = contact

    def get_patientInfo(self):
        return {
            "PatientID": self.__patient_id,
            "Name": self.__name,
            "Age": self.__age,
            "Gender": self.__gender,
            "Contact": self.__contact
        }


class Doctor:
    def __init__(self, doc_id, name, specialisation) -> None:
        self.__doc_id = doc_id
        self.__name = name
        self.__specialisation = specialisation

    def get_doctorInfo(self):
        return {
            "Doctor ID": self.__doc_id,
            "Name": self.__name,
            "Specialisation": self.__specialisation
        }


class Medical_Records:
    def __init__(self) -> None:
        self.__records = {}

    def add_records(self, p, d, disease, medication):
        self.__records[p.get_patientInfo()["PatientID"]] = {"Patient": p.get_patientInfo(),
                                                            "Doctor": d.get_doctorInfo(),
                                                            "Disease": disease,
                                                            "Medication": medication}

    def get_record(self):
        return self.__records


# Driver Code
patient1 = Patient(1, "Ravi", 23, "Male", "+91 7837764328")
patient2 = Patient(2, "Saket", 27, "Male", "+91 9989674123")
patient3 = Patient(3, "Rakesh", 54, "Male", "+91 9785413652")
doctor1 = Doctor(1, "Rotalk", "Cardiologist")
doctor2 = Doctor(2, "Atring", "Radiologist")

record = Medical_Records()
record.add_records(patient1, doctor1, "Heart Problem", "Aspirin")
print(record.get_record())

patient_name = input("Enter Patient Name: ")
if patient_name == "Ravi":
    for x, y in record.get_record().items():
        print(record.get_medical_record()[x][y][y["PatientID"]])
elif patient_name == "Saket":
    for x, y in record.get_record().items():
        print(record.get_medical_record()[x][y][y["PatientID"]])
