# При выполнении этого задания я решила воспользоваться пакетом Faker на php,
  так как эта библиотека позволяет генерировать данные искусственного наполнителя.

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

# В результате, при запуске кода мы получим такие данные как:
    
    (888) 937-7238
    bradley72@gmail.com
    k&|X+a45*2[
