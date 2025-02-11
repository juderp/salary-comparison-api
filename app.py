from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__, template_folder='templates')

# ✅ Fix Homepage Route to Serve HTML Instead of JSON
@app.route('/')
def home():
    return render_template('index.html')  # This should return the HTML page

# ✅ Salary API Route
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
