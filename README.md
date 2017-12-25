# <center> Краскал - кластеризация </center>

Для кластерицации объектов, построим алгоритмом Краскала - мин ост лес. Количество кластеров выбирает эксперт.
Алгоритм Мин Ост Дерева описан [здесь]( http://e-maxx.ru/algo/mst_kruskal)
По нижеприведенным графикам мы можем оценить на сколько "хорошо" эксперт выбрал кол-во кластеров. 

###### Пример работы программы:

<figure>
  <img src="https://raw.githubusercontent.com/okiochan/Kruskal/master/niice.png" alt="uniform"/>
</figure>

Выберем, к примеру, 1 кластер (Краскал даст просто Мин Ост дерево)
<figure>
  <img src="https://raw.githubusercontent.com/okiochan/Kruskal/master/11.png" alt="uniform"/>
</figure>

Мы видим, что на графике большой скачок - это мы взяли тяжелое ребро
<figure>
  <img src="https://raw.githubusercontent.com/okiochan/Kruskal/master/1.png" alt="uniform"/>
</figure>

###### Пример для 3х кластеров:
<figure>
  <img src="https://raw.githubusercontent.com/okiochan/Kruskal/master/31.png" alt="uniform"/>
  <img src="https://raw.githubusercontent.com/okiochan/Kruskal/master/3.png" alt="uniform"/>
</figure>

###### Пример для 5х кластеров:
<figure>
  <img src="https://raw.githubusercontent.com/okiochan/Kruskal/master/51.png" alt="uniform"/>
  <img src="https://raw.githubusercontent.com/okiochan/Kruskal/master/5.png" alt="uniform"/>
</figure>

###### Пример для 10х кластеров:
<figure>
  <img src="https://raw.githubusercontent.com/okiochan/Kruskal/master/101.png" alt="uniform"/>
  <img src="https://raw.githubusercontent.com/okiochan/Kruskal/master/10.png" alt="uniform"/>
</figure>


код программы [здесь]( https://github.com/okiochan/Kruskal/blob/master/kruskal.py)
