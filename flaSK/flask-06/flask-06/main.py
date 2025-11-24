from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['secret_key'] = 'synergy'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/theme_05.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

notes = [
    {'topic':'rest api'},
    {'uni':'synergy'}
]

@app.route('/api/get/<int:notes_index>')
def get_tasks(notes_index):
    return notes[notes_index]

@app.route('/api/task', methods=['POST'])
def add_note():
    notes = {'uni':'another institute'}
    notes.append(note)
    return jsonify({'note':note}), 201

@app.route('/api/delete/<int:to_delete>')
def delete_note(to_delete):
    del notes[to_delete]
    return notes

@app.route('/api/put/<int:to_edit>')
def edit_note(to_edit):
    user = db.session.query(User).filter_by(id=id).first()
    data = requests.get_json()
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return user.to_dic(), 201

if __name__ == '__main__':
    app.run(debug=True)