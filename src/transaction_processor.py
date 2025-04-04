import re
from collections import Counter
from typing import List, Dict

def search_operations_by_description(transactions: List[Dict[str, str]], search_string: str) -> List[Dict[str, str]]:
    """
    Возвращает список операций, в описании которых содержится заданная строка.
    """
    pattern = re.compile(search_string, re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get('description', ''))]

def count_operations_by_category(transactions: List[Dict[str, str]], categories: List[str]) -> Dict[str, int]:
    """
    Возвращает словарь с количеством операций в каждой категории.
    """
    category_counts = Counter(transaction['description'] for transaction in transactions if transaction['description'] in categories)
    return dict(category_counts)