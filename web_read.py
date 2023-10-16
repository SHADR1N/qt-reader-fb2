import os
from functools import partial

import flet as ft


class WebReader:
    def __init__(self, page: ft.Page):
        self.page = page
        self.file_picker = ft.FilePicker(on_result=self.on_dialog_result)
        self.text_content = ft.Text(value="Raw book...", size=20, text_align=ft.alignment.center)
        self.main()

    def on_dialog_result(self, e: ft.FilePickerResultEvent):
        print("Selected files:", e.files)
        print("Selected file or directory:", e.path)

    def upload_files(self, e):
        page = e.page
        upload_list = []
        if self.file_picker.result is not None and self.file_picker.result.files is not None:
            for f in self.file_picker.result.files:
                upload_list.append(
                    ft.FilePickerUploadFile(
                        f.name,
                        upload_url=page.get_upload_url(f.name, 600),
                    )
                )
            self.file_picker.upload(upload_list)

    def start_read(self, *args):
        print("start")

    def stop_read(self, *args):
        print("stop")

    def select_book(self, path, *args):
        self.path_book = path
        print("set book")

    def main(self):
        self.page.title = "FletReadBook by SHADRIN"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER

        path_books = os.listdir("books")

        books = [
            ft.ElevatedButton(
                text=path,
                on_click=partial(self.select_book, path)) for path in path_books if ".fb2" in path
        ]

        self.page.add(

            ft.Column(
                controls=[
                    ft.Column(
                        controls=books,
                        wrap=False,
                        height=200,
                        width=400,
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            self.file_picker,
                            ft.ElevatedButton(
                                text="Choose files...",
                                on_click=partial(self.file_picker.pick_files, allow_multiple=True)
                            ),
                            ft.ElevatedButton(
                                text="Upload",
                                on_click=self.upload_files
                            )
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.ElevatedButton(
                                text="Start",
                                on_click=self.start_read
                            ),
                            ft.ElevatedButton(
                                text="Stop",
                                on_click=self.stop_read
                            ),
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[self.text_content]
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )


if __name__ == "__main__":
    ft.app(
        view=ft.WEB_BROWSER,
        target=WebReader,
        upload_dir="books",
    )
