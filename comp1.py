

beginning_of_xml = """
<?xml version="1.0" encoding="UTF-8"?>
<quiz>
"""
ending_of_xml = """
</quiz>
"""


def print_question(r, sub):
    expression = f"z_n = \\frac{{\left( \sqrt{{3}} + i \\right)^{{4n+{r}}} }}{{\left( 1 -i\sqrt{{3}} \\right)^{{4n}}}}"
    answer = 6 / r
    question = f"""
        <question type="cloze">
            <name>
              <text>Let 
                $$\displaystyle {expression}$$
               for any positive integer $n$.</text>
            </name>
            <questiontext format="html">
              <text><![CDATA[<p dir="ltr" style="text-align: left;">Let 
                $$\displaystyle {expression} &nbsp;$$
               for any positive integer $$n$$. If&nbsp;
               $$\displaystyle \\arg(z_{{{sub}}}) = \\frac{{\pi}}{{k}}$$ and&nbsp;
               $$\displaystyle \\arg(z_{{{sub + 1}}}) = \\frac{{\pi}}{{m}}$$
<br></p><p dir="ltr" style="text-align: left;">Then $$k = $${{1:NM:={answer}}}, $$m = $${{1:NM:={answer}}}</p>]]></text>
            </questiontext>
            <generalfeedback format="html">
              <text></text>
            </generalfeedback>
            <penalty>0.3333333</penalty>
            <hidden>0</hidden>
            <idnumber></idnumber>
        </question>
    """

    return question


def start():
    with open("questions.xml", "w") as f:
        f.write(beginning_of_xml)
    r_list = [1, 2, 3, 6]
    for item in range(0, 4):
        r = r_list[item]
        for sub in range(2, 52):
            with open("questions.xml", "a") as f:
                f.write(print_question(r, sub))
    with open("questions.xml", "a") as f:
        f.write(ending_of_xml)


def test():
    print(6/1, 6/2, 6/3, 6/6)