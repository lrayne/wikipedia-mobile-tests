import allure
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene import browser as mobile
from allure import step


@allure.severity(Severity.CRITICAL)
@allure.suite('Погружение')
@allure.title('Завершение процесса погружения')
def test_complete_onboarding_proccess():

    with step(
        'Заголовок первого экрана должен быть: \'The Free Encyclopedia\n…in over 300 languages\''
    ):
        mobile.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.exact_text('The Free Encyclopedia\n…in over 300 languages')
        )

    # WHEN
    with step('Нажать на \'Continue\''):
        mobile.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')
        ).click()

    with step('Заголовок второго экрана должен быть: \'New ways to explore\''):
        mobile.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.exact_text('New ways to explore')
        )

    with step('Нажать на \'Continue\''):
        mobile.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')
        ).click()

    with step('Заголовок третьего экрана должен быть: \'Reading lists with sync\''):
        mobile.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.exact_text('Reading lists with sync')
        )

    with step('Нажать на \'Continue\''):
        mobile.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')
        ).click()

    with step('Заголовок четвертого экрана должен быть: \'Data & Privacy\''):
        mobile.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.exact_text('Data & Privacy')
        )

    # AND
    with step('Нажать на \'Get started\''):
        mobile.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button')
        ).click()

    # THEN
    with step('Пользователь видит ленту новостей'):
        mobile.element((AppiumBy.ID, 'org.wikipedia.alpha:id/feed_view')).should(
            be.visible
        )


@allure.severity(Severity.CRITICAL)
@allure.suite('Закладки')
@allure.title('Добавление нового списка для чтения')
def test_add_a_new_reading_list():

    # GIVEN
    reading_list_name = 'My reading list'

    # WHEN
    with step('Нажать на \'Skip\''):
        mobile.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')
        ).click()

    with step('Перейти на вкладку \'Saved\''):
        mobile.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/nav_tab_reading_lists')
        ).click()

    with step('Нажать на опции, выбрать \'Create new list\''):
        mobile.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/menu_overflow_button')
        ).click()
        mobile.element(
            (
                AppiumBy.ID,
                'org.wikipedia.alpha:id/reading_lists_overflow_create_new_list',
            )
        ).click()

    with step('В \'Name of this list\' ввести наименование'):
        mobile.element((AppiumBy.ID, 'org.wikipedia.alpha:id/text_input')).type(
            reading_list_name
        )

    with step('Подтвердить действие в модальном окне'):
        mobile.element((AppiumBy.ID, 'android:id/button1')).click()

    # THEN
    with step('Список для чтения создан'):
        mobile.element((AppiumBy.ID, 'org.wikipedia.alpha:id/item_title')).should(
            have.exact_text(reading_list_name)
        )


@allure.severity(Severity.NORMAL)
@allure.suite('Погружение')
@allure.title('Добавление нового языка через экран погружения')
def test_add_a_new_language_through_onboarding_screen():

    # GIVEN
    language = 'Russian'

    # WHEN
    with step('Нажать на \'Add or edit languages\''):
        mobile.element(
            (
                AppiumBy.ID,
                'org.wikipedia.alpha:id/addLanguageButton',
            )
        ).click()

    with step('Нажать на \'Add language\', выбрать один из языков'):
        mobile.all(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/wiki_language_title')
        ).second.click()
        mobile.all(
            (
                AppiumBy.ID,
                'org.wikipedia.alpha:id/language_subtitle',
            )
        ).element_by(have.exact_text(language)).click()

    # THEN
    with step('В \'Your languages\' отображается выбранный язык'):
        mobile.all(
            (
                AppiumBy.ID,
                'org.wikipedia.alpha:id/wiki_language_title',
            )
        ).should(have.exact_texts('English', language, 'Add language'))
