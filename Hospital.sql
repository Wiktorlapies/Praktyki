CREATE DATABASE Hospital;

USE Hospital
GO

CREATE TABLE dbo.Specializations (
	ID INT IDENTITY(1,1) NOT NULL,
	SpecName VARCHAR(25) NOT NULL,
	CONSTRAINT PK_Specialization PRIMARY KEY(ID)
);

CREATE TABLE dbo.Deseases (
	ID INT IDENTITY(1,1) NOT NULL,
	DesName VARCHAR(35) NOT NULL,
	CONSTRAINT PK_Deseases PRIMARY KEY(ID)
);

CREATE TABLE dbo.Medicines (
	ID INT IDENTITY(1,1) NOT NULL,
	MedName VARCHAR(40) NOT NULL,
	CONSTRAINT PK_Medicines PRIMARY KEY(ID)
);

CREATE TABLE dbo.Doctors (
	ID INT IDENTITY(1,1) NOT NULL,
	FirstName CHAR NOT NULL,
	LastName CHAR NOT NULL,
	SpecID INT NULL,
	CONSTRAINT PK_Doctors PRIMARY KEY(ID),
	CONSTRAINT FK_DoctorSpecialization FOREIGN KEY (SpecID) REFERENCES dbo.Specializations(ID)
);

CREATE TABLE dbo.Patients (
	ID INT IDENTITY(1,1) NOT NULL,
	FirstName CHAR NOT NULL,
	LastName CHAR NOT NULL,
	Age TINYINT NOT NULL,
	DeseaseID INT NULL,
	PESEL BIGINT NULL,
	CONSTRAINT PK_Patients PRIMARY KEY(ID),
	CONSTRAINT FK_PatientDesease FOREIGN KEY (DeseaseID) REFERENCES dbo.Deseases(ID)
);

CREATE TABLE dbo.Prescriptions (
	ID INT IDENTITY(1,1) NOT NULL,
	PatientID INT NOT NULL,
	MedicineID INT NOT NULL,
	DoctorID INT NOT NULL,
	Dose TINYINT NOT NULL,
	Date DATE NOT NULL,
	ExpirationMM TINYINT NULL,
	CONSTRAINT PK_Prescriptions PRIMARY KEY(ID),
	CONSTRAINT FK_PrescriptionPatient FOREIGN KEY (PatientID) REFERENCES dbo.Patients(ID),
	CONSTRAINT FK_PrescriptionMedicine FOREIGN KEY (MedicineID) REFERENCES dbo.Medicines(ID),
	CONSTRAINT FK_PrescriptionDoctor FOREIGN KEY (DoctorID) REFERENCES dbo.Doctors(ID)
);
