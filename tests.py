#tests.py
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

#print("Result for current directory:")
#result = get_files_info("calculator", ".")
#rint(result)

#print("Result for 'pkg' directory:")
#result = get_files_info("calculator", "pkg")
#print(result)

#print("Result for '/bin' directory:")
#result = get_files_info("calculator", "/bin")
#print(result)

#print("Result for '../' directory:")
#result = get_files_info("calculator", "../")
#print(result)

#print("Result for truncation test of lorem.txt")
#result = get_file_content("calculator", "lorem.txt")
#print(result)

print("\nResult for 'main.py' file:")
result = get_file_content("calculator", "main.py")
print(result)

print("\nResult for 'pkg/calculator.py' file:")
result = get_file_content("calculator", "pkg/calculator.py")
print(result)

print("\nResult for '/bin/cat' file:")
result = get_file_content("calculator", "/bin/cat")
print(result)

print("\nResult for 'pkg/does_not_exist.py' file:")
result = get_file_content("calculator", "pkg/does_not_exist.py")
print(result)