*** Keywords ***
My name is
    [Documentation]    The keyword should take one required positional argument, 'name',
    ...                and one positional argument with a default value (empty), 'surname'.
    ...                The keyword should log a following message when called: "Got name=<value>, surname=<value>"
    ...                For example: "Got name=John, surname="
    ...                Logs should appear in the console.
    ...                The keyword should return a string "My name is <name>" if 'surname' is empty,
    ...                or "My name is <surname>, <name> <surname>" if 'surname' was given.
    ...                For example: "My name is John"; "My name is Bond, James Bond"
    [Arguments]    ${name}    ${surname}=${EMPTY}
    Log To Console    Got name=${name}, surname=${surname}
    ${result}=    Run Keyword If    '${surname}' == ''    Set Variable    My name is ${name}
    ...                       ELSE    Set Variable    My name is ${surname}, ${name} ${surname}

    RETURN    ${result}

Concatenate varargs
    [Documentation]    The keyword should take a variable number of positional arguments into the list 'args'.
    ...                The keyword should log a following message when called: "Got args=<values>"
    ...                For example: "Got args=['first', 'second']"
    ...                Logs should appear in the console.
    ...                The keyword should return a string made of space-separated arguments it received.
    ...                For example: "first second"
    ...                Hint: use the 'Catenate' keyword from the BuiltIn library, or extended variable syntax.
    [Arguments]    @{args}
    Log To Console    Got args=@{args}
    ${result}=    Catenate    SEPARATOR=${SPACE}    @{args}

    RETURN    ${result}


Definitions
    [Documentation]    The keyword should take a variable number of named arguments into the dictionary 'args'.
    ...                The keyword should log a following message when called: "Got args=<values>"
    ...                For example: "Got args={'key'='value'}"
    ...                Logs should appear in the console.
    ...                The keyword should return a string of this format: "<key1> is a <value1>, <key2> is a <value2>"
    ...                (each new pair is appended to the string with a comma and a space).
    ...                For example: "apple is a fruit, cake is a lie"
    ...                Hint: use the 'Evaluate' keyword from the BuiltIn library with a Python expression.
    [Arguments]    &{args}
    Log To Console    Got args=&{args}
    ${result}=	Evaluate	', '.join([f"{k} is a {v}" for k, v in &{args}.items()])	modules=json
    
    RETURN    ${result}

Knights of Ni
    [Documentation]    The keyword should take a single named-only argument 'loud'
    ...                with a default value of boolean 'False' and no other arguments.
    ...                The keyword should log a following message when called: "Got loud=<value>"
    ...                For example: "Got loud=False"
    ...                Logs should appear in the console.
    ...                The keyword should return the string "We are the knights of Ni!" if 'loud' is False,
    ...                and "WE ARE THE KNIGHTS OF NI!" otherwise.
    [Arguments]    ${loud}=${FALSE}
    Log To Console    Got loud=${loud}
    ${result}=    Run Keyword If    ${loud} == ${FALSE}    Set Variable    We are the knights of Ni!    
...                                ELSE    Set Variable    WE ARE THE KNIGHTS OF NI!
    
    RETURN    ${result}
    
Raise ${base} To The Power Of ${power}
    [Documentation]    The keyword should take two embedded arguments: 'base', after the word 'raise', and
    ...                'power', after the word 'of'.
    ...                The keyword should log a following message when called: "Got base=<value>, power=<value>"
    ...                For example: "Got base=4, power=3"
    ...                Logs should appear in the console.
    ...                The keyword should return an integer: 'base' raised to the power of 'power'.
    ...                For example, with base=2 and power=4: 16
    ...                Hint: use extended variable syntax.

    Log To Console    Got base=${base}, power=${power}
    ${result}=    Evaluate    ${base} ** ${power}
    RETURN    ${result}
        
