# Обзор методов фотограмметрии для задач 3D-сканирования зданий

Ключевые слова: фотограмметрия, реконструкция, стереофотограмметрия, SfM, TLS, RGB-D, LIDAR

## Аннотация

В настоящее время существуют разнообразные подходы к созданию трехмерной моделей. Фотограмметрия позволяет определить по снимкам исследуемого объекта его форму, размеры и пространственное положение в заданной системе координат. В частности, можно использовать фотограмметрию для процесса создания трехмерных моделей из нескольких изображений одного объекта, сфотографированного с разных углов. Большое разнообразие методов фотограмметрии объясняется различными подходами к решению проблемы трехмерной реконструкции здания и выбором оборудования. В работе были рассмотрены основные методы фотограмметрии (Structure from Motion, Terrestrial Laser Scanning, Стереофотограмметрия, Комбинированный SfM и TLS, Ортопроекции) и принципы их работы. Были выявлены проблемы, возникающие при трехмерной реконструкции зданий, какие ограничения накладывает поставленная задача. Выполнен сравнительный анализ методов фотограмметрии на основе сформированных критериев и выявленных проблем при сканировании зданий. На основе сравнительного анализа составляется классификация методов. Описаны рекомендации по процессу съемки зданий. 


## Введение

В настоящее время с развитием трехмерной графики возможность создавать трехмерные модели существующих объектов возросла многократно, в том числе и в архитектуре. Учитывая разнообразие сканируемых объектов, технологий и инструментов, появилось множество фотограмметрических методов трехмерной реконструкции объекта.

Объектом исследования данной статьи являются методы фотограмметрии для задач трехмерного сканирования зданий.
Цель статьи заключается в том, чтобы построить классификацию методов фотограмметрии для трехмерного сканирования зданий.

Для решения проблемы выбора конкретного метода фотограмметрии для задачи трехмерного сканирования зданий, возникающей из-за разнообразия существующих методов, необходимо решить следующие задачи:

1. Выявить проблемы, возникающие при трехмерной реконструкции зданий.
2. Рассмотреть существующие методы фотограмметрии и принципы их работы.
3. Сформировать критерии сравнения методов фотограмметрии.
4. Сравнительный анализ методов фотограмметрии на основе сформированных критериев и выявленных проблем при сканировании зданий.
5. Составить классификацию методов фотограмметрии на основе сравнительного анализа.

## Проблемы, возникающие при трехмерной реконструкции зданий

Используя фотограмметрию, можно создавать трехмерные модели практически любого объекта, если этот объект можно обхватить снимками камеры со всех сторон. Однако, учитывая разнообразие сканируемых объектов, технологий и инструментов, сложность сканирования объекта сильно варьируется в зависимости от выбранного метода и объекта.

Здание — наземное архитектурное строительное сооружение. Для создания полной модели необходимо запечатлеть здание со всех сторон, включая крышу. Однако в некоторых случаях без специального оборудования подручными методами это сделать практически невозможно. Чтобы это осуществить съемку крыши можно воспользоваться специальными беспилотным летательным аппаратом (UAV - Unmanned aerial vehicle), например квадрокоптер DJI Phantom 4, чтобы облететь здание со всех сторон, что ускорит процесс и даст возможность сфотографировать высоко расположенные или труднодоступные части здания [2].

Стоит отметить, что здания или ансамбли зданий являются большими объектами для человека по сравнению человеческим лицом [3] или растениями [4], над которыми тоже выполняются фотограмметрические работы, что влечет к большому количеству снимков и соответственно к большому объему занимаемой памяти и времени на их обработку, поэтому для работы с фотограмметрией потребуется компьютер с высокими характеристиками производительности.

Следующей важной особенностью процесса реконструкции зданий является тот факт, что здания расположены на улице в открытом пространстве. Влияние погодных условий при создании снимков имеет большое значение. Например, наличие солнечных бликов или дождя способно исказить работы алгоритмов, что напрямую влечет к увеличению неточности создаваемой модели.

# Сравнение методов

## Принцип отбора

Методы фотограмметрии выбирались на основе существующих видов камер и способов их использования. В обзоре участвуют методы, для которых репозитории с реализациями на GitHub имеют более 100 звезд. 

### Structure from Motion (SfM)

Structure from Motion (SfM) - это метод формирования изображения фотограмметрического диапазона для оценки и создания трехмерных моделей из последовательностей двумерных изображений. Биологическим примером работы SfM является тот факт, люди (и другие живые существа) могут восстанавливать трехмерную структуру из проецируемого двумерного поля движения объекта или сцены получаемого посредством зрения.

