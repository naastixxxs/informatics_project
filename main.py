import random
import tkinter as tk
from tkinter import messagebox

APP_TITLE = "Кодирование информации — обучение и мини-игра"
WINDOW_SIZE = "900x650"
WRAP = 740

COLORS = {
    "bg": "#f5f7fb",
    "card": "#ffffff",
    "border": "#e2e8f0",
    "text": "#1f2937",
    "muted": "#6b7280",
    "primary": "#4f46e5",
    "primary_dark": "#4338ca",
    "secondary": "#e2e8f0",
    "secondary_dark": "#cbd5e1",
    "success": "#16a34a",
    "danger": "#dc2626",
}

FONTS = {
    "title": ("Segoe UI", 19, "bold"),
    "header": ("Segoe UI", 16, "bold"),
    "section": ("Segoe UI", 13, "bold"),
    "body": ("Segoe UI", 11),
    "body_bold": ("Segoe UI", 11, "bold"),
    "small": ("Segoe UI", 10),
    "button": ("Segoe UI", 11, "bold"),
}


def style_button(button, variant="primary"):
    if variant == "primary":
        colors = (COLORS["primary"], "white", COLORS["primary_dark"], "white")
    elif variant == "secondary":
        colors = (COLORS["secondary"], COLORS["text"], COLORS["secondary_dark"], COLORS["text"])
    else:
        colors = (COLORS["card"], COLORS["text"], COLORS["secondary"], COLORS["text"])

    button.configure(
        bg=colors[0],
        fg=colors[1],
        activebackground=colors[2],
        activeforeground=colors[3],
        relief="flat",
        bd=0,
        highlightthickness=0,
        padx=12,
        pady=8,
        font=FONTS["button"],
        cursor="hand2",
        disabledforeground=COLORS["muted"],
    )


def make_button(parent, text, command, variant="primary", width=None):
    btn = tk.Button(parent, text=text, command=command, width=width)
    style_button(btn, variant=variant)
    return btn


def style_entry(entry):
    entry.configure(
        bg=COLORS["card"],
        fg=COLORS["text"],
        insertbackground=COLORS["text"],
        relief="solid",
        bd=1,
        highlightthickness=1,
        highlightbackground=COLORS["border"],
        highlightcolor=COLORS["primary"],
        font=FONTS["body"],
        disabledbackground=COLORS["secondary"],
        disabledforeground=COLORS["muted"],
    )

LESSON_ORDER = ["bits_bytes", "binary_numbers"]

