<h2>Задача</h2>

<p>Нужно создать простейший сервис просмотра информации о погоде.</p>

<p>При создании сервиса нужно соблюсти следующие условия:</p>

<ol>
    <li>Необходимо использовать фреймворк React и адаптивный дизайн, чтобы страница открывалась на любом consumer-grade устройстве.</li>
    <li>Пользователь должен либо иметь возможность выбрать из списка город, для которого ему нужен прогноз погоды.</li>
    <li>Пользователь должен иметь возможность посмотреть данные на следующие временные промежутки:</li>
    <ul>
        <li>«сейчас» (поминутно на ближайший час);</li>
        <li>«ближайшие два дня» (почасово на двое суток);</li>
        <li>«на этой неделе» (следующие семь дней).</li>
    </ul>
    <li>Данные должны запрашиваться через One Call API OpenWeather</li>
</ol>

<h2>Установка и запуск</h2>

<ol>
    <li>Клонировать репозиторий: <code>git clone https://github.com/g3n0m/WeatherInfoService.git</code></li>
    <li>В консоли в соответствующей папке проекта восстановить модули: <code>npm install</code></li>
    <li>Запуск сервера разработки: <code>npm run start</code></li>
    <li>Запуск build сборки: <code>npm run build</code></li>
    <li>Добавить в корне проекта файл const.js с описанием переменных apiKey и geolocationKey следующего содержания:<br>
        <code>let apiKey = "ключ openweathermap"</code><br>
        <code>let geolocationKey = "ключ ipgeolocation"</code><br>
        <code>export { apiKey, geolocationKey }</code><br>
    </li>
</ol>

<h2>Инструменты разработки</h2>

<ol>
    <li>Сборщик пакетов webpack</li>
    <li>Ручная сборка проекта, настройка конфигов под тестирование на локальном сервере</li>
    <li>Библиотека react</li>
    <li>Использование API для получения данных с сервиса OpenWeather, определение геопозиции</li>
    <li>Адаптивный дизайн</li>
</ol>
