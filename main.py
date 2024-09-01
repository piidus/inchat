from flet import Page, app
from controllers.page_control import PageControl


# @memory_test
def main(page: Page):
    page.title = "In-Chat"
    page.window.width =300
    # page.window.left = 3000
    page.window.always_on_top = True
    # Instantiate PageControl with the page instance
    pc = PageControl(page)

    # Load the first page
    pc.load_page("Chat")

app(target=main, assets_dir='assets')
#flet run -r
