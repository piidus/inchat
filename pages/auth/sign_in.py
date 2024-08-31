import flet as ft
from components.models import Database, ChatHandler
import os
# @memory_test
class Login(ft.Control):
    def __init__(self, page: ft.Page, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.pc = pc

    def did_mount(self):
        # first check datebase present or not, if not create one
        try:
            db = Database()
            db.create_table(sql=
                '''
                CREATE TABLE IF NOT EXISTS chats (
                    id INTEGER PRIMARY KEY,
                    name TEXT(30),
                    message TEXT(150),
                    time TEXT(30)
                    );
                '''
            )
        except Exception as e:
            print(e)
        self.page.session.set("last_page", "Page1")
        print('did mount page 1')
        self.page.update()


    def dummy_50_messages(self,e):
        try:
            chat_handler = ChatHandler()
            for i in range(50):
                chat_handler.insert_data(message=f" Dummy Message {i}")
                    # print(new_chat)
        except Exception as e:
            print(e)

    def content(self):
        last_page = self.page.session.get("last_page")
        return ft.Column(
            controls=[
                ft.Text("This is Page 1"),
                ft.ElevatedButton("Add Dummy Messages", on_click=self.dummy_50_messages),
                ft.Text(f"Last Page: {last_page}", selectable=False),
            ]
        )