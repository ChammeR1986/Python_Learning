def display_first_ten_chars(value):
    # Преобразуем значение в строку на всякий случай (если это число, например)
    value_str = str(value)

    # Срез [:10] всегда безопасно возвращает первые 10 символов
    truncated_value = value_str[:10]

    # Простая проверка для красоты вывода
    if len(value_str) > 10:
        print(f"Обрезано: {truncated_value}...")
    else:
        print(f"Полностью: {truncated_value}")


# --- Примеры использования ---
display_first_ten_chars("Международная")  # Длинное слово
display_first_ten_chars("Привет")  # Короткое слово
display_first_ten_chars(12345678901234)  # Число
