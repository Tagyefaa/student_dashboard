-- Task 1: UniversityDB table + GetStudentResult stored procedure
IF DB_ID('UniversityDB') IS NULL CREATE DATABASE UniversityDB;
GO
USE UniversityDB;
GO

IF OBJECT_ID('dbo.Students') IS NULL
CREATE TABLE dbo.Students (
    StudentId INT IDENTITY(1,1) PRIMARY KEY,
    Name      NVARCHAR(100) NOT NULL,
    Score     INT NOT NULL CHECK (Score BETWEEN 0 AND 100)
);
GO

IF NOT EXISTS (SELECT 1 FROM dbo.Students)
INSERT INTO dbo.Students (Name, Score)
VALUES (N'Ali', 85), (N'Leyla', 72), (N'Murad', 48), (N'Aysel', 91), (N'Kamran', 63);
GO

CREATE OR ALTER PROCEDURE dbo.GetStudentResult
    @StudentName NVARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        Name,
        Score,
        CASE
            WHEN Score >= 90 THEN 'A'
            WHEN Score >= 80 THEN 'B'
            WHEN Score >= 70 THEN 'C'
            WHEN Score >= 60 THEN 'D'
            ELSE 'F'
        END AS Grade
    FROM dbo.Students
    WHERE Name LIKE '%' + @StudentName + '%';
END
GO

-- Test:
-- EXEC dbo.GetStudentResult @StudentName = N'Ali';