В простейшем случае пространственные координаты точек объекта определяются путём измерений, выполняемых по двум или более фотографиям, снятым из разных положений. При этом на каждом изображении отыскиваются общие точки (features), например алгоритмом SIFT. Затем луч зрения проводится от местоположения фотоаппарата до точки на объекте. Пересечение этих лучей и определяет расположение точки в пространстве. Найдя эти точки можно выстроить полную трехмерную модель объекта [5]. Пример построения нескольких восстановления нескольких точек представлен на рис. 1. [SfM Sample](image_sfm.png)

Для того, чтобы построить наиболее точную картину необходимо запечатлеть каждый участок объекта минимум два раза с разных ракурсов, то есть перекрытие изображений между собой должно быть как можно больше [6]. Хорошим случаем будет являться продольное перекрытие снимков примерно равное 60-80% [7].

### Стереофотограмметрия (Stereo photogrammetry)

По аналогии с SfM методом стереофотограмметрия пытается запечатлеть деталь объекта с разных сторон. В данном случае стереофотограмметрия подразумевает создание стереофотографии - 2 изображений (левое и правое). Согласно стереографическому принципу пара «стереоизображений» может просматриваться вместе, что создает пространственное (стереоскопическое) зрение. Этот эффект может быть использован для достижения выполнения трехмерного восстановления. Направления камеры должны быть почти параллельно друг другу для лучшего стереоскопического просмотра, как на рис. 2. Чтобы гарантировать хорошие результаты соотношение расстояния между камерами к расстоянию до объекта должно лежать между 1:5 и 1:15.
[Stereo scheme](image_stereo.png)

### Terrestrial laser scanning (TLS)

Наземное лазерное сканирование (TLS - Terrestrial laser scanning) - это наземный вариант использования сканера LIDAR, основанного на технологии получения и обработки информации об удалённых объектах с помощью активных оптических систем. Эти сканеры, изначально разработанные для моделирования архитектурных и инженерных сооружений, используются также для картографирования рельефа местности и ландшафта. Такие устройства в отличие от обычных фотоаппаратов способны запечатлеть трехмерное облако точек, тем самым упрощая процесс реконструкции [9]. По сравнению с TLS, фотограмметрическое решение является недорогим, так как такая система сбора данных требует всего лишь любое фотографирующее устройство, в отличие от TLS c более дорогими лазерными сканерами.
Отдельным направлением стоить отметить RGB-D камеры, которые могут создавать для каждого изображения карту глубины, то есть создавать трехмерное облако точек, например Kinect или Depth Camera D435i Intel RealSense, они более дешевые, чем LIDAR, но дороже, чем обычные фотоаппараты [10].

Важным моментом является процесс совмещения трехмерных облаков точек. Учитывая факт, что после каждого снимка камера выполняет смещение и/или поворот в пространстве, то необходимо совмещать облака точек, сделанные каждый в своей системе координат относительно камеры.

Одним из вариантов решения проблемы отслеживания изменения положения камеры - использование специальных внешних сенсоров (акселерометр, гироскоп, магнитометр), которые помогут отслеживать положение камеры. Часть RGB-D камер (Kinect, Depth Camera D435i Intel RealSense и другие) оснащены такими сенсорами, что позволяет использовать их для реконструкции объектов [10].

### Комбинирование SfM и TLS

Отдельно стоит отметить комбинирование фотограмметрического метода SfM для лазерных или RGB-D камер.
Точную трехмерную модель здания можно создать путем совмещения этих методов [11]. Перед тем как переходить к процессу трехмерного моделирования необходимо объединить оба облака точек в одну систему с использованием Helmet (7-parameter) transformation и алгоритма Iterative Closest Point (ICP), после чего скомбинированное облако точек использовать для реконструкции объекта [12]. Одним из главных преимуществу такого метода является высокая плотность точек из-за TLS и более полная растровая информация о точках из-за фотограмметрии.

### Ортопроекции

Самым простым способом реконструкции зданий, в частности создания упрощенной модели здания, является генерация ортопроекции фасадов зданий (SVR - Single View Reconstruction). Для создания такой модели понадобится всего по одной фотографии каждого фасада (стороны) здания. Данный способ подходит в случае, если для получаемой модели интересны только ее детали на ее сторонах (узоры, текстура, цвет и прочее) и не нужна точная форма объекта. Пример результата проецирования и исходного фото представлены на рис. 3. После создания ортопроекций (ортофото) данные снимки совмещаются в соответствии с геометрией здания. [Ortho](image_ortho.png)


