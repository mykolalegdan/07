class ArrayQueue:
    def __init__(self, capacity=13):
        self.capacity = capacity
        self.data = [None] * capacity  # Масив фіксованого розміру
        self.head = 0  # Індекс початку (звідси видаляємо)
        self.tail = 0  # Індекс кінця (сюди додаємо)[cite: 1, 2]
        self.count = 0  # Кількість елементів у черзі

    # Додавання елемента в чергу
    def enqueue(self, item):
        if self.count == self.capacity:
            print("Черга переповнена!")
            return
        self.data[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity  # Перехід на наступну комірку
        self.count += 1

    # Видалення та повернення елемента з черги[cite: 1, 3]
    def dequeue(self):
        if self.count == 0:
            print("Черга порожня!")
            return None
        removed_item = self.data[self.head]
        self.head = (self.head + 1) % self.capacity  # Пересуваємо head
        self.count -= 1
        return removed_item

    # Повертає кількість елементів
    def size(self):
        return self.count

    # Вивід елементів черги
    def print_queue(self):
        elements = []
        for i in range(self.count):
            index = (self.head + i) % self.capacity
            elements.append(str(self.data[index]))
        print("Черга:", " -> ".join(elements))


# Перевірка роботи
queue = ArrayQueue()

# Додаємо елементи згідно з прикладом з методички (6, 4, 6, 2, 7)[cite: 2]
queue.enqueue(6)
queue.enqueue(4)
queue.enqueue(6)
queue.enqueue(2)
queue.enqueue(7)

queue.print_queue()  # Виведе: Черга: 6 -> 4 -> 6 -> 2 -> 7
print("Кількість:", queue.size())  # Виведе: Кількість: 5[cite: 3]

print("Видалено:", queue.dequeue())  # Виведе: Видалено: 6[cite: 1, 3]
queue.print_queue()  # Виведе: Черга: 4 -> 6 -> 2 -> 7
print("Кількість:", queue.size())  # Виведе: Кількість: 4[cite: 3]