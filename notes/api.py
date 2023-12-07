from ninja import NinjaAPI
from .models import *
from .schema import *
from typing import List
from django.shortcuts import get_object_or_404
api = NinjaAPI()

@api.post("/notes")
def create_note(request, payload: NotesIn):
    note = Notes.objects.create(**payload.dict())
    return {"id": note.id}

@api.get("/notes/{note_id}", response=NotesOut)
def get_note(request, note_id: int):
    note = get_object_or_404(Notes, id=note_id)
    return NotesOut(id=note.id, title=note.title, body=note.body)

@api.get("/notes", response=List[NotesOut])
def list_notes(request):
    notes = Notes.objects.all()
    return [NotesOut(id=note.id, title=note.title, body=note.body) for note in notes]

@api.put("/notes/{note_id}")
def update_note(request, note_id: int, payload: NotesIn):
    note = get_object_or_404(Notes, id=note_id)
    for attr, value in payload.dict().items():
        setattr(note, attr, value)
    note.save()
    return {"success": True}

@api.delete("/notes/{note_id}")
def delete_note(request, note_id: int):
    note = get_object_or_404(Notes, id=note_id)
    note.delete()
    return {"success": True}
