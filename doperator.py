from utils import factorize

beginning_of_xml = """
<?xml version="1.0" encoding="UTF-8"?>
<quiz>
"""
ending_of_xml = """
</quiz>
"""

def format(value):
    if value == 1:
        return ""
    return value

def print_question(a,b,c,d,e,f):

    question = f"""
        <question type="cloze">
            <name>
              <text>Consider the proof below and answer the subsequent questions.</text>
            </name>
            <questiontext format="html">
              <text><![CDATA[Consider the proof below and answer the subsequent questions.<br><br>\( \\begin{{align*}}&nbsp;\displaystyle \sum_{{s=1}}^n s^4
        &amp;= \sum_{{s=1}}^n \left[ s(s-1)(s-2)(s-3) + {format(a)}\\alpha s(s-1)(s-2) + \\beta s(s-1) + s\\right] \\\\
        &amp;= \sum_{{s=1}}^n \left[ y_4(s) + {format(a)}\\alpha y_3(s) +&nbsp;\\beta y_2(s) + y_1(s)\\right] \\\\
        &amp;= \sum_{{s=\gamma}}^n \left[ y_4(s) +&nbsp;{format(a)}\\alpha y_3(s) +&nbsp;\\beta y_2(s) + y_1(s)\\right] \\\\
        &amp;= \\frac{{1}}{{5}} y_5(n+1) + \\frac{{{format(a)}\\alpha}}{{4}} y_4(n+1) + \\frac{{\\beta}}{{3}} y_3(n+1) + \\frac{{1}}{{2}} y_2(n+1) \\\\
        &amp;= \\frac{{1}}{{5}} (n+1)n(n-1)(n-2)(n-3) + \\frac{{3}}{{2}} (n+1)n(n-1)(n-2) + \\frac{{\\beta}}{{3}} (n+1)n(n-1) + \\frac{{1}}{{2}} (n+1)n \\\\
        &amp;= \\frac{{(n+1)n}}{{30}}\left[ {format(b)}\delta (n-1)(n-2)(n-3) + {format(c)}\eta (n-1)(n-2) + {format(d)}\\theta (n-1) + {format(e)}\kappa \\right] \\\\
        &amp;= \\frac{{(n+1)n}}{{30}}\left[ {format(b)}\delta n^3 + {format(f)}\lambda n^2 + \mu n + \\rho \\right] 
        \end{{align*}} \)<br><br>$$\\alpha = $${{1:NM:={6/a}}}&nbsp;$$\\beta = $${{1:NM:=7}}&nbsp;$$\gamma = $${{1:NM:=0}} $$\delta = $${{1:NM:={6/b}}}&nbsp;$$\eta = $${{1:NM:={45/c}}}&nbsp;<br><br>$$\\theta = $${{1:NM:={70/d}}} $$\kappa = $${{1:NM:={15/e}}}&nbsp;$$\lambda = $${{1:NM:={9/f}}}&nbsp;$$\mu = $${{1:NM:=1}} $$\\rho = $${{1:NM:=-1}}<br>]]></text>
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
    factors_of_alpha = factorize(6)
    factors_of_delta = factorize(6)
    factors_of_eta = factorize(45)
    factors_of_theta = factorize(70)
    factors_of_kappa = factorize(15)
    factors_of_lambda = factorize(9)
    for a in factors_of_alpha:
        for b in factors_of_delta:
            # if a == b:
            #     break
            for c in factors_of_eta:
                # if a == c or b == c:
                #     break
                for d in factors_of_theta:
                    # if a == d or b == d or c == d:
                    #     break
                    for e in factors_of_kappa:
                        # if a == e or b == e or c == e or d == e:
                        #     break
                        for f in factors_of_lambda:
                            # if a == f or b == f or c ==f or d == f or e == f:
                            #     break
                            with open("questions.xml", "a") as file:
                                file.write(print_question(a,b,c,d,e,f))
    with open("questions.xml", "a") as f:
        f.write(ending_of_xml)



def test():
    factors_of_alpha = factorize(6)
    for a in factors_of_alpha:
        print(6/a)