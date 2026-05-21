from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/validate', methods=['POST'])
def validate():
    data = request.json

    request_type = data.get("request_type")
    input_data = data.get("input_data")

    if not request_type or not input_data:
        return jsonify({
            "status": "invalid",
            "message": "Missing required information"
        })

    unsafe_terms = ["<script>", "</script>", "DROP TABLE", "DELETE FROM"]

    for term in unsafe_terms:
        if term.lower() in input_data.lower():
            return jsonify({
                "status": "invalid",
                "message": "Unsafe input detected"
            })

    return jsonify({
        "status": "valid",
        "message": "Input accepted"
    })

if __name__ == "__main__":
    app.run(port=5002)
