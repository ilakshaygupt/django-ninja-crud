from datetime import date
from ninja import Schema

class NotesIn(Schema):
    title: str
    body: str

class NotesOut(Schema):
    id:int
    title: str
    body: str
from datetime import date
from ninja import Schema

class EmployeeIn(Schema):
    first_name: str
    last_name: str
    department_id: int = None
    birthdate: date = None

class EmployeeOut(Schema):
    id: int
    first_name: str
    last_name: str
    department_id: int = None
    birthdate: date = None