LESSONS = {
    "bits_bytes": {
        "title": "Тема 1. Измерение информации",
        "theory": [
            "Информация в компьютере хранится в виде битов.\n"
            "Бит — это минимальная единица информации и может принимать 2 значения: 0 или 1.\n"
            "Байт — это 8 бит. Именно байт чаще всего используется для измерения объема данных.",
            "Крупные единицы строятся через множители 1024:\n"
            "1 КБ = 1024 байта\n"
            "1 МБ = 1024 КБ\n"
            "1 ГБ = 1024 МБ\n"
            "Эти значения часто используют при работе с файлами и памятью.",
            "Пример расчета:\n"
            "2 КБ = 2 × 1024 = 2048 байт.\n"
            "Если известно количество байт, можно найти биты: 1 байт = 8 бит.",
        ],
        "practice": [
            {
                "prompt": "Сколько бит в 3 байтах?",
                "answer": "24",
                "checker": "int",
                "explain": "1 байт = 8 бит, значит 3 × 8 = 24.",
            },
            {
                "prompt": "Сколько байт в 2 КБ?",
                "answer": "2048",
                "checker": "int",
                "explain": "1 КБ = 1024 байта, значит 2 × 1024 = 2048.",
            },
            {
                "prompt": "Сколько КБ в 3072 байтах?",
                "answer": "3",
                "checker": "int",
                "explain": "3072 / 1024 = 3 КБ.",
            },
        ],
    },
    "binary_numbers": {
        "title": "Тема 2. Двоичное кодирование чисел",
        "theory": [
            "В двоичной системе используются только цифры 0 и 1.\n"
            "Разряды справа налево имеют значения 1, 2, 4, 8, 16, 32 и т.д.\n"
            "Например, 1011₂ = 1×8 + 0×4 + 1×2 + 1×1 = 11.",
            "Перевод из десятичной системы в двоичную:\n"
            "делим число на 2, записываем остатки, читаем остатки снизу вверх.\n"
            "Пример: 13 → 1101₂.",
            "Перевод из двоичной системы в десятичную:\n"
            "складываем значения разрядов, где стоит 1.\n"
            "Пример: 1101₂ = 8 + 4 + 0 + 1 = 13.",
        ],
        "practice": [
            {
                "prompt": "Переведи 25 (десятичное) в двоичную систему.",
                "answer": "11001",
                "checker": "binary",
                "explain": "25 = 16 + 8 + 1, поэтому 11001.",
            },
            {
                "prompt": "Чему равно 10110₂ в десятичной системе?",
                "answer": "22",
                "checker": "int",
                "explain": "10110₂ = 16 + 4 + 2 = 22.",
            },
            {
                "prompt": "Переведи 7 (десятичное) в двоичную систему.",
                "answer": "111",
                "checker": "binary",
                "explain": "7 = 4 + 2 + 1, поэтому 111.",
            },
        ],
    },
}

QUESTION_BANK = [
    {
        "type": "mcq",
        "prompt": "Сколько бит в одном байте?",
        "options": ["4", "8", "16", "32"],
        "answer_index": 1,
        "explain": "1 байт всегда равен 8 битам.",
    },
    {
        "type": "mcq",
        "prompt": "Сколько байт в 1 КБ (кибибайте)?",
        "options": ["1000", "1024", "2048", "512"],
        "answer_index": 1,
        "explain": "В информатике 1 КБ = 1024 байта.",
    },
    {
        "type": "mcq",
        "prompt": "Какое число в десятичной системе соответствует 1010₂?",
        "options": ["10", "12", "8", "9"],
        "answer_index": 0,
        "explain": "1010₂ = 8 + 2 = 10.",
    },
    {
        "type": "mcq",
        "prompt": "Как записать десятичное число 5 в двоичном виде?",
        "options": ["101", "110", "111", "100"],
        "answer_index": 0,
        "explain": "5 = 4 + 1, значит 101₂.",
    },
    {
        "type": "mcq",
        "prompt": "Что больше: 1 МБ или 900 КБ?",
        "options": ["1 МБ", "900 КБ", "Одинаково", "Нельзя сравнить"],
        "answer_index": 0,
        "explain": "1 МБ = 1024 КБ, значит больше.",
    },
    {
        "type": "input",
        "prompt": "Переведи 25 (десятичное) в двоичную систему.",
        "answer": "11001",
        "checker": "binary",
        "explain": "25 = 16 + 8 + 1, поэтому 11001.",
    },
    {
        "type": "input",
        "prompt": "Чему равно число 11001₂ в десятичной системе?",
        "answer": "25",
        "checker": "int",
        "explain": "11001₂ = 16 + 8 + 1 = 25.",
    },
    {
        "type": "input",
        "prompt": "Сколько бит в 6 байтах?",
        "answer": "48",
        "checker": "int",
        "explain": "6 × 8 = 48 бит.",
    },
    {
        "type": "input",
        "prompt": "Сколько байт в 3 КБ?",
        "answer": "3072",
        "checker": "int",
        "explain": "3 × 1024 = 3072 байта.",
    },
    {
        "type": "input",
        "prompt": "Переведи 18 (десятичное) в двоичную систему.",
        "answer": "10010",
        "checker": "binary",
        "explain": "18 = 16 + 2, поэтому 10010.",
    },
]


