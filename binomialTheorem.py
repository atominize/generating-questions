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
        if self.coe_fir_var < 0:
            self.coe_fir_arr.append("-")
            self.coe_fir_arr.append(abs(self.coe_fir_var))
        else:
            self.coe_fir_arr = ["+", self.coe_fir_var]

        if self.coe_sec_var < 0:
            self.coe_sec_arr = ["-", abs(self.coe_sec_var)]
        else:
            self.coe_sec_arr = ["+", self.coe_sec_var]

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
