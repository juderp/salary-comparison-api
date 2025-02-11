import pandas as pd

# Load the Excel file
file_path = "Copy of full_salary_comparison_report.xlsx"
df = pd.read_excel(file_path)

# Function to get salaries for a given role
def get_salary(role):
    role = role.lower()
    matching_rows = df[df["Role"].str.lower() == role]

    if matching_rows.empty:
        print(f"Sorry, no salary data found for '{role}'.")
        return

    print(f"\nSalary comparison for '{role}':")
    for col in df.columns[1:]:  # Skip the "Role" column
        print(f"{col}: SGD {matching_rows[col].values[0]}")

# User input loop
while True:
    user_role = input("\nEnter a job role (or type 'exit' to quit): ").strip()
    if user_role.lower() == "exit":
        break
    get_salary(user_role)
