
from prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
my_list = [ruby, python, visual_basic]

print("The dynamically typed languages are:")
for i in my_list:
    if i.is_dynamic() == True:
        print(i.name)
