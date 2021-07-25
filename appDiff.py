from math import log, exp

beginning_of_xml = """
<?xml version="1.0" encoding="UTF-8"?>
<quiz>
"""
ending_of_xml = """
</quiz>
"""


def print_question(a, b, t_answer, s_answer):
    # a = 0.24
    # b = 0.12
    expression = f"C(t)=0.005e^{{{a}t}}+0.495e^{{{-b}t}}"
    # t_answer = 11
    # s_answer = 0.2
    question = f"""
    <question type="cloze">
    <name>
      <text>1</text>
    </name>
        <questiontext format="html">
              <text><![CDATA[<p>Consider a medical experiment in which a breast tumor patient is 
              given a chemotherapeutic drug. At the time of the drug being administered, the average 
              tumor size was about $$0.50cm^3$$. The tumor volume after t days is modeled by
               $${expression}$$
            given time frame of $$0 \le t \le 16$$<br> </p>
        <p>At what time frame do we expect a critical change in the tumor<br> 
        {{2:NM:={t_answer}}} days (Should be an integer)<br> </p>
        <p></p>
        <p></p>
        <p>What is the nature of the obtained critical time<br> 
        {{1:SHORTANSWER:=local minimum point}} (Use lowercase)<br> </p>
        <p></p>
        <p>What is the size of the tumor with respect to the critical time<br> 
        {{1:NM:={s_answer}}} $$cm^{{2}}$$ (Answer to two decimal places). </p>
        <p></p>
        <p></p>]]></text>
            </questiontext>
            <generalfeedback format="html">
              <text></text>
            </generalfeedback>
            <penalty>0.1</penalty>
            <hidden>0</hidden>
            <idnumber></idnumber>
        </question>
"""
    return question


def start():
    a = 0.24
    b = 0.12
    with open("questions.xml", "w") as f:
        f.write(beginning_of_xml)
    for i in range(1, 11):
        for j in range(1, 11):
            new_a = i*a
            new_b = j*b
            first_dif = [0.005 * new_a, 0.495 * (-new_b)]
            cri_t = -(1 / (new_a + new_b)) * log(-(first_dif[0] / first_dif[1]))
            cri_round_t = round(cri_t)
            exp_cri = (0.005 * exp((new_a * cri_t))) + (0.495 * exp((-new_b * cri_t)))
            exp_cri_round = round(exp_cri, 2)
            with open("questions.xml", "a") as f:
                f.write(print_question(new_a, new_b, cri_round_t, exp_cri_round))
    with open("questions.xml", "a") as f:
        f.write(ending_of_xml)


def test():
    a = 0.24
    b = 0.12
    t_answer = 11
    s_answer = 0.2
    for i in range(1, 11):
        for j in range(1, 11):
            new_a = i*a
            new_b = j*b
            # print(new_a, new_b)
            expression = f"C(t)=0.005e^{{{new_a}t}}+0.495e^{{{-new_b}t}}"
            first_dif = [0.005*new_a, 0.495*(-new_b)]
            # print(first_dif)
            second_dif = [new_a*first_dif[0], -new_b*first_dif[1]]
            # print(second_dif)
            cri_t = -(1 / (new_a + new_b))*log(-(first_dif[0] / first_dif[1]))
            cri_round_t = round(cri_t)
            sec_dif_cri = (second_dif[0]*exp((new_a*cri_t)))+(second_dif[1]*exp((-new_b*cri_t)))
            exp_cri = (0.005 * exp((new_a * cri_t))) + (0.495 * exp((-new_b * cri_t)))
            print(round(exp_cri, 2))
            # print(new_a, new_b, cri_t, cri_round_t)