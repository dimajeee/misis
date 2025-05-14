from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select
from flask import Flask, request, jsonify
import jwt
from functools import wraps


DATABASE_URL = "sqlite:///example.db"

engine = create_engine(DATABASE_URL, echo=True)

metadata = MetaData()


users = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer)
)


metadata.create_all(engine)


def get_all_users():
    stmt = select(users)

    with engine.connect() as conn:
        result = conn.execute(stmt)
        return [dict(row) for row in result]


app = Flask(__name__)
SECRET_KEY = "qwerty"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            parts = auth_header.split()
            if len(parts) == 2 and parts[0] == 'Bearer':
                token = parts[1]
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = data['user']
        except Exception as e:
            return jsonify({'message': 'Token is invalid!', 'error': str(e)}), 401
        return f(current_user, *args, **kwargs)
    return decorated


@app.route('/users', methods=['GET'])
@token_required
def users_route(current_user):
    users_list = get_all_users()
    return jsonify({'current_user': current_user, 'users': users_list})


if __name__ == '__main__':
    app.run(debug=True)
