#!/usr/bin/env python
# coding: utf-8

"""
Script: fetch_vehicle_models.py
Description: Fetches vehicle model data from the NHTSA API,
             converts it to a PySpark DataFrame,
             and writes it into a MySQL database using JDBC.
Author: Your Name
"""

import requests
from pyspark.sql import SparkSession

# Initialize SparkSession with MySQL JDBC connector
spark = (
    SparkSession.builder
    .appName("MySQLConnection")
    .config(
        "spark.jars",
        r"D:\Inceptez\software\mysql-connector-java-8.0.21\mysql-connector-java-8.0.21.jar"  # Path to MySQL JDBC driver
    )
    .getOrCreate()
)

# Step 1: Fetch vehicle models data from NHTSA API
response = requests.get("https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/honda?format=json")  # Replace * with a real make
data = response.json()

# Step 2: Extract the 'Results' list from the response
results = data['Results']

# Step 3: Convert the API results into a Spark DataFrame
df = spark.createDataFrame(results)

# Show the DataFrame content
df.show(truncate=False)

# Step 4: Define MySQL JDBC connection parameters
url = "jdbc:mysql://localhost:3306/mypysparkdb"  # Replace with your DB details
table = "vehicle_details"
properties = {
    "user": "root",         # MySQL username
    "password": "root",     # MySQL password
    "driver": "com.mysql.cj.jdbc.Driver"
}

# Step 5: Write the DataFrame into MySQL table (overwrite mode)
df.write.jdbc(url=url, table=table, mode="overwrite", properties=properties)

# Step 6: Read back the data from MySQL to confirm
df = spark.read.jdbc(url=url, table=table, properties=properties)

# Show the data read from MySQL
df.show()