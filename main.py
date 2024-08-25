import flet as ft
from controllers.page_control import PageControl
# from components.memory_usage import memory_profiler

# @memory_profiler
def main(page: ft.Page):
    page.title = "My App"
    page.window.width =300
    page.window.left = 3000
    page.window.always_on_top = True
    # Instantiate PageControl with the page instance
    pc = PageControl(page)

    # Load the first page
    pc.load_page("Login")

ft.app(target=main, assets_dir='assets')
