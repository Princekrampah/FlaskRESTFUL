from api_application import api, db
from flask_restful import Resource, reqparse
from api_application.models import Todo
from datetime import datetime
from .serializer import response_serializer


parser = reqparse.RequestParser()
parser.add_argument("name")
parser.add_argument("description")
parser.add_argument("created_at")
parser.add_argument("completed")

class Todos(Resource):
    def get(self):
        todos = Todo.query.all()
        response = response_serializer(todos)  
        return response, 200

    def post(self):
        data = parser.parse_args()
        data["created_at"] = str(datetime.strptime(data["created_at"] ,"%d/%m/%y"))
        data["completed"] = bool(data["completed"])
        new_data = Todo(**data)
        db.session.add(new_data)
        db.session.commit()
        return data, 201


class TodosId(Resource):

    def get(self, id):
        todo = Todo.query.get(int(id))

        if todo:
            response = response_serializer([todo])
            return response, 200
        else:
            return {"msg": "Not Found"}, 404


    def put(self, id):
        data = parser.parse_args()
        data["created_at"] = datetime.strptime(data["created_at"] ,"%d/%m/%y")
        data["completed"] = bool(data["completed"])

        try:
            todo = Todo.query.get(int(id))

            if todo:
                todo.name = data.get("name")
                todo.description = data.get("description")
                todo.created_at = data.get("created_at")
                todo.completed = data.get("completed")

                db.session.commit()
                response = response_serializer([todo])
                return response, 200
            else:
                return {"msg": "Not Found"}, 404
        except:
            return {"msg": "Invalid data, make sure name of todo is unique"}


    def delete(self, id):
        todo = Todo.query.get(int(id))

        if todo:
            db.session.delete(todo)
            db.session.commit()
            return {"msg": "Todo Deleted"}, 200
        else:
            return {"msg": "Not Found"}, 404
    



api.add_resource(Todos, "/todos")
api.add_resource(TodosId, "/todos/<int:id>")


