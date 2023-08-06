import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import psycopg2
import webbrowser 

USER_DATA_TABLE = "user_data"
entry_email = None
entry_budget = None
entry_product = None
entry_description = None
entry_developer_type = None

def get_user_input():
    email = entry_email.get()
    budget = float(entry_budget.get())
    product = entry_product.get()
    description = entry_description.get("1.0", tk.END).strip()
    developer_type = entry_developer_type.get()

    return email, budget, product, description, developer_type

def save_user_data(data):
    conn = psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        database="postgres",
        user="postgres",
        password="fender123"
    )
    cur = conn.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {USER_DATA_TABLE} (email TEXT, budget FLOAT, product TEXT, description TEXT, developer_type TEXT);")
    for user in data:
        cur.execute(f"INSERT INTO {USER_DATA_TABLE} VALUES (%s, %s, %s, %s, %s);", (user["email"], user["budget"], user["product"], user["description"], user["developer_type"]))
    conn.commit()
    cur.close()
    conn.close()

def load_user_data():
    conn = psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        database="postgres",
        user="postgres",
        password="fender123"
    )
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {USER_DATA_TABLE};")
    data = cur.fetchall()
    cur.close()
    conn.close()

    users = []
    for user in data:
        users.append({
            "email": user[0],
            "budget": user[1],
            "product": user[2],
            "description": user[3],
            "developer_type": user[4]
        })

    return users

def match_developers (user_data):
    conn = psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        database="postgres",
        user="owner",
        password="fender123"
    )
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {USER_DATA_TABLE} WHERE budget >= %s AND LOWER(product) = LOWER(%s) AND LOWER(developer_type) = LOWER(%s);",
                (user_data["budget"], user_data["product"], user_data["developer_type"]))
    data = cur.fetchall()
    cur.close()
    conn.close()

    matching_developers = []
    for developer in data:
        matching_developers.append({
            "email": developer[0],
            "budget": developer[1],
            "product": developer[2],
            "description": developer[3],
            "developer_type": developer[4]
        })

    return matching_developers

def register_developer():
    email, budget, product, description, developer_type = get_user_input()

    user_data = {
        "email": email,
        "budget": budget,
        "product": product,
        "description": description,
        "developer_type": developer_type
    }

    save_user_data([user_data])
    messagebox.showinfo("Registration Successful", "You have been registered as a freelance developer.")

def register_client():
    email, budget, product, description, developer_type = get_user_input()

    user_data = {
        "email": email,
        "budget": budget,
        "product": product,
        "description": description,
        "developer_type": developer_type
    }

    save_user_data([user_data])
    messagebox.showinfo("Registration Successful", "You have been registered as a client searching for a developer.")

def find_developer():
    user_email, user_budget, user_product, user_description, user_developer_type = get_user_input()

    user_data = {
        "email": user_email,
        "budget": user_budget,
        "product": user_product,
        "description": user_description,
        "marketing_type": user_developer_type
    }

    matching_developers = match_developers(user_data)

    if matching_developers:
        result = "Matching developers:\n"
        for developer in matching_developers:
            result += f"Email: {developer['email']}\n"
            result += f"Description: {developer['description']}\n"
            result += f"Marketing Type: {developer['developer_type']}\n\n"
        messagebox.showinfo("Match Found", result)

        selected_developer = simpledialog.askstring("Select developer", "Enter the email of the developer you want to message:")

        if selected_developer:
            message = simpledialog.askstring("Send Message", "Enter your message:")
            if message:
                messagebox.showinfo("Message Sent", "Your message has been sent.")
            else:
                messagebox.showinfo("Message Not Sent", "Please enter a message.")
    else:
        messagebox.showinfo("No Match", "No matching developer/client found.")

def view_profile():
    email = entry_email.get()
    users = load_user_data()

    for user in users:
        if user["email"] == email:
            profile = f"Email: {user['email']}\n"
            profile += f"Budget: {user['budget']}\n"
            profile += f"Product: {user['product']}\n"
            profile += f"Description: {user['description']}\n"
            profile += f"developer type: {user['developer_type']}"
            messagebox.showinfo("Profile", profile)
            break
    else:
        messagebox.showinfo("Profile", "No profile found for the provided email.")

def open_help_website():
    webbrowser.open("https://pencil13130.wixsite.com/falcon")

def main():
    global entry_email, entry_budget, entry_product, entry_description, entry_developer_type

    window = tk.Tk()
    window.title("falmark. instant clinets.")

     # Styling
    window.configure(bg="#F5F5F5")
    window.geometry("400x400")
    window.resizable(False, False)

    label_email = tk.Label(window, text="Email:", bg="#F5F5F5")
    label_email.grid(row=0, column=0, pady=5)
    entry_email = tk.Entry(window)
    entry_email.grid(row=0, column=1, pady=5)

    label_budget = tk.Label(window, text="Budget:", bg="#F5F5F5")
    label_budget.grid(row=1, column=0, pady=5)
    entry_budget = tk.Entry(window)
    entry_budget.grid(row=1, column=1, pady=5)

    label_product = tk.Label(window, text="your Project idea/service you provide:", bg="#F5F5F5")
    label_product.grid(row=2, column=0, pady=5)
    entry_product = tk.Entry(window)
    entry_product.grid(row=2, column=1, pady=5)

    label_description = tk.Label(window, text="Description:", bg="#F5F5F5")
    label_description.grid(row=3, column=0, pady=5)
    entry_description = tk.Text(window, height=4, width=20)
    entry_description.grid(row=3, column=1, pady=5)

    label_developer_type = tk.Label(window, text="Developer type:", bg="#F5F5F5")
    label_developer_type.grid(row=4, column=0, pady=5)
    entry_developer_type = tk.Entry(window)
    entry_developer_type.grid(row=4, column=1, pady=5)

    button_register_developer = tk.Button(window, text="Register as a developer", command=register_developer, width=20)
    button_register_developer.grid(row=5, column=0, pady=10)

    button_register_client = tk.Button(window, text="Register as a Client", command=register_client, width=20)
    button_register_client.grid(row=5, column=1, pady=10)

    button_find_developer = tk.Button(window, text="Find a developer or client", command=find_developer, width=20)
    button_find_developer.grid(row=6, column=0, columnspan=2, pady=10)

    button_view_profile = tk.Button(window, text="View Profile", command=view_profile, width=20)
    button_view_profile.grid(row=7, column=0, columnspan=2, pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()


      