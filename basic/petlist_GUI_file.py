from tkinter import Tk, ttk, Label, Button, Text, END
import json

petstores = []
file_name = './basic/petstores.json'
with open(file_name, 'r') as petstores_file:
    petstores = json.load(petstores_file)

selected_index = 0

def setTreeItems():
    # Delete all rows on treePetstores
    treePetstores.delete(*treePetstores.get_children())
    for idx, petstore in enumerate(petstores): 
        item = petstore['item']
        price = petstore['price']
        treePetstores.insert("", END, iid=None, text=str(idx), values=[item, price])   

def petstores_selected(event):
    global selected_index
    for item in treePetstores.selection():
        selected_index = int(treePetstores.item(item, "text"))
    petstore = petstores[selected_index]
    item = petstore['item']
    price = str(petstore['price'])
    text_Item.delete('1.0', END)
    text_Item.insert(END, item)
    text_Price.delete('1.0', END)
    text_Price.insert(END, price)

def insert_content():
    item = text_Item.get('1.0', END)
    price = float(text_Price.get('1.0', END))
    petstore = { 'item': item.rstrip(), 'price': price }
    petstores.append(petstore)
    setTreeItems()

def update_content():
    global selected_index
    item = text_Item.get('1.0', END)
    price = float(text_Price.get('1.0', END))
    selectedItem = petstores[selected_index]
    selectedItem['item'] = item.rstrip()
    selectedItem['price'] = price
    setTreeItems()

def delete_content():
    global selected_index
    petstores.pop(selected_index)
    setTreeItems()

def save_content():
    with open(file_name, 'w', encoding='UTF-8') as petstores_file:
        jsonString = json.dumps(petstores, ensure_ascii=False)
        petstores_file.write(jsonString)
    petstores_file.close()
# encording은 형태를 설정하기 위해 적어줌.

window = Tk()
window.title("Pet List Management")
window.geometry("600x600")
window.resizable(0,0)
title = "Pet List Manager"
lbl_title = Label(window, text=title, font=("helvetica",20))
lbl_title.pack(padx=5, pady=15)

# Display pet list on treePetstores
treePetstores = ttk.Treeview(window)
treePetstores['columns']=('item', 'price')
treePetstores.column('#0', width=50)
treePetstores.column('item', width=200)
treePetstores.column('price', width=150)
treePetstores.heading('#0', text='No')
treePetstores.heading('item', text='Item')
treePetstores.heading('price', text='Price')
treePetstores.place(x=100, y=100, width=400, height=250)
# Bind select event to petstores_selected
treePetstores.bind('<<TreeviewSelect>>', petstores_selected)

labelItem = Label(window, text='Item')
labelItem.place(x=100, y=400, width=50, height=25)
labelPrice = Label(window, text='Price')
labelPrice.place(x=100, y=450, width=50, height=25)
text_Item = Text(window, width=30, height=1)
text_Item.place(x=200, y=400)
text_Price = Text(window, width=30, height=1)
text_Price.place(x=200, y=450)

btn_Insert = Button(window, text='Insert', command=insert_content, font=("helvetica",14) )
btn_Insert.place(x=100, y=500, width=100, height=30)

btn_Update = Button(window, text='Update', command=update_content, font=("helvetica",14) )
btn_Update.place(x=200, y=500, width=100, height=30)

btn_Delete = Button(window, text='Delete', command=delete_content, font=("helvetica",14) )
btn_Delete.place(x=300, y=500, width=100, height=30)

btn_Save = Button(window, text='Save', command=save_content, font=("helvetica",14) )
btn_Save.place(x=400, y=500, width=100, height=30)

# Initialize treePetstores
setTreeItems()

window.mainloop()