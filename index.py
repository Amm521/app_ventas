import flet as ft
from utilities import *

def main(page: ft.Page):

    df = read_data()    # Read data from csv file
    page.title = "App Ventas"   # Set the title of the app
    # Create a text field for the search bar
    lista_productos = pd.DataFrame()    
    print(lista_productos.empty)
    material = ft.TextField(label="Buscador de articulos: ", text_align=ft.TextAlign.LEFT, hint_text="Escribe el nombre del articulo")

    def edit_search(material):
        nrows = data.rows[:-1]

        # pass
    
    # Function to create a table with the data
    def create_table(rows):
        data = ft.DataTable(
            # width=700,
            bgcolor="blue",
            border=ft.border.all(2, "blue"),
            border_radius=10,
            vertical_lines=ft.BorderSide(3, "black"),
            horizontal_lines=ft.BorderSide(1, "black"),
            sort_column_index=0,
            sort_ascending=True,
            heading_row_color=ft.colors.BLACK12,
            heading_row_height=100,
            data_row_color={"hovered": "0x30FF0000"},
            show_checkbox_column=True,
            divider_thickness=0,
            column_spacing=200,
            columns=[ft.DataColumn(ft.Text("Articulo"), on_sort=lambda e: print(f"{e.column_index}, {e.ascending}")),
                     ft.DataColumn(ft.Text("Precio"), tooltip="This is a second column", numeric=True, on_sort=lambda e: print(f"{e.column_index}, {e.ascending}")),
                     ft.DataColumn(ft.Text("Cantidad"), numeric=True, on_sort=lambda e: print(f"{e.column_index}, {e.ascending}")),
            ],
            rows=rows
        )
        return data

    page.add(material)

    # Create an empty table
    rows = [ft.DataRow([ft.DataCell(ft.Text("")) for i in range(len(df.columns))])]
    # Create a table with the data
    data = create_table(rows)
    page.add(data)

    # Function to search for a product
    def on_keyboard(e: ft.KeyboardEvent, lista_productos=lista_productos):
        if e.key=="Enter":
            if not lista_productos.empty: lista_productos = pd.concat([lista_productos, search(material.value, df)])
            else: lista_productos = search(material.value, df)
            print_search(e)
            print(data.rows)
            print("LISTA PRODUCTOS", lista_productos)

    
    def print_search(e):
        values = [df.loc[df["material"] == material.value].values][0][0]
        selfmaterial = material.value
        print("VALUES", values, len(values))
        new_row = ft.DataRow([
            ft.DataCell(ft.Text(values[0]), on_double_tap=edit_search(selfmaterial)),
            ft.DataCell(ft.Text(str(values[1])), on_double_tap=edit_search(selfmaterial)),
            ft.DataCell(ft.Text(str(values[2])), on_double_tap=edit_search(selfmaterial))
            ],)
        if data.rows == rows:
            data.rows = [new_row]
            print("DATA ROWS 1", data.rows[0])

        else: 
            data.rows.append(new_row)
        print("DATA ROWS 2", data.rows[0])
        t.value = f"{material.value} encontrado"
        page.update()
        
    page.on_keyboard_event = on_keyboard
    t = ft.Text(lista_productos.values)
    page.add(t)

    def button_click(e):
        page.add(ft.Text("Hello!"))
    # page.add(ft.ElevatedButton("Say hello!", on_click=button_click))
df = read_data()
material = "soap"
cells = [f"{i}" for i in df.loc[df["material"] == material].values]
print(cells)
print(df.loc[df["material"] == material].values)
ft.app(main)






































def counter(page: ft.Page):
    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()
        
    page.title = "App Ventas"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    