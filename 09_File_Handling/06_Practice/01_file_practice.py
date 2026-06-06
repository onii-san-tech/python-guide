"""
Practice: File Handling

Build a simple note-taking application using files.
"""

import json
import os
from datetime import datetime

NOTES_FILE = "notes.json"

def load_notes():
    """Load notes from file, return empty list if file doesn't exist."""
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    return []

def save_notes(notes):
    """Save notes to file."""
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)

def add_note(title, content):
    """Add a new note."""
    notes = load_notes()
    note = {
        "id": len(notes) + 1,
        "title": title,
        "content": content,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    notes.append(note)
    save_notes(notes)
    print(f"Note '{title}' added!")

def list_notes():
    """Display all notes."""
    notes = load_notes()
    if not notes:
        print("No notes yet!")
        return
    for note in notes:
        print(f"\n[{note['id']}] {note['title']} — {note['created']}")
        print(f"     {note['content']}")

# Demo usage
add_note("Python Tips", "Use list comprehensions for cleaner code!")
add_note("Daily Task", "Study file handling chapter.")
list_notes()

# Clean up
if os.path.exists(NOTES_FILE):
    os.remove(NOTES_FILE)
