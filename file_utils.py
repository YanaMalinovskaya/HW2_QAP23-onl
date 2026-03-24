#4.Напиши модуль file_utils.py с тремя полностью аннотированными функциями:

#def read_lines(filename): ...
#def write_lines(filename, lines): ...
#def count_words(filename): ... # count_words считает сколько раз каждое слово встречается в файле 
# и возвращает словарь. 
#В main.py импортируй и протестируй все три.

def read_lines(filename: str) -> list[str]:
    """Читает файл и возвращает список строк."""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.readlines()

def write_lines(filename: str, lines: list[str]) -> None:
    """Записывает список строк в файл."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(line if line.endswith('\n') else line + '\n' for line in lines)

def count_words(filename: str) -> dict[str, int]:
    """Считает количество вхождений каждого слова в файле."""
    word_count = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            words = line.lower().split()
            for word in words:
                clean_word = word.strip('.,!?;:"()')
                if clean_word:
                    word_count[clean_word] = word_count.get(clean_word, 0) + 1
    return word_count
