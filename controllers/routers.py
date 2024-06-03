from fastapi import APIRouter
from ariadne.asgi import GraphQL
from ariadne import QueryType, MutationType, make_executable_schema, load_schema_from_path
from models.model import User
from database.database import SessionLocal

type_defs = load_schema_from_path("database/schema.graphql")

# Định nghĩa truy vấn
query = QueryType()

@query.field("user")
def resolve_user(_, info, id):
    session = SessionLocal()
    return session.query(User).filter(User.id == id).first()

@query.field("allUsers")
def resolve_all_users(_, info):
    session = SessionLocal()
    return session.query(User).all()

# Định nghĩa thay đổi 
mutation = MutationType()

@mutation.field("createUser")
def resolve_create_user(_, info, user_data):
    session = SessionLocal()
    user = User(**user_data)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@mutation.field("updateUser")
def resolve_update_user(_, info, id, user_data):
    session = SessionLocal()
    user = session.query(User).filter(User.id == id).first()
    if user:
        for key, value in user_data.items():
            setattr(user, key, value)
        session.commit()
        session.refresh(user) 
        return user
    return  {"success": False, "message": "Người dùng không tồn tại !"}


@mutation.field("deleteUser")
def resolve_delete_user(_, info, id):
    session = SessionLocal()
    user = session.query(User).filter(User.id == id).first()
    if user:
        session.delete(user)
        session.commit()
        return {"success": True, "message": "Xóa người dùng thành công!"}
    return {"success": False, "message": "Người dùng không tồn tại !"}

# Tạo executable schema
schema = make_executable_schema(type_defs, query, mutation)

router = APIRouter()

graphql_app = GraphQL(schema, debug=True)
router.add_route("/graphql", graphql_app)
router.add_websocket_route("/graphql", graphql_app)
