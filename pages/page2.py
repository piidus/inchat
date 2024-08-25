import flet as ft
# from components import memory_profiler
class Page2(ft.Control):
    def __init__(self, page: ft.Page, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.pc = pc

    # @memory_profiler
    def did_mount(self):
        self.page.session.set("last_page", "Page2")
        print('did mount page 2')
        self.page.update()

    def content(self):
        last_page = self.page.session.get("last_page")
        return ft.Column(            
            controls=[
                ft.Text("This is Page 2"),
                ft.ElevatedButton("Go to Page 1", on_click=lambda _: self.pc.load_page("Login")),
                ft.Text(f"Last Page: {last_page}", selectable=False),
            
            ]
        )
