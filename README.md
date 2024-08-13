<p align="center">
  <a href="https://demoblaze.com">
  <picture>
<img alt="Wikipedia" src="resources/logo.png" width="100" height="100">
    </picture>
  </a>
</p>
<h1 align="center">
  Wikipedia mobile tests
</h1>
<p align="center">
Тест-кейсы для общедоступной интернет-энциклопедии со свободным контентом
</p>

<p align="center">
<img title="Python" src="resources/icons/python.svg" height="30" width="30"/> 
<img title="Selene" src="resources/icons/selene.png" height="30" width="30"/>  
<img title="Pytest" src="resources/icons/pytest.svg" height="30" width="30"/> 
<img title="Allure Report" src="resources/icons/allure-report.png" height="30" width="30"/> 
<img title="Allure TestOps" src="resources/icons/allure-testops.png" height="30" width="30"/> 
<img title="Selenoid" src="resources/icons/selenoid.png" height="30" width="30"/> 
<img title="Jenkins" src="resources/icons/jenkins.svg" height="30" width="30"/> 
<img title="GitHub" src="resources/icons/github.svg" height="30" width="30"/> 
<img title="Pycharm" src="resources/icons/pycharm.png" height="30" width="30"/> 
<img title="Telegram" src="resources/icons/telegram.png" height="30" width="30"/> 
<img title="Jira" src="resources/icons/jira.png" height="30" width="30"/> 
<img title="Requests" src="resources/icons/requests.png" height="30" width="30"/> 
<img title="Mimesis" src="resources/icons/mimesis.svg" height="30" width="30"/> 
<img title="Pydantic" src="resources/icons/pydantic.svg" height="30" width="30"/> 
<img title="Black" src="resources/icons/black.png" height="30" width="30"/> 
<img title="Poetry" src="resources/icons/poetry.png" height="30" width="30"/>
</p>

## Запуск

1. Склонировать репозиторий:

```
git clone https://github.com/lrayne/demoblaze-tests.git
```

2. Установить зависимости:

```
poetry install
```

3. Открыть проект в PyCharm, настроить интерпретатор

4. Скопировать содержимое из `config.*.env.example` в `config.*.env`, где `*` — `local` или `remote`
5. Поместить `config.*.env` в корень проекта
6. При необходимости изменить значения у параметров в `config.*.env`
7. Запустить тест-кейсы, исходя из выбранного контекста:

```
context='local' pytest tests
```

```
context='remote' pytest tests
```

8. Cгенерировать отчёт:

```
allure serve allure-results
```

## <img title="Jenkins" src="resources/icons/jenkins.svg" height="30" width="30"/> Jenkins

[![Button](https://img.shields.io/badge/Открыть%20сборку-d33732)](https://jenkins.autotests.cloud/job/demoblaze-tests/)

### Параметры сборки:

- `TEST_SUITE` — тестовый набор
- `DRIVER_NAME` — наименование браузера
- `DRIVER_VERSION` — версия браузера
- `WINDOW_WIDTH` и `WINDOW_HEIGHT` — разрешение окна
- `TIMEOUT` — максимальное время ожидания элемента
- `ENVIRONMENT` — окружение, `COMMENT` — комментарий. Будут отображаться в уведомлении telegram'а

<details><summary>Результат выполнения</summary>
<br>
<details><summary>Общая информация</summary>
<br>
<img src="resources/screens/allure-overview.png">
</details>
<details><summary>Тест-кейсы</summary>
<br>
<img src="resources/screens/allure-test-cases.png">
</details>
<details><summary>Видео прохождения тест-кейса</summary>
<br>
<img src="resources/screens/selenoid-video-attach.gif">
<p></p>
</details>
<details><summary>Уведомление в telegram</summary>
<br>
<img src="resources/screens/telegram-notification.png">
</details>
</details>

## <img title="Allure TestOps" src="resources/icons/allure-testops.png" height="30" width="30"/> Allure TestOps

[![Button](https://img.shields.io/badge/Открыть%20проект-21c45e)](https://allure.autotests.cloud/project/4370/dashboards)



<details><summary>Общая информация</summary>
<br>
<img src="resources/screens/allure-testops-overview.png">
</details>

<details><summary>Тест-кейсы</summary>
<br>
<img src="resources/screens/allure-testops-testcases.png">
</details>

<details><summary>История запусков</summary>
<br>
<img src="resources/screens/allure-testops-jobs.png">
</details>

## <img title="Jira" src="resources/icons/jira.png" height="30" width="30"/>  Jira

[![Button](https://img.shields.io/badge/Открыть%20проект-2584ff)](https://https://jira.autotests.cloud/browse/HOMEWORK-1318
)

<details><summary>Тест-кейсы</summary>
<br>
<img src="resources/screens/jira-testcases.png">
</details>

<details><summary>История запусков</summary>
<br>
<img src="resources/screens/jira-launches.png">
</details>
