#----Project Title: Processing, error and file handling of employee salary data using Python----------
# -------------------------------------------------------------------------------------------------------
# Note: The actual script run starts from line 32 of this python notebook.

# Created by:  Victor Kadiri
# Date Created: 15th March 2025

# Purpose: This python script is created to perform data processing, error and file handling procedures using Python. The script utilizes series of function, libraries and syntax to address its objectives.

# Desired Output: The final output will be saved into physical csv file "employee_details.csv" and zipped file "employee_profile.zip"

# Datasets used: Salary data which contains salaries for San Francisco employee from 2011 - 2018 was used to perform this analysis. Data Source: https://www.kaggle.com/code/itshorus/sf-salary

# Scripts Required: 
# a. Salary_function_Python.py

# Tools and Installations Required:
# 1. Download and Install VS Code 
# 2. Download and Install Python 3.12.9 or higher

# Procedures Performed:
# 1: Launch the VS Code application
# 2: Create three folders( i. "input", "output", "scripts") in your desired location 
# 3: Download the salary data from the data source into the "input" folder
# 4: Download the script source file (a.Salary_Function_Python.py) from the GIT repos into the "script" folder
# 5: Locate and open the script source file (a.Salary_Function_Python.py) using VS code
# 6: Update input and output file paths to your desired location.
# 7: Locate and Click the "Run" button on the script file (a.Salary_Function_Python.py)
# 8: View the outputs on the terminal panes or locate the results in the output folder on your PC.
#--------------------------------------------------------------------------------------------------------

# ----------------------- The Actual Analysis Begins Here -----------------------------------------------
#Step 1: This step import the required libraries and functions required for this analysis
import os
import pandas as pd
import zipfile

# Step 2: Defining the file paths: This step is important - Please ensure you update accordingly

# Define the input path
# Set your input folder path (Remember to Change this to your desired input folder path)
input_folder_path = r"C:\Users\User\Downloads\BAN6420\Assignment_2\Salary_Data_Processing_VK\input"
# The script below creates this input folder path if it does not exist on your PC. This will prevent an error from occuring.
os.makedirs(input_folder_path, exist_ok=True)
# This line of code defines the input file path
input_file_path = os.path.join(input_folder_path, "Total.csv")

# Define the output paths
# Set your output folder path (Remember to Change this to your desired output folder path)
output_folder_path = r"C:\Users\User\Downloads\BAN6420\Assignment_2\Salary_Data_Processing_VK\output"
# The script below creates this output folder path if it does not exist on your PC. This will prevent an error from occuring.
os.makedirs(output_folder_path, exist_ok=True)
# This line of code defines the output file paths
output_file_path_1 = os.path.join(output_folder_path, "employee_details.csv")
output_file_path_2 = os.path.join(output_folder_path, "employee_profile.zip")

# Step 3: This step imports the salary data into the notebook environment.
salary_df = pd.read_csv(input_file_path)

#View the first few rows of the imported data.
print(salary_df.head(7))

#Step 4: This step creates an employee function that accepts an employees's name as an input and return their details. It also performs an error handling procedures.

# Below is a function use to retrieve employee details from a dataframe containing the employee data
def get_employee_details(name, data):

# This line of code uses a try block to handle potential errors during processing.    
    try:
#This line of code searches from a match for employee name on the dataframe and uses a squeeze function to convert it to a series.
        employee_details = data[data['EmployeeName'] == name].squeeze()
# The below line of code addresses a case where no employee record was found and return a message.
        if employee_details.empty:
            return f"No employee found with the name: {name}"
# If an employee record is found, then the details is returned.
        return employee_details
#The final set of codes helps to handle any exceptions that may occur during processing.
    except Exception as e:
        return f"An error occurred: {e}"
    
#Test Scenarios for the created function- Feel free to explore.
# Scenario 1: Employee record was found in the salary data
print("Scenario 1: Employee found")
print(get_employee_details("NATHANIEL FORD", salary_df))  

# Scenario 2: No employee record found in the salary data
print("\nScenario 2: Employee not found")
print(get_employee_details("Victor Kadiri", salary_df))

# Scenario 3: Error handling message
print("\nScenario 3: Invalid name input")
print(get_employee_details(123, salary_df))


# Step 5: This step processes the employee salary data using a python dictionary. 

# This line of code converts the DataFrame to a dictionary
salary_dict = salary_df.set_index('EmployeeName')['TotalPay'].to_dict()

# This line of code provides a view of the dictionary
print(salary_dict)


# Step 6: This step exports an employee details as csv and as a zip folder including error and file handling

# a. csv export
# This converts the sample employee details dictionary to a dataframe
employee_details_df = pd.DataFrame(get_employee_details("NATHANIEL FORD", salary_df))  
try:
# This code exports the employee detail for one employee and checks for file and permissions error
    try:
# This code saves the DataFrame to a CSV file
        employee_details_df.to_csv(output_file_path_1, index=False)
        print(f"Employee details have been exported to '{output_file_path_1}'.")
# This code raises an exception if read/write permission is not allowed within the target folder and stops further execution
    except PermissionError:
        print(f"Error: Permission denied. Cannot write to '{output_file_path_1}'.")
        raise  
# This code raises an exception if the files fails to export to the target folder and stops further execution  
    except Exception as e:
        print(f"Error: Failed to export CSV file. Reason: {e}")
        raise 

 # b. Zip export
    try:

#This code creates a zip file and adds the CSV file to it
        with zipfile.ZipFile(output_file_path_2, 'w') as zipf:
            zipf.write(output_file_path_1, arcname=os.path.basename(output_file_path_1))

        print(f"CSV file '{output_file_path_1}' has been zipped to '{output_file_path_2}'.")
# This code raises an exception if the file is not found and stops further execution
    except FileNotFoundError:
        print(f"Error: CSV file '{output_file_path_1}' not found. Cannot create ZIP file.")
# This code raises an exception if read/write permission is not allowed within the target folder and stops further execution
    except PermissionError:
        print(f"Error: Permission denied. Cannot write to '{output_file_path_2}'.")
# This code raises an exception if the files fails to export to the target folder and stops further execution  
    except Exception as e:
        print(f"Error: Failed to create ZIP file. Reason: {e}")
#The final set of code helps to handle any exceptions that may occur during processing.
except Exception as e:
    print(f"An unexpected error occurred during the process: {e}")


