from .models import Todo

def response_serializer(todos: Todo):
    response = []
    for todo in todos:
        todo_dict = {   
            "id": todo.id,
            "name": todo.name,
            "description": todo.description,
            "created_at": str(todo.created_at),
            "completed": todo.completed
        }

        response.append(todo_dict)

    return response