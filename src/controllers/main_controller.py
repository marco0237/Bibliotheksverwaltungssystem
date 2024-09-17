

import asyncio
import sqlite3

from tkinter import messagebox

from time import time

from typing import List

from faker import Faker

from models.member import Member


class MainController:

    def __init__(self) -> None:

        # Create a database or connect to an existing one
        self.conn = sqlite3.connect("libraryDB.db")
        self.cursor = self.conn.cursor()

        # Drop Table if exists
        self.cursor.execute(
            '''DROP TABLE IF  EXISTS members''')
        self.conn.commit()

        # Create a table if it doesn't exist
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS members (id INTEGER PRIMARY KEY,  name TEXT, member_id INTEGER)''')
        self.conn.commit()

        # record start time
        time_start = time()

        # Fake 5000 members
        # self.create_fake_data(5000)
        asyncio.run(self.create_fake_data_async(50))
        # record end time
        time_end = time()
        # calculate the duration
        time_duration = time_end - time_start
        print(f"#########################  {time_duration}")

    # self.cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))

    def add_member(self, member: Member) -> None:
        if member:
            self.cursor.execute(
                """INSERT INTO members (name,  member_id) VALUES (?,?)""", (member.name, member.member_id, ))
            self.conn.commit()
        else:
            messagebox.showwarning("Warning", "Please input a task.")

    def load_members(self) -> List[Member]:

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

    async def create_fake_data_async(self, number_of_members=1000):
        await asyncio.create_task(self.__async_fake_data__(number_of_members))

    def create_fake_data(self, number_of_members=1000):
        """TODO: Better use pip install Faker (https://faker.readthedocs.io/en/master/index.html) """
        faker = Faker('fr_FR')
        for member_id in range(number_of_members):
            member = Member(f"{faker.name()}", member_id)
            self.add_member(member)

    async def __async_fake_data__(self, number_of_members=1000):
        self.create_fake_data(number_of_members)
