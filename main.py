import flet as ft 
from app import getresposta
def main(page:ft.Page):
    page.title="CloneGPT"
    page.theme_mode=ft.ThemeMode.LIGHT
    page.padding=20
    page.window.full_screen=True

    chat_list=ft.ListView()
        

    def addChat(mesagem,tipo):
        if tipo=="user":
            chat_list.controls.append(
            ft.Text(mesagem)
        )
            page.update()
        resposta=getresposta(mesagem)
        chat_list.controls.append(
        ft.Container(padding=10,bgcolor=ft.colors.INDIGO_50,content=ft.Text(resposta),border_radius=10)
                    )

        page.update()
    def clear(e):
        chat_list.controls.clear()
        page.update()
    header=ft.Container(padding=10,content=ft.Row([
        ft.Text("CloneGpt",size=25,color=ft.colors.INDIGO_800,weight="bold"),
        ft.IconButton(ft.icons.ADD,on_click=clear)
    ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),bgcolor=ft.colors.INDIGO_200)


    
    input=ft.TextField(label="Ola clonegpt")
    chatbody=ft.Container(expand=True,content=chat_list,padding=10)
    footer=ft.Container(content=ft.Row([
        input,
        ft.IconButton(ft.icons.SEND,on_click=lambda e: addChat(input.value,"user"))
    ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),padding=10,bgcolor=ft.colors.INDIGO_200)

    layout=ft.Container(bgcolor=ft.colors.INDIGO_100,width=400,height=page.window.height,border_radius=10,expand=True, content=ft.Column([
        header,
        chatbody,
        footer
    ]))
    page.add(ft.Container(expand=True,content=ft.Row([layout,ft.Text("CloneGPT\nBy Ghost04",weight="bold",size=200,color=ft.colors.INDIGO_600)])))
    
ft.app(target=main)