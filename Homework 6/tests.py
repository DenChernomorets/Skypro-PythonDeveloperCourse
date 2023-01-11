import  test
from validators import check_pin as validate_pin


def fixed_tests():
    @test.it("should return False for pins with length other than 4 or 6")
    def basic_test_cases():    
        test.assert_equals(validate_pin("1"),False, "Wrong output for '1'")
        test.assert_equals(validate_pin("12"),False, "Wrong output for '12'")
        test.assert_equals(validate_pin("123"),False, "Wrong output for '123'")
        test.assert_equals(validate_pin("12345"),False, "Wrong output for '12345'")
        test.assert_equals(validate_pin("1234567"),False, "Wrong output for '1234567'")
        test.assert_equals(validate_pin("-1234"),False, "Wrong output for '-1234'")
        test.assert_equals(validate_pin("-12345"),False, "Wrong output for '-12345'")
        test.assert_equals(validate_pin("1.234"),False, "Wrong output for '1.234'")
        test.assert_equals(validate_pin("00000000"),False, "Wrong output for '00000000'")
    
    @test.it("should return False for pins which contain characters other than digits")
    def _():
        test.assert_equals(validate_pin("a234"),False, "Wrong output for 'a234'")
        test.assert_equals(validate_pin(".234"),False, "Wrong output for '.234'")
    
    @test.it("should return True for valid pins")
    def _():
        test.assert_equals(validate_pin("1234"),True, "Wrong output for '1234'")
        test.assert_equals(validate_pin("0000"),True, "Wrong output for '0000'")
        test.assert_equals(validate_pin("1111"),True, "Wrong output for '1111'")
        test.assert_equals(validate_pin("123456"),True, "Wrong output for '123456'")
        test.assert_equals(validate_pin("098765"),True, "Wrong output for '098765'")
        test.assert_equals(validate_pin("000000"),True, "Wrong output for '000000'")
        test.assert_equals(validate_pin("123456"),True, "Wrong output for '123456'")
        test.assert_equals(validate_pin("090909"),True, "Wrong output for '090909'")
    
    @test.it("should handle edge cases")
    def _():
        tests = [
            '',
            '123',
            '12345',
            '1234567',
            '1234567890',
            '1234x',
            '123456x',
            '12.0',
            '1234.0',
            '123456.0',
            '123\n',
            '1234\n',
            '09876\n',
            '098765\n',
            '-111',
            '111-',
            '-44444',
            '44444-',
            '+111',
            '+88888',
            '+1111',
            '-2018',
            '+234567',
            '-234567',
            '123/',
            '456:',
            '\xbe', # "three quarters" in Python 3, just some byte in Python 2
        ]
        for s in tests:
            test.assert_equals(validate_pin(s), False, "Wrong output for '{}'".format(s))
    
def random_tests():
        
    from random import randint, choice
    from string import ascii_letters, punctuation, digits
        
    all_chars = ascii_letters + punctuation + digits
        
    def solution(pin):
        return len(pin) in (4, 6) and pin.isdigit()
        
    def rand_valid_pin():
        length = 4 if randint(0, 1) else 6
        return "".join(choice(digits) for _ in range(length))
        
    def rand_pin():
        return "".join(choice(all_chars) for _ in range(randint(0, 10)))
        
    for _ in range(40):
        pin = rand_pin() if randint(0, 1) else rand_valid_pin()
        @test.it(f"testing for validate_pin({pin})")
        def test_case():    
            test.assert_equals(validate_pin(pin),solution(pin))