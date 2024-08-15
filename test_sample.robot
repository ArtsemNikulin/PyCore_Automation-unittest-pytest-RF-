*** Settings ***
#Resource    C:/Users/Artsem_Nikulin/PycharmProjects/pyhton-core/task-1-template/tasks/keywords.robot
Library    C:/Users/Artsem_Nikulin/PycharmProjects/pyhton-core/task-2-template/tasks/ClassLibrary.py    James
*** Test Cases ***
Test 2
    ${result}=    Raise 2 To The Power Of 3
    Should Be Equal    ${result}    My name is Jame
Test My Name Is Without Surname
    ${result}=    My Name Is
    Should Be Equal    ${result}    My name is James
Test My Name Is
    ${result1}=    My name is    John
    Should Be Equal    ${result1}    My name is John
Test My Name Is2
    ${result2}=    My name is    James    Bond
    Should Be Equal    ${result2}    My name is Bond, James Bond
Test Concatenate Varargs
    ${result}=    Concatenate varargs    first    second
    Should Be Equal    ${result}    first second
Test def
    ${result}=    Definitions    another=value two    esca=value three
    Should Be Equal    ${result}    first second
Test def2
    ${result}=    Knights Of Ni
    Should Be Equal    ${result}    first second
Test Raise 2 To The Power Of 3
    ${result}=    Raise 2 To The Power Of 3
    Should Be Equal As Numbers    ${result}    4