## Критерии сравнения аналогов

### Стоимость оборудования

Стоимость оборудования зависит от количества и типа используемой камеры.
- Низкая - используется одна обычная фотокамера.
- Средняя - используется две обычные фотокамеры или стереокамера.
- Высокая - используется лазерная камера.

### Степень детализация модели

Детализация модели - степень схожести получаемой модели с реальным объектом.
- Низкая - минимальность детализации объекта, присутствуют только основные отличительные изгибы и формы здания, передана текстура здания.
- Высокая - получаемая модель сохраняет формы объекта, присутствуют все детали (узоры, текстура, цвет и прочее) фасадов.
- Очень высокая - большее количество точек модели, более правильная передача цвета

### Минимальное количество снимков каждой детали
Чем меньше требуется фотографий с разного ракурса, тем быстрее выполняется процесс фотографирования здания.

- При SfM рекомендуется сделать снимки как минимум с двух ракурсов, чтобы сопоставлять обнаруженные features.
- При стереофотограмметрии делается всего один стереоснимок детали, обеспечивая тем самым разный ракурс, в отличие от SfM, где нужно меняет ракурс камеры вручную и делать 2 снимка.
- При TLS - один снимок для каждой детали, объемность обеспечивается самой камерой
- При SfM и TLS - как и при SfM - 2 снимка.
- При ортопроекциях - один снимок каждого фасада (детали).

Результаты сравнения представлены в табл. 1.

## Таблица 1 - Сравнение методов по критериям
|   |  Стоимость оборудования | Детализация модели | Количество снимков каждой детали |
| --- | --- | --- | --- |
| SfM | Низкая | Высокая | 2 |
| Stereo | Средняя | Высокая | 1 |
| TLS | Высокая | Высокая | 1 |
| SfM и TLS | Высокая | Очень высокая | 2 |
| Ортопроекции | Низкая | Низкая | 1 |


## Выводы по итогам сравнения

Как видно из таблицы 1, у каждого метода есть свои сильные и слабые стороны.
В случае, если есть доступ к лазерной камере или RGB-D, то можно использовать комбинированный метод SfM и TLS для создания модели высокой точности.
В случае, если такой возможности нет, то для создания высоко детализированной модели подойдет метод SfM.

SfM и стереофотограмметрический метод очень схожи между собой, так как имеют один и тот же алгоритм создания модели. Разница между ними в количестве фотокамер, которая и объясняет потребность в создании дополнительного снимка для SfM метода.

Использования лазерной камеры или RGB-D обеспечивает высокую детализацию модели.

##  Выбор метода решения

Учитывая тот факт, что размеры зданий сильно варьируются, то для больших зданий необходимо делать большое количество снимков для создания полной трехмерной модели здания со всех сторон. Важным критерием при выборе метода является минимальное количество снимков каждой детали, так как при большом объеме данных потребуется большой объем памяти и большее время на обработку данных. Исходя из этого факта, метод ортопроекций отлично подходит для быстрого создания грубой модели здания.

Выбор конкретного метода реконструкции здания зависит от желаемого результата. В случае, если нужно составить высокоточную модель какой-либо архитектурной конструкции с высокой степенью детализации, то понадобятся трехмерные камеры. Если же нужна более простая модель, то можно в зависимости от бюджета использовать соответствующий фотограмметрический метод.

Отдельно стоит отметить влияние погодных условий на процесс съемки здания. Если выполнять съемку во время снегопада или дождя, то результаты могут быть хуже в сравнении с результатами при ясной погоде без осадков в случае фотограмметрических методов SfM и стереофотограмметрии. С большой вероятностью алгоритмы будут использовать падающие осадки в качестве ключевых точек. Учитывая, что в каждый момент времени выпадают хаотично одинаковые на внешний вид осадки, то отслеживать и сопоставлять их на фото практически невозможно и соответственно алгоритм будет выдавать неправильные результаты. С связи с этим стоит избегать использование данных алгоритмов в такую погоду.

Для высоких зданий, фотографирование крыши которых труднодоступно, необходимо использовать UAV. Существуют квадрокоптеры уже оснащенные камерой или имеют возможность крепления камеры. Однако стоит отметить, что большинство производителей квадрокоптеров предоставляет возможность установки только одной камеры, поэтому использовать стереометрическую систему из нескольких камер не предоставляется возможной.

## Рекомендации по процессу съемки

