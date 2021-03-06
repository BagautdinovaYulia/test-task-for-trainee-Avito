## Решение задания №1

**Условие:** Найти на Авито (сайт/мобильные приложения) один любой баг и описать на него баг-репорт.
Дополнительно: сделать это внутри категории коммерческая недвижимость.

### Баг-репорт "Наложение текста на карте в категории Недвижимость при отсутствии интернета"
| Attribute | Description |
| ------------- | ------------- |
| **Summary** | При создании условия сбоя интернет-соединения у юзера, возникает ошибка верстки, а именно наложение сообщения об ошибке на поле выбора объявления  |
| **Component** | Мобильное приложение "Авито"<br /> Раздел "Недвижемость" |
| **Environment** | Mi Note 2, Android 8.0.0 |
| **Severity** | S4 (Minor) |
| **Priority** | P2 (Medium) |
| **Reproducibility** | Always |
| **STR** |    1. Открыть мобильное приложение Авито; <br /> 2. Открыть параметры (справа от поля Поиск); <br /> 3. Выбрать категорию - Недвижемость, <br /> Город или регион - любой; <br /> 4. Нажать на кнопку «Показать N объявлений»; <br /> 5. Нажать на поле карты; <br /> 6. Перевести телефон в авиарежим; <br /> 7. Нажать на любое объявление на карте <br />|
| **Expected result** | Сообщение об ошибке "Не удалось загрузить объявления" перекрывает текст "Показать N объявлений" |
| **Actual result** | Сообщение об ошибке не перекрывает текст. Сообщение об ошибке всплывает внизу карты, но над полем "Показать N объявлений" |
| **Attachments** | ![<img src="img/image_task-1.jpg" width="900"/>](img/image_task-1.jpg "Приложение")|
