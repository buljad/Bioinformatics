import subprocess
import re

# Путь к файлу BAM
file = "alignment_sorted.bam"

# Запуск команды samtools flagstat и получение вывода
result = subprocess.run(['samtools', 'flagstat', file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Проверяем, был ли успешный вывод
if result.returncode != 0:
    print("Ошибка при выполнении команды samtools flagstat:")
    print(result.stderr)
    exit(1)

# Печатаем вывод для диагностики
print("Вывод команды flagstat:")
print(result.stdout)

# Извлекаем процент картированных ридов из вывода команды с дополнительными символами после процента
match = re.search(r'(\d+\.\d+)%', result.stdout)

if match:
    percent_mapped = float(match.group(1))
    print(f"Процент картированных ридов: {percent_mapped}%")
else:
    print("Ошибка: Процент картированных ридов не найден.")
    exit(1)

# Устанавливаем порог (например, 95% считается хорошим качеством)
threshold = 95.0

# Оценка качества картирования
if percent_mapped >= threshold:
    print(f"OK - Процент картированных ридов: {percent_mapped}%")
else:
    print(f"not OK - Процент картированных ридов: {percent_mapped}%")
