import sys
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def main():
    #print("Result for 'calculator', '.' :")
    #print(get_files_info("calculator", "."))
    #print("")

    #print("Result for 'calculator', 'pkg' :")
    #print(get_files_info("calculator", "pkg"))
    #print("")

    #print("Result for 'calculator', '/bin' :")
    #print(get_files_info("calculator", "/bin"))
    #print("")

    #print("Result for 'calculator', '../' :")
    #print(get_files_info("calculator", "../"))
    #print("")

    #print("Result for 'calculator', 'lorem.txt' :")
    #print(get_file_content("calculator", "lorem.txt"))
    #print("")

    #print("Result for 'calculator', 'main.py' :")
    #print(get_file_content("calculator", "main.py"))
    #print("")

    #print("Result for 'calculator', 'pkg/calculator.py' :")
    #print(get_file_content("calculator", "pkg/calculator.py"))
    #print("")

    #print("Result for 'calculator', '/bin/cat' :")
    #print(get_file_content("calculator", "/bin/cat"))
    #print("")

    #print("Result for 'calculator', 'lorem.txt', 'wait, this isn't lorem ipsum' :")
    #print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    #print("")

    #print("Result for 'calculator', 'pkg/more_lorem.txt', 'lorem ipsum dolor sit amet' :")
    #print(write_file("calculator", "pkg/more_lorem.txt", "lorem ipsum dolor sit amet"))
    #print("")

    #print("Result for 'calculator', '/tmp/temp.txt', 'this should not be allowed' :")
    #print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    #print("")

    print("Result for 'calculator', 'main.py'")
    print(run_python_file("calculator", "main.py"))
    print("")

    print("Result for 'calculator', 'tests.py'") 
    print(run_python_file("calculator", "tests.py"))
    print("")

    print("Result for 'calculator', '../main.py'")
    print(run_python_file("calculator", "../main.py"))
    print("")

    print("Result for 'calculator', 'nonexistent.py'")
    print(run_python_file("calculator", "nonexistent.py"))
    print("")


if __name__ == "__main__":
    main()
