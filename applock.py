import tkinter as tk
from tkinter import messagebox
import hashlib

# Функция для хеширования PIN-кода
def hash_pin(pin):
    return hashlib.sha256(pin.encode()).hexdigest()

# Функция для проверки PIN-кода
def check_pin():
    entered_pin = pin_entry.get()
    if hash_pin(entered_pin) == stored_pin_hash:
        messagebox.showinfo("Доступ разрешен", "PIN-код правильный. Доступ разрешен.")
        root.quit()  # Закрытие приложения после успешной проверки
    else:
        messagebox.showwarning("Доступ запрещен", "Неправильный PIN-код. Попробуйте снова.")
        pin_entry.delete(0, tk.END)  # Очистка поля ввода

# Хранимый хешированный PIN-код (пример: "1234")
stored_pin_hash = hash_pin("1234")

# Создание основного окна
root = tk.Tk()
root.title("Блокировка действий")

# Создание виджетов
label = tk.Label(root, text="Введите PIN-код для разблокировки:")
label.pack(pady=10)

pin_entry = tk.Entry(root, show="*", width=10)
pin_entry.pack(pady=5)

submit_button = tk.Button(root, text="Проверить", command=check_pin)
submit_button.pack(pady=10)

# Запуск основного цикла приложения
root.mainloop()
