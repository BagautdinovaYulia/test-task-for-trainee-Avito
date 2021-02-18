Решение задания №3
=====================

**Условие** </br>
У пользователя есть возможность авторизоваться на сайте через форму https://www.avito.ru/#login
В качестве логина можно использовать номер мобильного телефона или электронную почту.
В качестве пароля можно использовать цифры, буквы латинского языка и специальные символы. Допустимая длина пароля от 8 до 16 символов.</br>
Составить набор тестовых данных, при котором мы гарантированно будем знать, что авторизация работает
***
**Результат** </br>
*Блок-схема всех возможных значений*

![<img src="img/block.png" width="800"/>](img/block.png "Блок-схема")

*Файл для генерации всех значений в PICT*

![<img src="img/anketa.png" width="800"/>](img/anketa.png "Значения")

***

**Дополнительно** </br>
При выполнении этого задания я решила воспользоваться пакетом Faker на php, так как эта библиотека позволяет генерировать данные искусственного наполнителя.

Для этого необходимо подключить Сomposer или установить, если его нет:

    $ php composer-setup.php --install-dir=/usr/local/bin --filename=composer

Далее нам требуется установить пакет Faker https://github.com/fzaninotto/Faker:

    $ composer require fzaninotto/faker

Написав такой незамысловатый код, мы получим слуйчайные валидные данные для наших полей

    <?php 
    require_once 'vendor/utoload.php';

    $fakerNumber = new Faker\Provider\en_RU\PhoneNumber::create();
    echo $fakerNumber -> tollFreePhoneNumber, "\n";

    $fakerAdress = new Faker\Provider\Internet::create();
    echo $fakerAdress -> freeEmail, "\n";
    echo $fakerAdress -> password, "\n";
    ?>

В результате, при запуске кода мы получим такие данные как:
    
    (888) 937-7238
    bradley72@gmail.com
    k&|X+a45*2[
