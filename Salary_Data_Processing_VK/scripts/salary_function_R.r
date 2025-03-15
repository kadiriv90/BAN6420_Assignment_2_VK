#----Project Title: Processing, error and file handling of employee salary data using R--------
# -------------------------------------------------------------------------------------------------------
# Note: The actual script run starts from line 32 of this R notebook.

# Created by:  Victor Kadiri
# Date Created: 15th March 2025

# Purpose: This R script is created to perform data processing, error and file handling procedures using R. The script utilizes series of function, libraries and syntax to address its objectives.

# Desired Output: The final output will be saved into physical csv file "employee_details_r.csv" and unzipped file "employee_profile_r.zip"

# Datasets used: Salary data which contains salaries for San Francisco employee from 2011 - 2018 was used to perform this analysis. Data Source: https://www.kaggle.com/code/itshorus/sf-salary

# Scripts Required: 
# a. Salary_function_R.py

# Tools and Installations Required:
# 1. Download and Install VS Code 
# 2. Download and Install R 4.3.0 or higher

# Procedures Performed:
# 1: Launch the VS Code application
# 2: Download the script source file (a.Salary_Function_R.py) from the GIT repos into the "script" folder
# 3: Locate and open the script source file (a.Salary_Function_R.py) using VS code
# 4: Update output file path to your desired location.
# 5: Locate and Click the "Run" button on the script file (a.Salary_Function_R.py)
# 6: View the outputs on the terminal panes or locate the results in the output folder on your PC.
#--------------------------------------------------------------------------------------------------------

# Step 1: Load required libraries
# No external libraries are required for this R script.

# Step 2: This step is important - Please action the below:
# Set your output folder path (Remember to Change this to your desired output folder path)

# Step 2: Set your output folder path (Change this to your same output folder path used in the python code)
output_folder_path <- "C:/Users/User/Downloads/BAN6420/Assignment_2/Salary_Data_Processing_VK/output"

# This code checks if the the output folder exists and creates one if it does not
if (!dir.exists(output_folder_path)) {
  dir.create(output_folder_path, recursive = TRUE)
  print(paste("Output folder created at:", output_folder_path))
} else {
  print(paste("Output folder already exists at:", output_folder_path))
}

# This line of code defines the output file path where the python exported Zip file is located 
output_file_path_2 <- file.path(output_folder_path, "employee_profile.zip")


# Step 3: This steps of code unzips the file to the output folder location defined above

# This line of code uses a tryCatch block to handle potential errors during processing.
tryCatch({

# This line of codes unzips the file to the specified output folder
  unzip(output_file_path_2, exdir = output_folder_path)
  print(paste("Employee details zip file has been unzipped to:", output_folder_path))

#Step 4: This step finds the CSV file in the unzipped folder and displays it

# This line of code finds the csv file in the folder
  csv_files <- list.files(output_folder_path, pattern = "\\.csv$", full.names = TRUE)

# This line of code handles errors by returning a "No csv file" message if no csv file is found in the folder and stops further execution.
  if (length(csv_files) == 0) {
    stop("No CSV file found in the unzipped folder.")
  }

# Step 5: These lines of code reads the csv file saves it as "employee_details_r dataframe and displays the CSV file 
  csv_file_path <- csv_files[1] 
  employee_details_r <- read.csv(csv_file_path)

 # View the csv file
  print("Data from the CSV file:")
  print(employee_details_r)


# Step 6: This final code export the employee_details_r output to a CSV file and handle errors that may affect the accuracy and completeness of the file processing.

  output_csv_path <- file.path(output_folder_path, "employee_details_r.csv")
  write.csv(employee_details_r, output_csv_path, row.names = FALSE)
# This code display a message upon successful export
  print(paste("Final output saved to:", output_csv_path))

# This code raises an exception if the files fails to export to the target folder and stops further execution  
}, error = function(e) {

# The final set of code helps to handle any exceptions that may occur during processing.
  print(paste("An error occurred:", e$message))
}, warning = function(w) {

# The final set of code helps to handle any warnings that may occur during processing.
  print(paste("A warning occurred:", w$message))
})