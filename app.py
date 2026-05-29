from flask import Flask, request, jsonify
app = Flask(__name__)
tickets = []
class Ticket:
    def __init__(self, ticket_id, issue, priority):
        self.ticket_id = ticket_id
        self.issue = issue
        self.priority = priority
        self.status = "OPEN"
@app.route('/')
def home():
    return "Telcom Ticket Managemenet System Running"
@app.route('/create', methods=['POST'])
def create_ticket():
    data = request.json
    ticket = Ticket(
        data['ticket_id'],
        data['issue'],
        data['priority']
    )
    tickets.append(ticket.__dict__)
    return jsonify({
        "message": "Ticket Created",
        "ticket": ticket.__dict__
    })
@app.route('/tickets')
def get_tickets():
    return jsonify(tickets)
@app.route('/high')
def high_priority():
    high = [
        t for t in tickets
        if t['priority'] == 'HIGH'
    ]

    return jsonify(high)
@app.route('/update/<ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    for ticket in tickets:
        if ticket['ticket_id'] == ticket_id:
           ticket['status'] = "RESOLVED"
           return jsonify({
               "message": "Ticket Updated",
               "ticket": ticket
           })

    return jsonify({
        "message": "Ticket Not Found"
     })
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001
)
