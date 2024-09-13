

import sqlite3
import random
from tkinter import messagebox

from typing import List

from models.member import Member


class MainController:

    def __init__(self) -> None:

        # Create a database or connect to an existing one
        self.conn = sqlite3.connect("libraryDB.db")
        self.cursor = self.conn.cursor()

        # Create a table if it doesn't exist
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS members (id INTEGER PRIMARY KEY,  name TEXT, member_id INTEGER)''')
        self.conn.commit()

        # Fake 1000 members
        list_of_member_ids = [
            random.randint(
                1, 900000) for _ in range(
                0, 1000)]  # List comprehension
        for member_id in list_of_member_ids:
            member = Member(f"Name Nr . {member_id}", member_id)
            self.add_member(member)

    # self.cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    def add_member(self, member: Member) -> None:
        if member:
            self.cursor.execute(
                """INSERT INTO members (name,  member_id) VALUES (?,?)""", (member.name, member.member_id, ))
            self.conn.commit()
        else:
            messagebox.showwarning("Warning", "Please input a task.")

    def load_member(self) -> List[Member]:

        self.cursor.execute("SELECT * FROM members")
        members = self.cursor.fetchall()
        return members

    def delete_member(self, selected_member: Member):

        if selected_member:
            self.cursor.execute(
                "DELETE FROM tasks WHERE member=?", (selected_member,))
            self.conn.commit()
        else:
            messagebox.showwarning(
                "Warning", "Please select a task to delete.")
