import random

from utils import multi_coefficient

beginning_of_xml = """
<?xml version="1.0" encoding="UTF-8"?>
<quiz>
"""
ending_of_xml = """
</quiz>
"""


def print_question(n, a, b, c):
    expression = f"\\binom {{{n}}} {{{a}, {b}, {c}}}"
    answer = multi_coefficient(n, [a, b, c])
    if answer <= 1 or answer > 1000000:
        return ""
    question = f"""
    <question type="numerical">
        <name>
          <text>Evaluate \( {expression} \)</text>
        </name>
        <questiontext format="html">
          <text><![CDATA[<p dir="ltr" style="text-align: left;">Evaluate \( \displaystyle {expression} \)<br></p>]]></text>
        </questiontext>
        <generalfeedback format="html">
          <text></text>
        </generalfeedback>
        <defaultgrade>1</defaultgrade>
        <penalty>0.3333333</penalty>
        <hidden>0</hidden>
        <idnumber></idnumber>
        <answer fraction="100" format="moodle_auto_format">
          <text>{answer}</text>
          <feedback format="html">
            <text></text>
          </feedback>
          <tolerance>0</tolerance>
        </answer>
        <unitgradingtype>0</unitgradingtype>
        <unitpenalty>0.1000000</unitpenalty>
        <showunits>3</showunits>
        <unitsleft>0</unitsleft>
    </question>
    """
    return question


def start():
    with open("questions.xml", "w") as f:
        f.write(beginning_of_xml)
    for n in range(12, 16):
        for a in range(0, n + 1):
            for b in range(0, a + 1):
                if (a + b) > n:
                    break
                c = n - (a + b)
                with open("questions.xml", "a") as f:
                    f.write(print_question(n, a, b, c))
    with open("questions.xml", "a") as f:
        f.write(ending_of_xml)


def test():
    number = 0
    for n in range(12, 16):
        for a in range(0, n + 1):
            for b in range(0, a + 1):
                if (a + b) > n:
                    break
                c = n - (a + b)
                number = number + 1
                print(multi_coefficient(n, [a, b, c]))
    print(number)

