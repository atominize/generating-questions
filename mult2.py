import random

from utils import multi_coefficient

beginning_of_xml = """
<?xml version="1.0" encoding="UTF-8"?>
<quiz>
"""
ending_of_xml = """
</quiz>
"""


def getOperation(number):
    if number > 0:
        return "+"
    else:
        return "-"


def convertOper(operation):
    if operation == "+":
        return 1
    else:
        return -1


def formatOne(number):
    if number == 1:
        return ""
    else:
        return number


def print_question(a, b, c, d):
    expression = f"\left({formatOne(a)}x^2 {getOperation(d)} \\frac{{{b}}}{{y}} + \\frac{{{formatOne(c)}y}}{{x}} \\right)^5"
    answer = multi_coefficient(5, [2, 1, 2])*(a**2)*b*(c**2)*convertOper(getOperation(d))
    # if answer <= 1 or answer > 1000000:
    #     return ""
    question = f"""
    <question type="numerical">
        <name>
          <text>The coefficient of \( x^2y \) in the expansion of \( {expression} \) is</text>
        </name>
        <questiontext format="html">
          <text><![CDATA[<p dir="ltr" style="text-align: left;">The coefficient of \( x^2y \) in the expansion of&nbsp;\(\displaystyle &nbsp;{expression} \) is&nbsp;</p>]]></text>
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
    for a in range(1, 6):
        for b in range(1, 6):
            for c in range(1, 6):
                for d in range(0, 2):
                    with open("questions.xml", "a") as f:
                        f.write(print_question(a, b, c, d))
    with open("questions.xml", "a") as f:
        f.write(ending_of_xml)


def test():
    # d = random.randrange(0,2,1)
    # a = b = c = 1
    for a in range(1, 6):
        print(a)

