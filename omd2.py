import csv


def reading() -> list[dict]:
    with open("Corp_Summary.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        data = []
        for row in reader:
            row["Оклад"] = int(row["Оклад"])
            row["Оценка"] = float(row["Оценка"])
            data.append(row)
        return data


def variant1(data: list[dict]) -> None:
    result = {}
    for employee in data:
        department = employee["Департамент"]
        team = employee["Отдел"]
        if department not in result:
            result[department] = []
        if team not in result[department]:
            result[department].append(team)

    for department in sorted(result):
        print(f"департамент: {department}")
        for team in sorted(result[department]):
            print(team)


def department_data(data: list[dict]) -> dict:
    result = {}
    for employee in data:
        department = employee["Департамент"]
        salary = employee["Оклад"]
        if department not in result:
            result[department] = {
                "count": 0, "min": salary, "max": salary, "total": 0
            }
        s = result[department]
        s["count"] += 1
        s["total"] += salary
        if salary < s["min"]:
            s["min"] = salary
        if salary > s["max"]:
            s["max"] = salary
    for s in result.values():
        s["avg"] = s["total"] / s["count"]
    return result


def variant2(data: list[dict]) -> None:
    x = department_data(data)
    print("департамент кол-во мин макс средняя")
    for department in sorted(x):
        s = x[department]
        print(
            f"{department} {s['count']} {s['min']} "
            f"{s['max']} {s['avg']:.1f}"
        )


def variant3(data: list[dict]) -> None:
    x = department_data(data)
    with open("department_data.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow([
            "Департамент", "Количество человек", "Минимальная зарплата",
            "Максимальная зарплата", "Средняя зарплата"
        ])
        for department in sorted(x):
            d = x[department]
            writer.writerow([
                department, d["count"], d["min"], d["max"], round(d["avg"], 1)
            ])


def main(variant: int) -> None:
    data = reading()
    if variant == 1:
        variant1(data)
    elif variant == 2:
        variant2(data)
    elif variant == 3:
        variant3(data)


if __name__ == "__main__":
    user_variant = int(input("номер варианта: "))
    main(user_variant)
