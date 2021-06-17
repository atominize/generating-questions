from math import comb
import random

beginning_of_xml = """
<?xml version="1.0" encoding="UTF-8"?>
<quiz>
"""
ending_of_xml = """
</quiz>
"""


# a = 2
# b = 3
# n = 5
# r = 2
def print_question(a, b, n, r):
    expression = f"({a}x - {b})^{{{n}}}"
    term = f"x^{{{r}}}"
    answer = str(comb(n, r) * ((a) ** r) * ((-b) ** (n - r)))
    question = f"""
  <question type="numerical">
    <name>
      <text>In the expansion of \( {expression} \), what is the coefficient of \( {term} \)?</text>
    </name>
    <questiontext format="html">
      <text><![CDATA[In the expansion of&nbsp;\(  {expression}  \), what is the coefficient of&nbsp;\( {term} \)?<br>]]></text>
    </questiontext>
    <generalfeedback format="html">
      <text></text>
    </generalfeedback>
    <defaultgrade>1.0000000</defaultgrade>
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
    for i in range(1, 201):
        new_n = random.randint(5, 12)
        new_r = random.randint(3, (new_n - 1))
        new_a = random.randint(2, 5)
        new_b = random.randint(2, 5)
        with open("questions.xml", "a") as f:
            f.write(print_question(new_a, new_b, new_n, new_r))
    with open("questions.xml", "a") as f:
        f.write(ending_of_xml)