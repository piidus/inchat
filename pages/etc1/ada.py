import flet as ft
class Ada(ft.Control): 
    def __init__(self, page: ft.Page, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.pc = pc  
        # page.title = "Adaptive Height Text Field"
    def content(self):
        text_field = ft.TextField(
            label="Enter your text",
            adaptive=True,
        )

        # self.page.add(text_field)

        self.page.update()
        return ft.Column(
            controls=[
                ft.ListView(controls=[ ft.Text("Adaptive Text Field"+ str(i)) for i in range(100)], padding=10),
                text_field],
        )