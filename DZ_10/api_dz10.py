import pandas as pd
import json
import seaborn as sns
import matplotlib.pyplot as plt


with open('events.json', 'r') as file:
    data = json.load(file)
    df = pd.DataFrame(data['events'])
print(df)

all_fin_signatures: list = list()
for elem in df['signature']:
    all_fin_signatures.append(elem)

unique_signatures = set(all_fin_signatures)
print('\n Уникальные значения сигнатур:')
for value in unique_signatures:
    print(value)



# Визуализация через matplotlib
counts = df['signature'].value_counts()
plt.figure(figsize=(12, 8))
counts.plot(kind='bar')
plt.title('Event Signatures Frequency')
plt.ylabel('Count')
plt.xlabel('Signature Name')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Визуализация через matplotlib и seaborn
# plt.figure(figsize=(10, 6))
# sns.countplot(data=df, x="signature")
#
# plt.title("Распределение типов событий безопасности")
# plt.xticks(rotation=90)  # Поворот подписей оси X для лучшей читаемости
# plt.show()


# удаление дубликатов, если необходимо
# удаляем дубликаты id
# df.drop_duplicates(subset='id', inplace=True)

# замена пустых строк Nan
# df.replace({'': pd.NA, 'null': pd.NA, None: pd.NA}, inplace=True)

# удаление строк с пустыми значениями timestamp или events
# df.dropna(subset=['timestamp', 'event'], inplace=True)

# конвертаяиц timestamp в формат datetime
# df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

# замена пропущенных знаачений в users на 'unknown'
# df['user'].fillna('unkniwn', inplace=True)

# print(df)
