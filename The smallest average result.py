def smallest_average(person1, person2, person3):
    def average(person):
        return (person["result1"] + person["result2"] + person["result3"]) / 3

    avg1 = average(person1)
    avg2 = average(person2)
    avg3 = average(person3)

    if avg1 < avg2 and avg1 < avg3:
        return person1
    elif avg2 < avg1 and avg2 < avg3:
        return person2
    else:
        return person3


person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

print(smallest_average(person1, person2, person3))
