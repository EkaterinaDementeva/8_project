# 8_project
Проект, который связан с настройками пользовательского интерфейса, а именно с набором инструментов, который можно отредактировать в отдельном окне.

Обратите внимание на картинку, приложенную к домашнему заданию. Что в общем я ожидаю от его выполнения:

При выполнении скрипта открывается окно, в котором присутствует всего одна кнопка - Options.
При нажатии на кнопку появляется дополнительное окно с двумя полями:
В левом поле представлены все доступные инструменты проекта
Правое поле пустое, в него можно перетащить инструменты из левого поля.
При перетаскивании элемента из одного поля в другое - в первом поле он соответственно удаляется.
При нажатии на "Save"
вся информация из правого поля сохраняется в отдельный json файл
Главное окно программы обновляется и в него подгружаются (либо наоборот выгружаются - если мы их удалили из правого поля) выбранные инструменты
Теперь, мы в главном окне можем пользоваться этими инструментами. И в следующий раз, когда мы перезапустем Maya, либо просто заново создадим наше главное окно - все выбранные наши инструменты будут видны (при создании окна нужно будет каждый раз считывать json файл).
Когда мы откроем окно опций еще раз - наш набор выбранных инструментов справа должен быть виден.
