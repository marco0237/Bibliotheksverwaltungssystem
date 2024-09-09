
from member import Member

import sqlite3
import random
from tkinter import messagebox


class MainController:

    def __init__(self) -> None:

        # Create a database or connect to an existing one
        self.conn = sqlite3.connect("testGhis.db")
        self.cursor = self.conn.cursor()

        # Create a table if it doesn't exist
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS members (id INTEGER PRIMARY KEY,  name TEXT, member_id INTEGER)''')
        self.conn.commit()

        # Fake 1000 members
        listOfMemberIds = [
            random.randint(
                1, 900000) for p in range(
                0, 10000)]  # List comprehension
        for id in listOfMemberIds:
            member = Member(f"Name Nr . {id}", id)
            self.addMember(member)

      # self.cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    def addMember(self, member: Member) -> None:
        if member:
            self.cursor.execute(
                """INSERT INTO members (name,  member_id) VALUES (?,?)""", (member.name, member.member_id, ))
            self.conn.commit()
        else:
            messagebox.showwarning("Warning", "Please input a task.")

    def loadMember(self) -> list[Member]:

        self.cursor.execute("SELECT * FROM members")
        members = self.cursor.fetchall()
        return members

    def deleteMember(self, selectedmemeber: Member):

        if selectedmemeber:
            self.cursor.execute(
                "DELETE FROM tasks WHERE memeber=?", (selectedmemeber,))
            self.conn.commit()
        else:
            messagebox.showwarning(
                "Warning", "Please select a task to delete.")
