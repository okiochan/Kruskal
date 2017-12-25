# Kruskal

Для кластерицации объектов, построим алгоритмом Краскала - мин ост лес. Количество кластеров выбирает эксперт.
Алгоритм Мин Ост Дерева описан [здесь]( http://e-maxx.ru/algo/mst_kruskal)
По графику мф можем оценить на сколько "хорошо" эксперт выбрал кол-во кластеров. 

Выберем, к примеру, 1 кластер (Краскал даст просто Мин Ост дерево)
![](https://raw.githubusercontent.com/okiochan/Kruskal/master/11.png)

Мы видим, что на графике большой скачок - это мы взяли тяжелое ребро
![](https://raw.githubusercontent.com/okiochan/Kruskal/master/1.png)

Пример для 3х кластеров:
![](https://raw.githubusercontent.com/okiochan/Kruskal/master/3.png)
![](https://raw.githubusercontent.com/okiochan/Kruskal/master/31.png)

Пример для 5х кластеров:
![](https://raw.githubusercontent.com/okiochan/Kruskal/master/5.png)
![](https://raw.githubusercontent.com/okiochan/Kruskal/master/51.png)

Пример для 4х кластеров:
![](https://raw.githubusercontent.com/okiochan/Kruskal/master/10.png)
![](https://raw.githubusercontent.com/okiochan/Kruskal/master/101.png)