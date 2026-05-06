import tkinter as tk
from tkinter import messagebox



CONTACTS_LIST = [
    ['Alice', '555-1234', 'alice@example.com', '123 Main St'],
    ['Bob', '555-5678', 'bob@example.com', '456 Oak Ave']
]




def add_contact(name, phone, email, address):
    if name and phone:
        CONTACTS_LIST.append([name, phone, email, address])
        return f"Successfully Added: {name}"
    else:
        return "Error: Name and Phone are required."

def display_all_contacts(display_output_widget):
    display_output_widget.delete('1.0', tk.END)
    display_output_widget.insert(tk.END, "--- ALL CONTACTS ---\n")
    for contact in CONTACTS_LIST:
        output_string = f"Name: {contact[0]} | Phone: {contact[1]} | Email: {contact[2]}"
        display_output_widget.insert(tk.END, output_string + "\n")
    display_output_widget.insert(tk.END, f"\nTotal Contacts: {len(CONTACTS_LIST)}")
    return "Display complete."

def search_contact(search_name):
    result = []
    for i in CONTACTS_LIST:
        if i[0].lower() == search_name.lower():
            result.append(i)
            return result

def delete_contact(target_name):
    for i in CONTACTS_LIST:
        if i [0]== target_name:
            CONTACTS_LIST.remove(i)
            return f"{target_name} was deleted"
    return f"{target_name} was not found"
    

def update_contact(old_name, new_name, new_phone, new_email, new_address):
    updated = False
    for i in CONTACTS_LIST:
        if i[0] == old_name:
            i[0] = new_name
            i[1] = new_phone
            i[2] = new_email
            i[3] = new_address
            updated = True
            break
    if updated:
        return f"Contact '{old_name}' successfully updated to '{new_name}'."
    else:
        return f"Error: Contact '{old_name}' not found."


def add_contact_handler():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()
    result_message = add_contact(name, phone, email, address)
    messagebox.showinfo("Result", result_message)
    clear_entries()

def display_all_handler():
    display_all_contacts(result_text)

def search_contact_handler():
    name_to_search = entry_name.get()
    if name_to_search:
        search_result = search_contact(name_to_search)
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, f"Search results for '{name_to_search}':\n")
        if search_result:
            result_text.insert(tk.END, str(search_result) + "\n")
        else:
            result_text.insert(tk.END, "Contact not found.")
    else:
        messagebox.showwarning("Input Error", "Enter a name to search.")

def delete_contact_handler():
    name_to_delete = entry_name.get()
    if name_to_delete:
        result_message = delete_contact(name_to_delete)
        messagebox.showinfo("Result", result_message)
        clear_entries()
        display_all_contacts(result_text)
    else:
        messagebox.showwarning("Input Error", "Enter the name of the contact to delete.")

def update_contact_handler():
    old_name = entry_name.get()
    new_name = entry_name.get()
    new_phone = entry_phone.get()
    new_email = entry_email.get()
    new_address = entry_address.get()
    if old_name:
        result_message = update_contact(old_name, new_name, new_phone, new_email, new_address)
        messagebox.showinfo("Result", result_message)
        clear_entries()
        display_all_contacts(result_text)
    else:
        messagebox.showwarning("Input Error", "Enter the name of the contact to update.")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)





app = tk.Tk()
app.title("Contact Manager (Improved UI)")
app.geometry("850x650")
app.config(bg="#2c3e50")

font_title = ("Arial", 18, "bold")
font_label = ("Arial", 11)
font_btn = ("Arial", 11, "bold")

title_label = tk.Label(app, text="Contact Manager", font=font_title, bg="#2c3e50", fg="white")
title_label.pack(pady=10)

container = tk.Frame(app, bg="#ecf0f1", padx=15, pady=10, bd=2, relief="groove")
container.pack(fill="x", padx=20)

# Inputs
input_frame = tk.Frame(container, bg="#ecf0f1")
input_frame.pack()

tk.Label(input_frame, text="Name:", font=font_label, bg="#ecf0f1").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(input_frame, width=30)
entry_name.grid(row=0, column=1)

tk.Label(input_frame, text="Phone:", font=font_label, bg="#ecf0f1").grid(row=1, column=0, padx=5, pady=5)
entry_phone = tk.Entry(input_frame, width=30)
entry_phone.grid(row=1, column=1)

tk.Label(input_frame, text="Email:", font=font_label, bg="#ecf0f1").grid(row=0, column=2, padx=5, pady=5)
entry_email = tk.Entry(input_frame, width=30)
entry_email.grid(row=0, column=3)

tk.Label(input_frame, text="Address:", font=font_label, bg="#ecf0f1").grid(row=1, column=2, padx=5, pady=5)
entry_address = tk.Entry(input_frame, width=30)
entry_address.grid(row=1, column=3)

# Buttons
btn_frame = tk.Frame(app, bg="#2c3e50")
btn_frame.pack(pady=10)

def make_btn(txt, cmd):
    return tk.Button(btn_frame, text=txt, command=cmd, font=font_btn, bg="#3498db", fg="white", width=12)

make_btn("Add Contact", add_contact_handler).pack(side=tk.LEFT, padx=5)
make_btn("Display All", display_all_handler).pack(side=tk.LEFT, padx=5)
make_btn("Search", search_contact_handler).pack(side=tk.LEFT, padx=5)
make_btn("Delete", delete_contact_handler).pack(side=tk.LEFT, padx=5)
make_btn("Update", update_contact_handler).pack(side=tk.LEFT, padx=5)

tk.Button(btn_frame, text="Clear Fields", command=clear_entries, font=font_btn,
          bg="#95a5a6", fg="white", width=12).pack(side=tk.LEFT, padx=5)

# Results
result_label = tk.Label(app, text="All Contacts:", font=font_label, bg="#2c3e50", fg="white")
result_label.pack()

result_text = tk.Text(app, height=18, width=95, wrap=tk.WORD, bg="white")
result_text.pack(padx=10, pady=5)

display_all_contacts(result_text)

app.mainloop()