def normalize_simple(text):
    return "".join(text.strip().split())


def parse_int(text):
    clean = normalize_simple(text)
    if clean.startswith("+"):
        clean = clean[1:]
    if not clean or not clean.isdigit():
        return None
    return int(clean)


def parse_binary(text):
    clean = normalize_simple(text)
    if not clean:
        return None
    if any(ch not in "01" for ch in clean):
        return None
    return clean


def evaluate_task(task, user_input):
    checker = task.get("checker", "int")
    if checker == "int":
        value = parse_int(user_input)
        if value is None:
            return False, False, "Введите целое число."
        return True, value == int(task["answer"]), ""
    if checker == "binary":
        value = parse_binary(user_input)
        if value is None:
            return False, False, "Введите двоичное число, используя только 0 и 1."
        expected = task["answer"].lstrip("0") or "0"
        got = value.lstrip("0") or "0"
        return True, got == expected, ""
    return False, False, "Неизвестный тип задания."


class MenuFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=COLORS["bg"])
        self.controller = controller
        self.progress_var = tk.StringVar()

        self.card = tk.Frame(
            self,
            bg=COLORS["card"],
            highlightthickness=1,
            highlightbackground=COLORS["border"],
        )
        self.card.pack(padx=40, pady=30, fill="both", expand=True)

        title = tk.Label(
            self.card,
            text=APP_TITLE,
            font=FONTS["title"],
            bg=COLORS["card"],
            fg=COLORS["text"],
        )
        title.pack(pady=(22, 8))

        info = tk.Label(
            self.card,
            text="Сначала пройдите обе темы, затем откроется мини-игра.",
            font=FONTS["body"],
            bg=COLORS["card"],
            fg=COLORS["muted"],
        )
        info.pack(pady=(0, 16))

        self.progress_label = tk.Label(
            self.card,
            textvariable=self.progress_var,
            font=FONTS["body"],
            bg=COLORS["card"],
            fg=COLORS["muted"],
        )
        self.progress_label.pack(pady=(0, 18))

        btn_frame = tk.Frame(self.card, bg=COLORS["card"])
        btn_frame.pack(pady=10)

        self.btn_lesson_1 = make_button(
            btn_frame,
            text="Обучение: Измерение информации",
            width=42,
            command=lambda: controller.show_lesson("bits_bytes"),
            variant="secondary",
        )
        self.btn_lesson_1.pack(pady=6)

        self.btn_lesson_2 = make_button(
            btn_frame,
            text="Обучение: Двоичное кодирование чисел",
            width=42,
            command=lambda: controller.show_lesson("binary_numbers"),
            variant="secondary",
        )
        self.btn_lesson_2.pack(pady=6)

        self.btn_game = make_button(
            btn_frame,
            text="Мини-игра: проверить знания",
            width=42,
            command=controller.show_game,
            variant="primary",
        )
        self.btn_game.pack(pady=(14, 10))

        exit_button = make_button(
            btn_frame, text="Выход", width=42, command=controller.destroy, variant="ghost"
        )
        exit_button.pack(pady=(0, 8))

    def refresh(self):
        done = sum(1 for value in self.controller.lessons_done.values() if value)
        total = len(self.controller.lessons_done)
        self.progress_var.set(f"Пройдено тем: {done} из {total}")
        if done == total:
            self.progress_label.config(fg=COLORS["success"])
        else:
            self.progress_label.config(fg=COLORS["muted"])
        self.btn_game.config(state="normal" if self.controller.all_lessons_done() else "disabled")


class LessonFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=COLORS["bg"])
        self.controller = controller
        self.lesson_id = None
        self.lesson = None
        self.page_index = 0
        self.practice_index = 0

        self.title_var = tk.StringVar()
        self.content_var = tk.StringVar()

        self.card = tk.Frame(
            self,
            bg=COLORS["card"],
            highlightthickness=1,
            highlightbackground=COLORS["border"],
        )
        self.card.pack(padx=40, pady=30, fill="both", expand=True)

        title = tk.Label(
            self.card,
            textvariable=self.title_var,
            font=FONTS["header"],
            bg=COLORS["card"],
            fg=COLORS["text"],
        )
        title.pack(pady=(18, 10))

        self.theory_frame = tk.Frame(self.card, bg=COLORS["card"])
        self.theory_frame.pack(fill="both", expand=True)

        self.content_label = tk.Label(
            self.theory_frame,
            textvariable=self.content_var,
            font=FONTS["body"],
            wraplength=WRAP,
            justify="left",
            bg=COLORS["card"],
            fg=COLORS["text"],
        )
        self.content_label.pack(padx=30, pady=10)

        self.next_button = make_button(self.theory_frame, text="Далее", command=self.next_theory_page)
        self.next_button.pack(pady=12)

        self.practice_frame = tk.Frame(self.card, bg=COLORS["card"])

        self.practice_title_var = tk.StringVar()
        self.practice_title = tk.Label(
            self.practice_frame,
            textvariable=self.practice_title_var,
            font=FONTS["section"],
            bg=COLORS["card"],
            fg=COLORS["text"],
        )
        self.practice_title.pack(pady=(10, 10))

        self.practice_prompt_var = tk.StringVar()
        self.practice_prompt = tk.Label(
            self.practice_frame,
            textvariable=self.practice_prompt_var,
            font=FONTS["body"],
            wraplength=WRAP,
            justify="left",
            bg=COLORS["card"],
            fg=COLORS["text"],
        )
        self.practice_prompt.pack(padx=30, pady=10)

        self.practice_entry_var = tk.StringVar()
        self.practice_entry = tk.Entry(self.practice_frame, textvariable=self.practice_entry_var, width=30)
        style_entry(self.practice_entry)
        self.practice_entry.pack(pady=8)

        self.practice_feedback_var = tk.StringVar()
        self.practice_feedback = tk.Label(
            self.practice_frame,
            textvariable=self.practice_feedback_var,
            font=FONTS["body_bold"],
            wraplength=WRAP,
            justify="left",
            bg=COLORS["card"],
            fg=COLORS["muted"],
        )
        self.practice_feedback.pack(pady=(6, 4))

        self.practice_explain_var = tk.StringVar()
        self.practice_explain = tk.Label(
            self.practice_frame,
            textvariable=self.practice_explain_var,
            font=FONTS["small"],
            wraplength=WRAP,
            justify="left",
            bg=COLORS["card"],
            fg=COLORS["muted"],
        )
        self.practice_explain.pack(pady=(0, 10))

        self.practice_button_frame = tk.Frame(self.practice_frame, bg=COLORS["card"])
        self.practice_button_frame.pack(pady=10)

        self.practice_check_button = make_button(
            self.practice_button_frame, text="Проверить", command=self.check_practice
        )
        self.practice_check_button.grid(row=0, column=0, padx=6)

        self.practice_next_button = make_button(
            self.practice_button_frame,
            text="Следующее задание",
            command=self.next_practice,
            variant="secondary",
        )
        self.practice_finish_button = make_button(
            self.practice_button_frame,
            text="Завершить тему",
            command=self.finish_practice,
        )

        self.menu_button = make_button(self.card, text="В меню", command=controller.show_menu, variant="ghost")
        self.menu_button.pack(pady=14)

    def start_lesson(self, lesson_id):
        self.lesson_id = lesson_id
        self.lesson = LESSONS[lesson_id]
        self.page_index = 0
        self.practice_index = 0
        self.show_theory_page()

    def show_theory_page(self):
        self.practice_frame.pack_forget()
        self.theory_frame.pack(fill="both", expand=True)
        self.title_var.set(self.lesson["title"])
        self.content_var.set(self.lesson["theory"][self.page_index])
        if self.page_index < len(self.lesson["theory"]) - 1:
            self.next_button.config(text="Далее", command=self.next_theory_page)
        else:
            self.next_button.config(text="Перейти к практике", command=self.start_practice)

    def next_theory_page(self):
        self.page_index += 1
        self.show_theory_page()

    def start_practice(self):
        self.practice_index = 0
        self.show_practice_task()

    def show_practice_task(self):
        self.theory_frame.pack_forget()
        self.practice_frame.pack(fill="both", expand=True)
        total = len(self.lesson["practice"])
        self.practice_title_var.set(f"Практика: задание {self.practice_index + 1} из {total}")
        task = self.lesson["practice"][self.practice_index]
        self.practice_prompt_var.set(task["prompt"])
        self.practice_entry_var.set("")
        self.practice_entry.config(state="normal")
        self.practice_entry.focus_set()
        self.practice_feedback_var.set("")
        self.practice_feedback.config(fg=COLORS["muted"])
        self.practice_explain_var.set("")
        self.practice_check_button.config(state="normal")
        self.practice_next_button.grid_forget()
        self.practice_finish_button.grid_forget()

    def check_practice(self):
        task = self.lesson["practice"][self.practice_index]
        is_valid, is_correct, error_msg = evaluate_task(task, self.practice_entry_var.get())
        if not is_valid:
            self.practice_feedback_var.set(error_msg)
            self.practice_feedback.config(fg=COLORS["danger"])
            self.practice_explain_var.set("")
            return

        self.practice_entry.config(state="disabled")
        self.practice_check_button.config(state="disabled")
        if is_correct:
            self.practice_feedback_var.set("Верно!")
            self.practice_feedback.config(fg=COLORS["success"])
            self.practice_explain_var.set(task["explain"])
        else:
            self.practice_feedback_var.set(f"Неверно. Правильный ответ: {task['answer']}.")
            self.practice_feedback.config(fg=COLORS["danger"])
            self.practice_explain_var.set(task["explain"])

        if self.practice_index >= len(self.lesson["practice"]) - 1:
            self.practice_finish_button.grid(row=0, column=1, padx=6)
        else:
            self.practice_next_button.grid(row=0, column=1, padx=6)

    def next_practice(self):
        self.practice_index += 1
        self.show_practice_task()

    def finish_practice(self):
        self.controller.finish_lesson(self.lesson_id)


class GameFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=COLORS["bg"])
        self.controller = controller
        self.questions = []
        self.index = 0
        self.score = 0

        self.card = tk.Frame(
            self,
            bg=COLORS["card"],
            highlightthickness=1,
            highlightbackground=COLORS["border"],
        )
        self.card.pack(padx=40, pady=30, fill="both", expand=True)

        self.title_var = tk.StringVar(value="Мини-игра: проверка знаний")
        tk.Label(
            self.card,
            textvariable=self.title_var,
            font=FONTS["header"],
            bg=COLORS["card"],
            fg=COLORS["text"],
        ).pack(pady=(18, 5))

        self.progress_var = tk.StringVar()
        tk.Label(
            self.card,
            textvariable=self.progress_var,
            font=FONTS["body"],
            bg=COLORS["card"],
            fg=COLORS["muted"],
        ).pack(pady=(0, 10))

        self.prompt_var = tk.StringVar()
        self.prompt_label = tk.Label(
            self.card,
            textvariable=self.prompt_var,
            font=FONTS["body"],
            wraplength=WRAP,
            justify="left",
            bg=COLORS["card"],
            fg=COLORS["text"],
        )
        self.prompt_label.pack(padx=30, pady=(5, 10))

        self.mcq_frame = tk.Frame(self.card, bg=COLORS["card"])
        self.choice_var = tk.IntVar(value=-1)
        self.option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(
                self.mcq_frame,
                text="",
                variable=self.choice_var,
                value=i,
                font=FONTS["body"],
                anchor="w",
                justify="left",
                wraplength=WRAP,
                bg=COLORS["card"],
                fg=COLORS["text"],
                activebackground=COLORS["card"],
                activeforeground=COLORS["text"],
                selectcolor=COLORS["card"],
            )
            btn.pack(fill="x", padx=40, pady=2)
            self.option_buttons.append(btn)

        self.input_frame = tk.Frame(self.card, bg=COLORS["card"])
        self.input_var = tk.StringVar()
        self.input_entry = tk.Entry(self.input_frame, textvariable=self.input_var, width=30)
        style_entry(self.input_entry)
        self.input_entry.pack(pady=6)

        self.feedback_var = tk.StringVar()
        self.feedback_label = tk.Label(
            self.card,
            textvariable=self.feedback_var,
            font=FONTS["body_bold"],
            wraplength=WRAP,
            justify="left",
            bg=COLORS["card"],
            fg=COLORS["muted"],
        )
        self.feedback_label.pack(pady=(10, 4))

        self.explain_var = tk.StringVar()
        self.explain_label = tk.Label(
            self.card,
            textvariable=self.explain_var,
            font=FONTS["small"],
            wraplength=WRAP,
            justify="left",
            bg=COLORS["card"],
            fg=COLORS["muted"],
        )
        self.explain_label.pack(pady=(0, 10))

        self.button_frame = tk.Frame(self.card, bg=COLORS["card"])
        self.button_frame.pack(pady=10)

        self.check_button = make_button(self.button_frame, text="Ответить", command=self.check_answer)
        self.check_button.grid(row=0, column=0, padx=6)

        self.next_button = make_button(
            self.button_frame, text="Следующий вопрос", command=self.next_question, variant="secondary"
        )
        self.next_button.grid(row=0, column=1, padx=6)

        make_button(self.card, text="В меню", command=controller.show_menu, variant="ghost").pack(pady=10)

    def start_game(self):
        total = min(8, len(QUESTION_BANK))
        self.questions = random.sample(QUESTION_BANK, k=total)
        self.index = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        question = self.questions[self.index]
        total = len(self.questions)
        self.progress_var.set(f"Вопрос {self.index + 1} из {total}")
        self.prompt_var.set(question["prompt"])
        self.feedback_var.set("")
        self.feedback_label.config(fg=COLORS["muted"])
        self.explain_var.set("")
        self.next_button.config(state="disabled")
        self.check_button.config(state="normal")

        if question["type"] == "mcq":
            self.input_frame.pack_forget()
            self.mcq_frame.pack(pady=6)
            self.choice_var.set(-1)
            for i, btn in enumerate(self.option_buttons):
                if i < len(question["options"]):
                    btn.config(text=question["options"][i], state="normal")
                    btn.pack_configure(pady=2)
                else:
                    btn.config(text="", state="disabled")
        else:
            self.mcq_frame.pack_forget()
            self.input_frame.pack(pady=6)
            self.input_var.set("")
            self.input_entry.config(state="normal")
            self.input_entry.focus_set()

    def check_answer(self):
        question = self.questions[self.index]
        if question["type"] == "mcq":
            choice = self.choice_var.get()
            if choice < 0:
                self.feedback_var.set("Выберите вариант ответа.")
                self.feedback_label.config(fg=COLORS["danger"])
                self.explain_var.set("")
                return
            is_correct = choice == question["answer_index"]
        else:
            is_valid, is_correct, error_msg = evaluate_task(question, self.input_var.get())
            if not is_valid:
                self.feedback_var.set(error_msg)
                self.feedback_label.config(fg=COLORS["danger"])
                self.explain_var.set("")
                return
            self.input_entry.config(state="disabled")

        if is_correct:
            self.score += 1
            self.feedback_var.set("Верно!")
            self.feedback_label.config(fg=COLORS["success"])
        else:
            if question["type"] == "mcq":
                correct = question["options"][question["answer_index"]]
            else:
                correct = question["answer"]
            self.feedback_var.set(f"Неверно. Правильный ответ: {correct}.")
            self.feedback_label.config(fg=COLORS["danger"])

        self.explain_var.set(question.get("explain", ""))
        self.check_button.config(state="disabled")
        self.next_button.config(state="normal")

    def next_question(self):
        if self.index >= len(self.questions) - 1:
            self.controller.show_result(self.score, len(self.questions))
            return
        self.index += 1
        self.show_question()


class ResultFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=COLORS["bg"])
        self.controller = controller
        self.result_var = tk.StringVar()
        self.comment_var = tk.StringVar()

        self.card = tk.Frame(
            self,
            bg=COLORS["card"],
            highlightthickness=1,
            highlightbackground=COLORS["border"],
        )
        self.card.pack(padx=40, pady=30, fill="both", expand=True)

        tk.Label(
            self.card,
            text="Итог мини-игры",
            font=FONTS["header"],
            bg=COLORS["card"],
            fg=COLORS["text"],
        ).pack(pady=(18, 10))
        tk.Label(
            self.card,
            textvariable=self.result_var,
            font=FONTS["section"],
            bg=COLORS["card"],
            fg=COLORS["text"],
        ).pack(pady=6)
        tk.Label(
            self.card,
            textvariable=self.comment_var,
            font=FONTS["body"],
            wraplength=WRAP,
            bg=COLORS["card"],
            fg=COLORS["muted"],
        ).pack(pady=6)

        btn_frame = tk.Frame(self.card, bg=COLORS["card"])
        btn_frame.pack(pady=20)

        make_button(btn_frame, text="Сыграть еще раз", width=22, command=controller.show_game).grid(
            row=0, column=0, padx=6
        )
        make_button(
            btn_frame, text="В меню", width=22, command=controller.show_menu, variant="secondary"
        ).grid(row=0, column=1, padx=6)

    def set_result(self, score, total):
        self.result_var.set(f"Ваш результат: {score} из {total}")
        if total == 0:
            comment = "Нет вопросов для оценки."
        else:
            ratio = score / total
            if ratio >= 0.8:
                comment = "Отлично! Вы уверенно владеете материалом."
            elif ratio >= 0.5:
                comment = "Хорошо! Повторите сложные моменты и попробуйте снова."
            else:
                comment = "Нужно повторить обе темы и еще раз пройти практику."
        self.comment_var.set(comment)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry(WINDOW_SIZE)
        self.minsize(820, 600)
        self.configure(bg=COLORS["bg"])

        self.lessons_done = {lesson_id: False for lesson_id in LESSON_ORDER}

        container = tk.Frame(self, bg=COLORS["bg"])
        container.pack(fill="both", expand=True)

        self.frames = {}
        for frame_cls in (MenuFrame, LessonFrame, GameFrame, ResultFrame):
            frame = frame_cls(container, self)
            self.frames[frame_cls.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.show_menu()

    def all_lessons_done(self):
        return all(self.lessons_done.values())

    def show_menu(self):
        frame = self.frames["MenuFrame"]
        frame.refresh()
        frame.tkraise()

    def show_lesson(self, lesson_id):
        frame = self.frames["LessonFrame"]
        frame.start_lesson(lesson_id)
        frame.tkraise()

    def finish_lesson(self, lesson_id):
        self.lessons_done[lesson_id] = True
        messagebox.showinfo("Тема завершена", "Тема пройдена! Можно перейти в меню.")
        self.show_menu()

    def show_game(self):
        if not self.all_lessons_done():
            messagebox.showinfo(
                "Сначала обучение",
                "Чтобы открыть мини-игру, нужно пройти обе темы.",
            )
            self.show_menu()
            return
        frame = self.frames["GameFrame"]
        frame.start_game()
        frame.tkraise()

    def show_result(self, score, total):
        frame = self.frames["ResultFrame"]
        frame.set_result(score, total)
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()
