def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function() # Тут функция вызывается, но срабатывает только при вызове основной функции test_function()
#inner_function() #NameError: name 'inner_function' is not defined. Поскольку она существует только в своей области видимости

#inner_function() #NameError: name 'inner_function' is not definedб так как она существует только в своей области видимости,
# её не существует в глобальной области видимости
test_function()