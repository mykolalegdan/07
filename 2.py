# Клас одного вузла[cite: 2]
class Node:
    def __init__(self, data):
        self.data = data  # Значення[cite: 2]
        self.next = None  # Посилання на наступний вузол[cite: 2]


class LinkedListQueue:
    def __init__(self):
        self.head = None  # Початок черги[cite: 2]
        self.tail = None  # Кінець черги[cite: 2]
        self.count = 0  # Кількість елементів[cite: 3]

    # Додавання елемента[cite: 3]
    def enqueue(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Старий tail вказує на новий вузол[cite: 2, 3]
            self.tail = new_node  # Оновлюємо tail[cite: 2]
        self.count += 1

    # Видалення елемента[cite: 3]
    def dequeue(self):
        if self.head is None:
            print("Черга порожня!")
            return None
        removed_data = self.head.data
        self.head = self.head.next  # Пересуваємо head на наступний вузол[cite: 2]
        self.count -= 1
        if self.head is None:
            self.tail = None
        return removed_data

    # Повертає кількість елементів[cite: 3]
    def size(self):
        return self.count

    # Вивід усіх елементів[cite: 3]
    def print_queue(self):
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print("Черга:", " -> ".join(elements))


# Перевірка роботи
node_queue = LinkedListQueue()

# Додаємо елементи згідно з прикладом з методички (12, 25, 8)[cite: 2]
node_queue.enqueue(12)
node_queue.enqueue(25)
node_queue.enqueue(8)

node_queue.print_queue()  # Виведе: Черга: 12 -> 25 -> 8
print("Кількість:", node_queue.size())  # Виведе: Кількість: 3[cite: 3]

print("Видалено:", node_queue.dequeue())  # Виведе: Видалено: 12[cite: 1, 3]
node_queue.print_queue()  # Виведе: Черга: 25 -> 8
print("Кількість:", node_queue.size())  # Виведе: Кількість: 2[cite: 3]