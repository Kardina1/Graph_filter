from PIL import Image
from Filters import filters, validate_path, validate_value, validate_save

menu = "Выберите фильтр который хотите применить к изображению\n"
for filter in filters:
    menu += f"{filter}) {filters[filter]['name']}\n"
menu += "0) Выход"

finish = False

path = validate_path()
img = Image.open(path).convert("RGB")
while not finish:
    flag = False
    while not flag:
        print(menu)
        choise = int(validate_value("Выберите фильтр (или 0 для выхода):", ["0", "1", "2", "3", "4"]))

        if choise == 0:
            finish = True
            flag = True
        else:
            print(f"\n{filters[choise]['name']}")
            print(f"{filters[choise]['description']}")
            agree = validate_value("Применить фильтр к изображению (Да, Нет)?\nВвод:",["да", "нет"])

            if agree == "нет":
                flag = True
            else:
                filter = filters[choise]['class']
                img = filter.apply_to_image(img)
                save_path = validate_save()
                img.save(save_path)

                agree = validate_value("Ещё раз?\nВвод: ", ["да", "нет"])
                finish = agree == "нет"
                flag = agree == "нет"

print("До свидания!")
