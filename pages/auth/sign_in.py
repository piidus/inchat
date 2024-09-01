import flet as ft
from components.models import Database, ChatHandler
import time
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
            start_time = time.time()
            chat_handler = ChatHandler()
            for i in range(10000):
                chat_handler.insert_data(message=f" Dummy Message")
                #print(new_chat)
            # Count lengrh of message and time
            total_messages = len(chat_handler.all_chats())
            end_time = time.time()
            total_execution_time = end_time - start_time
            # show a alert
            self.page.snack_bar = ft.SnackBar(ft.Text(f"{total_messages} messages added in {total_execution_time} seconds"))
            self.page.snack_bar.open = True
            self.page.update()

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