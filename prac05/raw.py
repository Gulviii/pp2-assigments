import re
import json

text = """(осында чек мәтінін қой)"""

# Бағалар
prices = re.findall(r'\d[\d\s]*,\d{2}', text)

# Өнім атаулары (жол басында сан және нүктеден кейінгі жол)
products = re.findall(r'\d+\.\s*\n(.+)', text)

# Жалпы сома
total_match = re.search(r'ИТОГО:\s*([\d\s,]+)', text)
total = total_match.group(1).strip() if total_match else None

# Күні мен уақыты
datetime_match = re.search(r'Время:\s*([\d.]+\s[\d:]+)', text)
datetime_info = datetime_match.group(1) if datetime_match else None

# Төлем әдісі
payment_match = re.search(r'Банковская карта|Наличные', text)
payment_method = payment_match.group(0) if payment_match else None

# Құрылымдалған нәтиже
receipt = {
    "products": products,
    "prices": prices,
    "total": total,
    "datetime": datetime_info,
    "payment_method": payment_method
}

print(json.dumps(receipt, ensure_ascii=False, indent=2))
