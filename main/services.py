from typing import Dict, List


def load_ad_platforms(file_content: str) -> Dict[str, List[str]]:
    """
    Загружает данные о рекламных площадках из строки и возвращает словарь,
    где ключ — это локация, а значение — список рекламных площадок.

    :param file_content: Строка с данными о рекламных площадках.
    :return: Словарь с локациями и их рекламными площадками.
    """
    ad_platforms = {}

    # Разделяем входные данные на строки
    lines = file_content.splitlines()

    for line in lines:
        # Удаляем лишние пробелы в начале и конце строки
        line = line.strip()

        # Пропускаем пустые строки
        if not line:
            continue

        # Разделяем строку на платформу и локации
        if ':' not in line:
            print(f"Некорректная строка: '{line}'. Пропускаем.")
            continue

        platform, locations_str = line.split(':', 1)  # Разделяем только по первому ':'

        # Удаляем лишние пробелы у платформы
        platform = platform.strip()

        # Разделяем локации и удаляем лишние пробелы
        locations = [loc.strip() for loc in locations_str.split(',')]

        # Добавляем данные в словарь
        for loc in locations:
            if not loc:  # Пропускаем пустые локации
                continue
            if loc not in ad_platforms:
                ad_platforms[loc] = []
            ad_platforms[loc].append(platform)

    return ad_platforms


def search_ad_platforms(ad_platforms: Dict[str, List[str]], location: str) -> List[str]:
    platforms = set()
    for loc in ad_platforms:
        if location.startswith(loc):
            platforms.update(ad_platforms[loc])
    return list(platforms)