В виду особенностей реконструкции зданий стоит выделить следующие рекомендации по проведению процесса съемки:
- перемещение вокруг целевого объекта необходимо выполнять по кругу. Пример порядка съемки объекта предоставлен на рис. 5. [Pose](image_pose.png)

- перекрытие снимков. Важно, чтобы каждая часть модели была запечатлена как минимум на 2 изображения. Хорошим случаем будет являться продольное перекрытие снимков примерно равное 60-80%
- нужно избегать резких теней, использовать вспышку или снимать на улице в полумрачный день.
- объект должен составлять значительную часть каждого изображения, попадание других объектов в снимок влечет к их появлению на результирующей модели
- избегать движущихся объектов (например, автомобили, люди) [8] 
- наилучшими результатами будут обладать модели снятыми на камеру с разрешением от 1600x1200. Для достижения наилучшего результат значения ISO должно быть как можно меньше. [1]


## Классификация методов

На основании проделанной работы и составленной таблицы сравнения методов разработана следующая классификация методов фотограмметрии.

**По степени детализация модели**:
* Методы с низкой степенью детализация
	- Ортопроекции
* Методы с высокой степенью детализация
	- Structure from Motion
	- Terrestrial Laser Scanning
	- Стереофотограмметрия
* Методы с очень высокой степенью детализация
	- Комбинированный SfM и TLS


## Заключение

В рамках данной статьи была достигнута поставленная цель – построена классификация методов фотограмметрии для трехмерного сканирования зданий. Для этого были рассмотрены следующие методы фотограмметрии: Structure from Motion, Terrestrial Laser Scanning, Стереофотограмметрия, Комбинированный SfM и TLS, Ортопроекции. Был проведен сравнительный анализ на основе сформированных критериев ("Степень детализация модели", "Стоимость оборудования", "Минимальное количество снимков каждой детали") и выявленных проблем при сканировании зданий (погодные условия и размеры). На основе сравнительного анализа составлена классификация методов. Описаны рекомендации по процессу съемки зданий.

В дальнейшем следует расширить анализ, добавив в сравнение различные методы отслеживания положения камеры для TLS случая, провести сравнение коммерческих и OpenSource программ создания трехмерных моделей.

### Источники

1. Remondino F., Guarnieri A., Vettore A. 3D modeling of close-range objects: photogrammetry or laser scanning? //Videometrics VIII. – International Society for Optics and Photonics, 2005. – Т. 5665. – С. 56650M.
2. Remondino F. et al. UAV photogrammetry for mapping and 3d modeling–current status and future perspectives //International archives of the photogrammetry, remote sensing and spatial information sciences. – 2011. – Т. 38. – №. 1. – С. C22.
3. Galantucci L. M., Ferrandes R., Percoco G. Digital photogrammetry for facial recognition. – 2006.
4. Martinez-Guanter J. et al. Low-cost three-dimensional modeling of crop plants //Sensors. – 2019. – Т. 19. – №. 13. – С. 2883.
5. Schonberger J. L., Frahm J. M. Structure-from-motion revisited //Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. – 2016. – С. 4104-4113.
6. Zongjian L. I. N. et al. UAV for mapping—low altitude photogrammetric survey //International Archives of Photogrammetry and Remote Sensing, Beijing, China. – 2008. – Т. 37. – С. 1183-1186.
7. Linder W. Digital photogrammetry. – Berlin : Springer, 2009.
8. Hanke K., Grussenmeyer P. Architectural photogrammetry: Basic theory, procedures, tools //ISPRS Commission. – 2002. – Т. 5. – С. 1-2.
9. Pu S., Vosselman G. Knowledge based reconstruction of building models from terrestrial laser scanning data //ISPRS Journal of Photogrammetry and Remote Sensing. – 2009. – Т. 64. – №. 6. – С. 575-584.
10. Bethencourt A., Jaulin L. 3D reconstruction using interval methods on the kinect device coupled with an IMU //International Journal of Advanced Robotic Systems. – 2013. – Т. 10. – №. 2. – С. 93.
11. Grussenmeyer P. et al. Recording approach of heritage sites based on merging point clouds from high resolution photogrammetry and terrestrial laser scanning //Int. Arch. Photogramm. Remote Sens. Spat. Inf. Sci. – 2012. – Т. 39. – С. 553-558.
12. Balsa-Barreiro J., Fritsch D. Generation of 3D/4D photorealistic building models. The testbed area for 4D Cultural Heritage World Project: The historical center of Calw (Germany) //International Symposium on Visual Computing. – Springer, Cham, 2015. – С. 361-372.
