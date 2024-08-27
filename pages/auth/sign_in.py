import flet as ft
from components.models import Database

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



    def content(self):
        last_page = self.page.session.get("last_page")
        return ft.Column(
            controls=[
                ft.Text("This is Page 1"),
                ft.ElevatedButton("Chat", on_click=lambda _: self.pc.load_page("Chat")),
                ft.Text(f"Last Page: {last_page}", selectable=False),
            ]
        )