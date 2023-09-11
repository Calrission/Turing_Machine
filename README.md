# Turing_Machine
В 1936 г. Аланом Тьюрингом для уточнения понятия алгоритма был предложен абстрактный универсальный исполнитель. Его абстрактность заключается в том, что он представляет собой логическую вычислительную конструкцию, а не реальную вычислительную машину. Термин «универсальный исполнитель» говорит о том, что данный исполнитель может имитировать любой другой исполнитель. Например, операции, которые выполняют реальные вычислительные машины можно имитировать на универсальном исполнителе. В последствие, придуманная Тьюрингом вычислительная конструкция была названа машиной Тьюринга.
Описание машины Тьюринга#
Объяснение описания машины Тьюринга#
Машина Тьюринга представляет собой устройство, содержащее пишущую ленту бесконечной длины, разбитую на ячейки а1, а2, …, аn,… . В каждой ячейке может быть записан один и только один символ из входного алфавита машины Тьюринга.

![Тьюринг_лента](https://github.com/EvgenieLebedev/Turing_Machine/assets/92586907/e933960f-18a1-418e-b7b2-1b0f9b86e969)

В начальный момент на ленту записывается какое-то слово. Обычно это слово представляет собой описание некоторой задачи, на которых специализируется данная машина Тьюринга. Кроме ленты, у машины имеется читающая-пишущая головка, которая позволяется считать символ из ячейки или записать в ячейку, непосредственно находящуюся под головкой, какой-то один символ. Машина Тьюринга работает по тактам. Такты машины Тьюринга никак не привязываются к единицам времени, например, секундам. Но именно в тактах измеряется “время”, затрачиваемое машиной Тьюринга на то, чтобы выполнить обработку входного слова. Разумно и сложность задачи связывать с числом тактов, которую необходимо затратить на Машине Тьюринга для ее решения.

Управляющее устройство работает согласно правилам перехода, которые представляют алгоритм, реализуемый данной машиной Тьюринга. Каждое правило перехода предписывает машине, в зависимости от текущего состояния и наблюдаемого в текущей клетке символа, записать в эту клетку новый символ, перейти в новое состояние и переместиться на одну клетку влево или вправо. Некоторые состояния машины Тьюринга могут быть помечены как терминальные, и переход в любое из них означает конец работы, остановку алгоритма.

## Интерфейс программы
Лента машины представлена серым прямоугольником (изначально пустая)
Для отображения положения головки на лентие используется символ: **[]** 
Состояние машины отображается под лентой (q0 - начальное состояние)
Перемещение головки в ручном режиме осуществляется кнопками: ← и →
Запись 1,0 и _ осуществляется соотвествующими кнопками
Кнопка "Сброс" осуществляется возвращение в начальное состояние
"Стереть" позволяет удалить символ, который находится под головкой
Загрузка длинных последовательностей символов осуществляется при помлщи пользовательского интерфейса и кнопки "Загрузить на ленту"

![интерфейс](https://github.com/EvgenieLebedev/Turing_Machine/assets/92586907/28eedad7-0ae4-4eac-9205-52957e98a67d)

Таблица переходов хранит инструкции по последовательной смене состояний
Для описания необходимо нажать на кнопку "Добавить правило" и ввести 5 параметров : 
Текущее состояние, символ под головкой, новый символ, действие (сдвиг вправо - R, сдвиг влево - L, остаться на месте - S), новое состояние машины

![image](https://github.com/EvgenieLebedev/Turing_Machine/assets/92586907/6d4dbe92-3982-43bf-9d4b-ee8e9d177750)

Загрузка таблиц осуществляется из формата .txt  
Пример данных:

q0 0 _ R q0 


## Демонстрация

Рассматривается пример AND.TXT (функция логического И для 2 переменных. Входные данные: A_B__ , где A, B ∈ {0, 1} ) и пример ERASE (удаление всех символов в строке)

![Машина Тьюринга 2023-09-11 20-03-10 (online-video-cutter com)](https://github.com/EvgenieLebedev/Turing_Machine/assets/92586907/9358c140-cf3d-46c4-af72-f9e67a419472)


