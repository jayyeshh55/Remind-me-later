from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reminders.db'
db = SQLAlchemy(app)

class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text, nullable=False)
    reminder_type = db.Column(db.String(50), nullable=False)

@app.route('/api/create_reminder', methods=['POST'])
def create_reminder():
    data = request.json
    new_reminder = Reminder(date=data['date'], time=data['time'], message=data['message'], reminder_type=data['reminder_type'])
    db.session.add(new_reminder)
    db.session.commit()
    return jsonify({'message': 'Reminder created successfully!'}), 201

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
