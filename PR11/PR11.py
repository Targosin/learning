import tkinter as tk
from tkinter import messagebox, filedialog
import json
import urllib.request
import urllib.error

def get_github_info():
    """Получает информацию о пользователе GitHub по имени и сохраняет в JSON."""
    username = entry.get().strip()
    
    if not username:
        messagebox.showwarning("Внимание", "Введите имя пользователя GitHub.")
        return
    
    try:
        url = f"https://api.github.com/users/{username}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        with urllib.request.urlopen(req) as response:
            data = response.read()
            user_data = json.loads(data)

        result = {
            'company': user_data.get('company'),
            'created_at': user_data.get('created_at'),
            'email': user_data.get('email'),
            'id': user_data.get('id'),
            'name': user_data.get('name'),
            'url': user_data.get('url')
        }
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")],
            initialfile="github_info.json"
        )
        
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=4)
            messagebox.showinfo("Успех", f"Данные сохранены в:\n{file_path}")
    
    except urllib.error.HTTPError as e:
        messagebox.showerror("Ошибка", f"Не найден: {username}\nОшибка: {e.code}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка: {str(e)}")

# Создаем GUI
app = tk.Tk()
app.title("GitHub Info - Практическая работа 11")
app.geometry("400x150")

tk.Label(app, text="Имя пользователя GitHub:").pack(pady=10)
entry = tk.Entry(app, width=30)
entry.pack(pady=5)
entry.insert(0, "apache")  

tk.Button(app, text="Получить данные и сохранить", command=get_github_info).pack(pady=20)

app.mainloop()