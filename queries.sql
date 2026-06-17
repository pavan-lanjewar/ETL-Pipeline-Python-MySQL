SELECT * FROM sales;

SELECT SUM(Amount) AS TotalSales
FROM sales;

SELECT City,
SUM(Amount) AS CitySales
FROM sales
GROUP BY City;

SELECT Product,
AVG(Amount) AS AveragePrice
FROM sales
GROUP BY Product; 