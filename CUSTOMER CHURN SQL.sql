CREATE DATABASE CHURN_ANALYSIS;
USE CHURN_ANALYSIS;
SHOW TABLES;
SELECT COUNT(*)FROM `Telco Raw Data Set`;

# CHURNED CUSTOMERS 
SELECT COUNT(*) AS Churned_Customers FROM `Telco Raw Data Set`WHERE Churn = 'Yes';

# CHURN RATE 
SELECT
ROUND(
(COUNT(CASE WHEN Churn='Yes' THEN 1 END)*100.0)
/COUNT(*),2
) AS Churn_Rate
FROM `Telco Raw Data Set`;

# CHURN BY CONTRACT TYPE 
SELECT
Contract,
COUNT(*) AS Churn_Count
FROM `Telco Raw Data Set`
WHERE Churn='Yes'
GROUP BY Contract
ORDER BY Churn_Count DESC;

#CHURN BY INTERNET SERVICE 
SELECT
InternetService,
COUNT(*) AS Churn_Count
FROM `Telco Raw Data Set`
WHERE Churn='Yes'
GROUP BY InternetService
ORDER BY Churn_Count DESC;

#CHURN BY PAYMENT METHOD 
SELECT
PaymentMethod,
COUNT(*) AS Churn_Count
FROM `Telco Raw Data Set`
WHERE Churn='Yes'
GROUP BY PaymentMethod
ORDER BY Churn_Count DESC;

#

