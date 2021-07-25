from math import comb


# def check_for_neg(term):
#     if str(term).find("-") != -1:
#         return True
#     else:
#         return False


# def get_value_from_sign(sign):
#     if sign == "-":
#         return -1
#     else:
#         return 1


def format_variable(variable):
    if variable < 0:
        return ["-", abs(variable)]
    else:
        return ["+", variable]


class BinomialTheorem:
    def __init__(self, first_var, coe_fir_var, second_var, coe_sec_car, power):
        self.coefficients = []
        self.terms = []
        self.first_var = first_var
        self.coe_fir_var = coe_fir_var
        self.second_var = second_var
        self.coe_sec_var = coe_sec_car
        self.coe_fir_arr = []
        self.coe_sec_arr = []
        self.power = power
        self.format_variables()
        self.expression = f"({self.coe_fir_arr[0] if self.coe_fir_arr[0] == '-' else ''}" \
                          f"{self.coe_fir_arr[1] if self.coe_fir_arr[1] > 1 else ''}{self.first_var} " \
                          f"{self.coe_sec_arr[0]} {self.coe_sec_arr[1] if self.coe_sec_arr[1] > 1 else ''}" \
                          f"{self.second_var})^{{{self.power}}}"

    def format_variables(self):
        self.coe_fir_arr = format_variable(self.coe_fir_var)
        self.coe_sec_arr = format_variable(self.coe_sec_var)

    def get_terms(self):
        n = int(self.power)
        for item in range(0, n+1):
            if item == 0:
                term = f"{self.first_var}^{{{n - item}}}"
            elif item == n-1:
                term = f"{self.first_var}{self.second_var}^{{{item}}}"
            elif item == n:
                term = f"{self.second_var}^{{{item}}}"
            elif item == 1:
                term = f"{self.first_var}^{{{n - item}}}{self.second_var}"
            else:
                term = f"{self.first_var}^{{{n - item}}}{self.second_var}^{{{item}}}"
            self.terms.append(term)
        return self.terms

    def get_coefficients(self):
        n = int(self.power)
        for item in range(0, n + 1):
            coefficient = (self.coe_fir_var**(n - item))*(self.coe_sec_var**item)*comb(n, item)
            self.coefficients.append(coefficient)
        return self.coefficients

    def expansion(self):
        expansion = f"{self.expression} = "
        coefficients = self.get_coefficients()
        terms = self.get_terms()
        expansion = expansion + f"{'-' if coefficients[0] < 0 else ''}" \
                                f"{'' if abs(coefficients[0]) == 1 else abs(coefficients[0])}{terms[0]}"
        for item in range(1, self.power + 1):
            expansion = expansion + f" {'-' if coefficients[item] < 0 else '+'} " \
                                    f"{abs(coefficients[item]) if abs(coefficients[item]) > 1 else ''}{terms[item]}"
        return expansion

# x  = BinomialTheorem("x", "y", 5)


class MultinomialTheorem:
    def __init__(self, first_var, coe_fir_var, second_var, coe_sec_car, third_var, coe_thi_var, power):
        self.coefficients = []
        self.terms = []
        self.first_var = first_var
        self.coe_fir_var = coe_fir_var
        self.second_var = second_var
        self.coe_sec_var = coe_sec_car
        self.third_var = third_var
        self.coe_thi_var = coe_thi_var
        self.coe_fir_arr = []
        self.coe_sec_arr = []
        self.coe_thi_arr = []
        self.power = power
        self.format_variables()
        self.expression = f"({self.coe_fir_arr[0] if self.coe_fir_arr[0] == '-' else ''}" \
                          f"{self.coe_fir_arr[1] if self.coe_fir_arr[1] > 1 else ''}{self.first_var} " \
                          f"{self.coe_sec_arr[0]} {self.coe_sec_arr[1] if self.coe_sec_arr[1] > 1 else ''}" \
                          f"{self.second_var} {self.coe_thi_arr[0]} " \
                          f"{self.coe_thi_arr[1] if self.coe_thi_arr[1] > 1 else ''} {self.third_var})^{{{self.power}}}"

    def format_variables(self):
        self.coe_fir_arr = format_variable(self.coe_fir_var)
        self.coe_sec_arr = format_variable(self.coe_sec_var)
        self.coe_thi_arr = format_variable(self.coe_thi_var)

    def get_terms(self):
        n = int(self.power)
        for i in range(0, n+1):
            for j in range(0, n+1):
                if (i + j) > n:
                    break
                k = n - (i + j)
                ith_part = f"{self.third_var}^{{{i}}}"
                jth_part = f"{self.second_var}^{{{j}}}"
                kth_part = f"{self.first_var}^{{{k}}}"
                if k == 0:
                    kth_part = ""
                if j == 0:
                    jth_part = ""
                if i == 0:
                    ith_part =""
                if k == 1:
                    kth_part = self.first_var
                if j == 1:
                    jth_part = self.second_var
                if i == 1:
                    ith_part = self.third_var
                term = f"{kth_part}{jth_part}{ith_part}"
                self.terms.append(term)
        return self.terms

    def expansion(self):
        return self.expression

