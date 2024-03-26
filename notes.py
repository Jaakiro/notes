import json
import argparse
import notes

with open('notes.json', 'w') as file:
    json.dump(notes, file)


class Note:
    def __init__(self, id, title, message):
        self.id = id
        self.title = title
        self.message = message

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "message": self.message
        }


def add_note(notes, title, message):
    notes.append(Note(len(notes) + 1, title, message))


def read_notes(notes, filter_by_date=None):
    if filter_by_date:
        notes = [note for note in notes if note.created_at.strftime('%d.%m.%Y') == filter_by_date]
    for note in notes:
        print(note.to_dict())


def save_notes(notes, file_path):
    with open(file_path, 'w') as file:
        json.dump(notes, file)


def load_notes(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def delete_note(notes, note_id):
    notes = [note for note in notes if note.id != note_id]


def edit_note(notes, note_id, title, message):
    for note in notes:
        if note.id == note_id:
            note.title = title
            note.message = message
            break


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', type=str)
    parser.add_argument('--title', type=str)
    parser.add_argument('--message', type=str)
    parser.add_argument('--filter_by_date', type=str)
    parser.add_argument('--delete', type=int)
    parser.add_argument('--edit', type=int)
    parser.add_argument('--title_edit', type=str)
    parser.add_argument('--message_edit', type=str)
    args = parser.parse_args()

    notes = load_notes('notes.json') or []

    if args.command == 'add':
        add_note(notes, args.title, args.message)
        save_notes(notes, 'notes.json')
    elif args.command == 'read':
        read_notes(notes)
    elif args.command == 'delete':
        delete_note(notes, args.delete)
        save_notes(notes, 'notes.json')
    elif args.command == 'edit':
        edit_note(notes, args.edit, args.title_edit, args.message_edit)
        save_notes(notes, 'notes.json')
    else:
        print('Invalid command')


if __name__ == '__main__':
    main()


