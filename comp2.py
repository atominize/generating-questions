from math import gcd

beginning_of_xml = """
<?xml version="1.0" encoding="UTF-8"?>
<quiz>
"""
ending_of_xml = """
</quiz>
"""


def print_question(a, b, c, d, coe_alpha_1, coe_beta_1, first_eqn_val, coe_alpha_2, coe_beta_2, second_eqn_val):
    coe_alpha_1 = "" if coe_alpha_1 == 1 else coe_alpha_1
    coe_beta_1 = "" if coe_beta_1 == 1 else coe_beta_1
    coe_alpha_2 = "" if coe_alpha_2 == 1 else coe_alpha_2
    coe_beta_2 = "" if coe_beta_2 == 1 else coe_beta_2
    exp1 = f"{coe_alpha_1}\\alpha + {coe_beta_1}\\beta = {first_eqn_val}"
    exp2 = f"{coe_alpha_2}\\alpha - {coe_beta_2}\\beta = {second_eqn_val}i"
    question = f"""
    <question type="cloze">
        <name>
          <text>If \( {exp1} \) and \( {exp2} \)</text>
        </name>
        <questiontext format="html">
          <text><![CDATA[<p dir="ltr" style="text-align: left;">If&nbsp;
          \(  {exp1} \) 
          and&nbsp;\( {exp2} \), solve for 
          $$\\alpha$$ and $$\\beta$$.</p><p dir="ltr" style="text-align: left;">
          $$\\alpha = $${{1:NM:={a}}} $$+$$ {{1:NM:={b}}}$$i$$</p>
          <p dir="ltr" style="text-align: left;">
          $$\\beta = $${{1:NM:={c}}} $$+$$ {{1:NM:={d}}}$$i$$<br></p>]]></text>
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
    alpha = [2, 3]
    beta = [4, -1]
    for item in range(1, 16):
        new_alpha = [element * item for element in alpha]
        for thing in range(1, 16):
            new_beta = [element * thing for element in beta]
            coe_alpha_1 = 1
            coe_beta_1 = 1
            coe_alpha_2 = 1
            coe_beta_2 = 1
            if new_alpha[1] >= abs(new_beta[1]):
                if new_alpha[1] % abs(new_beta[1]) == 0:
                    coe_beta_1 = -round(new_alpha[1] / new_beta[1])
                else:
                    common_div = gcd(abs(new_beta[1]), new_alpha[1])
                    coe_alpha_1 = round(abs(new_beta[1]) / common_div)
                    coe_beta_1 = round(new_alpha[1] / common_div)
            else:
                if abs(new_beta[1]) % new_alpha[1] == 0:
                    coe_alpha_1 = -round(new_beta[1] / new_alpha[1])
                else:
                    common_div = gcd(abs(new_beta[1]), new_alpha[1])
                    coe_alpha_1 = round(abs(new_beta[1]) / common_div)
                    coe_beta_1 =  round(new_alpha[1] / common_div)
            if new_beta[0] >= new_alpha[0]:
                if new_beta[0] % new_alpha[0] == 0:
                    coe_alpha_2 = round(new_beta[0] / new_alpha[0])
                else:
                    common_div = gcd(new_alpha[0], new_beta[0])
                    coe_alpha_2 = round(new_beta[0] / common_div)
                    coe_beta_2 = round(new_alpha[0] / common_div)
            else:
                if new_alpha[0] % new_beta[0] == 0:
                    coe_beta_2 = round(new_alpha[0] / new_beta[0])
                else:
                    common_div = gcd(new_beta[0], new_alpha[0])
                    coe_alpha_2 = round(new_beta[0] / common_div)
                    coe_beta_2 = round(new_alpha[0] / common_div)
            first_eqn_val = (coe_alpha_1 * new_alpha[0]) + (coe_beta_1 * new_beta[0])
            second_eqn_val = (coe_alpha_2 * new_alpha[1]) - (coe_beta_2 * new_beta[1])
            with open("questions.xml", "a") as f:
                f.write(print_question(new_alpha[0], new_alpha[1], new_beta[0], new_beta[1], coe_alpha_1, coe_beta_1,
                                       first_eqn_val, coe_alpha_2, coe_beta_2, second_eqn_val))
    with open("questions.xml", "a") as f:
        f.write(ending_of_xml)


def test():
    # alpha = [2, 3]
    # alpha = 2 * alpha

    print(5%7)