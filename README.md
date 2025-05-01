Loading Public API Data into MySQL using PySpark
Objective:
To automate the process of extracting structured vehicle model data from a free public API and loading it into a local MySQL database using PySpark for further analysis or integration.
Description:
In this use case, I consumed vehicle model data from the National Highway Traffic Safety Administration (NHTSA) public API:
👉 https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/*?format=json
Using Python and PySpark, I performed the following steps:
	1. API Integration (Python requests) – Connected to the API and fetched vehicle model data for a specific car manufacturer (e.g., Honda, Toyota).
	2. Data Processing (PySpark) – Parsed the JSON response into a PySpark DataFrame and defined the schema to structure the data.
	3. Data Loading (PySpark JDBC) – Wrote the DataFrame into a MySQL Workbench database running on my local desktop using JDBC.
Tools & Technologies Used:
	• Python 3.x
	• PySpark 3.5.x
	• MySQL Workbench (local)
	• MySQL JDBC Connector
	• Public REST API (VPIC NHTSA)
Business Relevance:
This pipeline simulates a real-world data ingestion workflow where structured data from external sources (APIs) is regularly imported into internal systems (like MySQL) for reporting, analytics, or further ETL processing.

Technical information:

API Json schema 
{
  "type": "object",
  "properties": {
    "Count": { "type": "integer" },
    "Message": { "type": "string" },
    "SearchCriteria": { "type": "string" },
    "Results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Make_ID": { "type": "integer" },
          "Make_Name": { "type": "string" },
          "Model_ID": { "type": "integer" },
          "Model_Name": { "type": "string" }
        },
        "required": ["Make_ID", "Make_Name", "Model_ID", "Model_Name"]
      }
    }
  },
  "required": ["Count", "Message", "Results"]
}

MySQL table structure "vehicle_details";
Field	Type	Null	Key	Default	Extra
Make_ID	bigint	YES		NULL	
Make_Name	longtext	YES		NULL	
Model_ID	bigint	YES		NULL	
Model_Name	longtext	YES		NULL	

Unit testing:
	Steps	commands
	Source free API	United States Department of Transportation free RESTAPI for data as below,
		
		https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/*?format=csv
		
		
		
		We have 30345 records from the source API
		
		
	Before look of vehicle details table in MYSQL	
		
	Pyspark code execution	Step 1: First fetch form the free Api is successful 
		
		
		Step 2:  loading into table is also successful 
		
		
	After look of vehicle details table in MYSQL	
		
		
		
		
![image](https://github.com/user-attachments/assets/38cd95e7-f458-48c4-9835-eb60a2134970)
# 2_readapi_loadtable
