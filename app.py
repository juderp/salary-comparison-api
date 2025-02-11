from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the salary data
file_path = "Copy of full_salary_comparison_report.xlsx"
df = pd.read_excel(file_path)

@app.route('/salary', methods=['GET'])
def get_salary():
    role = request.args.get('role', '').strip().lower()
    matching_rows = df[df["Role"].str.lower() == role]

    if matching_rows.empty:
        return jsonify({"error": f"No salary data found for '{role}'"}), 404

    salary_data = {col: int(matching_rows[col].values[0]) for col in df.columns[1:]}
    return jsonify({"role": role, "salaries": salary_data})

if __name__ == '__main__':
    app.run(debug=True)
