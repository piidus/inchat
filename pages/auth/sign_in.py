import flet as ft
# from components.memory_usage import memory_test

# @memory_test
class Login(ft.Control):
    def __init__(self, page: ft.Page, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.pc = pc

    def did_mount(self):
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
