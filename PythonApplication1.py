import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class TuringMachine:
    def __init__(self):
        self.tape = [' '] * 30  # Лента машины Тьюринга с начальными пробелами
        self.position = 0  # Текущая позиция на ленте
        self.state = 'q0'  # Текущее состояние машины
        self.transition_table = {}  # Таблица переходов

    def move_left(self):
        self.position -= 1
        if self.position < 0:
            self.tape.insert(0, ' ')
            self.position = 0

    def move_right(self):
        self.position += 1
        if self.position >= len(self.tape):
            self.tape.append(' ')

    def write(self, symbol):
        self.tape[self.position] = symbol

    def read(self):
        return self.tape[self.position]

    def add_transition_rule(self, state, symbol, new_symbol, move, new_state):
        self.transition_table[(state, symbol)] = (new_symbol, move, new_state)

    def remove_transition_rule(self, state, symbol):
        if (state, symbol) in self.transition_table:
            del self.transition_table[(state, symbol)]

    def step(self):
        current_symbol = self.read()

        if (self.state, current_symbol) in self.transition_table:
            new_symbol, move, new_state = self.transition_table[(self.state, current_symbol)]
            self.write(new_symbol)

            if move == 'L':
                self.move_left()
            elif move == 'R':
                self.move_right()

            self.state = new_state  # Обновляем состояние машины

    def reset_machine(self):
        self.tape = [' '] * 30
        self.position = 0
        self.state = 'q0'


class TuringMachineGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Машина Тьюринга")

        self.turing_machine = TuringMachine()

        self.label = tk.Label(root, text="Лента машины Тьюринга:")
        self.label.pack()

        self.tape_label = tk.Label(root, text='', font=("Arial", 12))
        self.tape_label.pack()

        self.state_label = tk.Label(root, text='Состояние: ' + self.turing_machine.state)
        self.state_label.pack()

        self.update_tape_label()

        self.head_rect = None  # Прямоугольник для головки

        # фрейм для кнопок
        self.button_frame = tk.Frame(root, bg="white")
        self.button_frame.pack()

        self.left_button = tk.Button(self.button_frame, text="←", command=self.move_left, bg="white")
        self.left_button.pack(side="left", padx=5)

        self.right_button = tk.Button(self.button_frame, text="→", command=self.move_right, bg="white")
        self.right_button.pack(side="left", padx=5)

        self.write_button_1 = tk.Button(self.button_frame, text="Записать 1", command=self.write_1, bg="white")
        self.write_button_1.pack(side="left", padx=5)

        self.write_button_0 = tk.Button(self.button_frame, text="Записать 0", command=self.write_0, bg="white")
        self.write_button_0.pack(side="left", padx=5)

        self.write_button_blank = tk.Button(self.button_frame, text="Записать _", command=self.write_blank, bg="white")
        self.write_button_blank.pack(side="left", padx=5)

        self.erase_button = tk.Button(self.button_frame, text="Стереть", command=self.erase, bg="white")

        self.reset_button = tk.Button(self.button_frame, text="Сброс", command=self.reset_machine, bg="white")
        self.reset_button.pack(side="left", padx=5)

        self.erase_button.pack(side="left", padx=5)

        self.input_label = tk.Label(root, text="Введите последовательность:")
        self.input_label.pack()

        self.input_entry = tk.Entry(root)
        self.input_entry.pack()

        self.load_button = tk.Button(root, text="Загрузить на ленту", command=self.load_input, bg="white")
        self.load_button.pack()

        self.transition_table_frame = ttk.Frame(root)
        self.transition_table_frame.pack()

        self.transition_table_label = ttk.Label(self.transition_table_frame, text="Таблица переходов:")
        self.transition_table_label.pack()

        self.transition_tree = ttk.Treeview(self.transition_table_frame,
                                            columns=("state", "symbol", "new_symbol", "move", "new_state"),
                                            show="headings")
        self.transition_tree.heading("state", text="Состояние")
        self.transition_tree.heading("symbol", text="Символ")
        self.transition_tree.heading("new_symbol", text="Новый символ")
        self.transition_tree.heading("move", text="Движение")
        self.transition_tree.heading("new_state", text="Новое состояние")
        self.transition_tree.pack()

        self.add_rule_button = tk.Button(root, text="Добавить правило", command=self.add_transition_rule, bg="white")
        self.add_rule_button.pack(side="left", padx=5)

        self.remove_rule_button = tk.Button(root, text="Удалить правило", command=self.remove_transition_rule,
                                            bg="white")
        self.remove_rule_button.pack(side="left", padx=5)

        self.load_rules_button = tk.Button(root, text="Загрузить правила из файла", command=self.load_rules, bg="white")
        self.load_rules_button.pack(side="left", padx=5)

        self.step_button = tk.Button(root, text="Выполнить шаг", command=self.execute_step, bg="white")
        self.step_button.pack(side="left", padx=5)

        self.change_to_windows_style()

    def change_to_windows_style(self):
        self.root.style = ttk.Style()
        self.root.style.theme_use('alt')

        # фоновый цвет окна и виджетов на белый
        self.root.configure(bg="white")
        self.input_label.configure(bg="white")
        self.state_label.configure(bg="white")
        self.label.configure(bg="white")

    #  self.right_button.configure(style="TButton", font=("Segoe UI", 10))

    def reset_machine(self):
        self.turing_machine.reset_machine()
        self.update_tape_label()
        self.state_label.config(text='Состояние: ' + self.turing_machine.state)

    def load_transition_rules(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    parts = line.strip().split()
                    if len(parts) == 5:
                        state, symbol, new_symbol, move, new_state = parts
                        self.turing_machine.add_transition_rule(state, symbol, new_symbol, move, new_state)
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")

    def load_rules(self):
        filename = tk.filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if filename:
            self.load_transition_rules(filename)
            self.update_transition_table()

    def move_left(self):
        self.turing_machine.move_left()
        self.update_tape_label()

    def move_right(self):
        self.turing_machine.move_right()
        self.update_tape_label()

    def write_1(self):
        self.turing_machine.write('1')
        self.update_tape_label()

    def write_0(self):
        self.turing_machine.write('0')
        self.update_tape_label()

    def write_blank(self):
        self.turing_machine.write('_')
        self.update_tape_label()

    def erase(self):
        self.turing_machine.write(' ')
        self.update_tape_label()

    def load_input(self):
        input_text = self.input_entry.get()
        for symbol in input_text:
            self.turing_machine.write(symbol)
            self.turing_machine.move_right()
        self.update_tape_label()

    def add_transition_rule(self):
        # Окно для ввода нового правила
        rule_window = tk.Toplevel(self.root)
        rule_window.title("Добавить правило")

        # Поля для ввода данных правила
        state_label = tk.Label(rule_window, text="Состояние:")
        state_label.grid(row=0, column=0)
        state_entry = tk.Entry(rule_window)
        state_entry.grid(row=0, column=1)

        symbol_label = tk.Label(rule_window, text="Символ:")
        symbol_label.grid(row=1, column=0)
        symbol_entry = tk.Entry(rule_window)
        symbol_entry.grid(row=1, column=1)

        new_symbol_label = tk.Label(rule_window, text="Новый символ:")
        new_symbol_label.grid(row=2, column=0)
        new_symbol_entry = tk.Entry(rule_window)
        new_symbol_entry.grid(row=2, column=1)

        move_label = tk.Label(rule_window, text="Движение:")
        move_label.grid(row=3, column=0)
        move_entry = tk.Entry(rule_window)
        move_entry.grid(row=3, column=1)

        new_state_label = tk.Label(rule_window, text="Новое состояние:")
        new_state_label.grid(row=4, column=0)
        new_state_entry = tk.Entry(rule_window)
        new_state_entry.grid(row=4, column=1)

        # Функция для добавления правила в таблицу переходов
        def add_rule():
            state = state_entry.get()
            symbol = symbol_entry.get()
            new_symbol = new_symbol_entry.get()
            move = move_entry.get()
            new_state = new_state_entry.get()

            if state and symbol and new_symbol and move and new_state:
                self.turing_machine.add_transition_rule(state, symbol, new_symbol, move, new_state)
                self.update_transition_table()
                rule_window.destroy()

        add_button = tk.Button(rule_window, text="Добавить", command=add_rule)
        add_button.grid(row=5, columnspan=2)

    def remove_transition_rule(self):
        selected_item = self.transition_tree.selection()
        if selected_item:
            item = self.transition_tree.item(selected_item, 'values')
            state, symbol = item[0], item[1]
            self.turing_machine.remove_transition_rule(state, symbol)
            self.update_transition_table()

    def execute_step(self):
        self.turing_machine.step()
        self.update_transition_table()
        self.update_tape_label()
        self.state_label.config(text='Состояние: ' + self.turing_machine.state)

    def update_tape_label(self):
        tape_str = ''.join(self.turing_machine.tape)
        self.tape_label.config(text=tape_str)
        head_position = self.turing_machine.position
        self.tape_label.config(
            text=tape_str[:head_position] + '[' + tape_str[head_position] + ']' + tape_str[head_position + 1:])

    def update_transition_table(self):
        self.transition_tree.delete(*self.transition_tree.get_children())
        for (state, symbol), (new_symbol, move, new_state) in self.turing_machine.transition_table.items():
            self.transition_tree.insert("", "end", values=(state, symbol, new_symbol, move, new_state))


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    app = TuringMachineGUI(root)
    root.mainloop()
