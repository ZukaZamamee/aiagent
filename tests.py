#tests.py
#from functions.get_files_info import get_files_info
#from functions.get_file_content import get_file_content
#from functions.write_file import write_file
from functions.run_python_file import run_python_file

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

#print("\nResult for 'main.py' file:")
#result = get_file_content("calculator", "main.py")
#print(result)

#print("\nResult for 'pkg/calculator.py' file:")
#result = get_file_content("calculator", "pkg/calculator.py")
#print(result)

#print("\nResult for '/bin/cat' file:")
#result = get_file_content("calculator", "/bin/cat")
#print(result)

#print("\nResult for 'pkg/does_not_exist.py' file:")
#result = get_file_content("calculator", "pkg/does_not_exist.py")
#print(result)

#print("\nResult for \"wait, this isn't lorem ipsum\"")
#result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
#print(result)

#print("\nResult for \"lorem ipsum dolor sit amet\" in \"pkg/morelorem.txt\"")
#result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
#print(result)

#print("\nResult for \"this should not be allowed\" in \"/tmp/temp.txt\"")
#result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
#print(result)

print("\nResult for running 'main.py' in 'calculator' directory")
result = run_python_file("calculator", "main.py")
print(result)

print("\nResult for running 'main.py' in 'calculator' directory with arguments [3 + 5]")
result = run_python_file("calculator", "main.py", ["3 + 5"])
print(result)

print("\nResult for running 'tests.py' in 'calculator' directory")
result = run_python_file("calculator", "tests.py")
print(result)

print("\nResult for running '../main.py' in 'calculator' directory")
result = run_python_file("calculator", "../main.py")
print(result)

print("\nResult for running 'nonexistent.py' in 'calculator' directory")
result = run_python_file("calculator", "nonexistent.py")
print(result)


