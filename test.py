import pandas as pd

with open('gg.csv') as file:
    df = pd.read_csv(file)
    df_sorted = df.sort_values(by='diametr (micrometer)')
    print(df_sorted.iloc[:,0])

    # Заданный диапазон и шаг
    lower_bound = int(df_sorted.iloc[0,0])
    upper_bound = int(df_sorted.iloc[-1,0])
    print(upper_bound)
    step = 100

    # Пример: Считаем количество значений, попадающих в диапазоны [10, 15), [15, 20), [20, 25), [25, 30)
    ranges = list(range(lower_bound, upper_bound + step, step))  # Диапазоны с шагом

    # Создаём пустой список для хранения количества значений в каждом диапазоне
    counts = []

    # Для каждого диапазона считаем количество значений, которые в него входят
    for i in range(len(ranges) - 1):
        count = df[(df['diametr (micrometer)'] >= ranges[i]) & (df['diametr (micrometer)'] < ranges[i + 1])].shape[0]
        counts.append(count)

    # Выводим результат
    for i in range(len(counts)):
        print(f"Диапазон [{ranges[i]}, {ranges[i + 1]}): {counts[i]} значений")
