# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser Chrome"
# или "Open Browser [Chrome]"
# на ваш выбор.
def open_browser(browser_name="Chrome"):
    return browser_name


def go_to_company_name_homepage(page_url="https://www.google.com/"):
    return page_url


def find_registration_button_on_login_page(page_url="https://www.google.com/", button_text="button Log in"):
    return page_url, button_text


def func_name(func):
    name_func = func.__name__
    name_arg = func()
    print(f"{name_func}: {name_arg}".title().replace("_", " ").replace("Https://", "").replace("/", "").replace("(", "")
          .replace("'", "").replace(")", ""))


func_name(open_browser)
func_name(go_to_company_name_homepage)
func_name(find_registration_button_on_login_page)




