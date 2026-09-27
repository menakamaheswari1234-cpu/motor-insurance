from flask import Flask, jsonify, request

app = Flask(__name__)

policies = [
    {
        "policy_id": "POL1001",
        "customer_name": "Rahull",
        "vehicle_number": "KA01AB1234",
        "vehicle_type": "Car",
        "status": "ACTIVE"
    }
]


@app.route("/")
def home():
    return jsonify({
        "application": "Motor Insurance Platform",
        "service": "Policy Service",
        "status": "UP"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/policies", methods=["GET"])
def get_policies():
    return jsonify(policies)


@app.route("/policies/<policy_id>", methods=["GET"])
def get_policy(policy_id):

    for policy in policies:
        if policy["policy_id"] == policy_id:
            return jsonify(policy)

    return jsonify({
        "message": "Policy not found"
    }), 404


@app.route("/policies", methods=["POST"])
def create_policy():

    data = request.get_json()

    policy = {
        "policy_id": data["policy_id"],
        "customer_name": data["customer_name"],
        "vehicle_number": data["vehicle_number"],
        "vehicle_type": data["vehicle_type"],
        "status": "ACTIVE"
    }

    policies.append(policy)

    return jsonify(policy), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
