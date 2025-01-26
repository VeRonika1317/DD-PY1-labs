# TODO Напишите функцию find_common_participants

def find_common_participants(first_group, second_group, s=','):

    participants1 = set(first_group.split(s))
    participants2 = set(second_group.split(s))

    common_participants = participants1.intersection(participants2)

    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common = find_common_participants(participants_first_group, participants_second_group,  s='|')
print(common)

# TODO Провеьте работу функции с разделителем отличным от запятой

participants_first_group2 = "Иванов,Петров,Сидоров"
participants_second_group2 = "Петров,Сидоров,Смирнов"
common2 = find_common_participants(participants_first_group2, participants_second_group2,  s=',')
print(common2)
