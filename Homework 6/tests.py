
from validators import check_pin, check_mail, check_name, check_pass

def test_check_pin():
    '''
    False tests
    '''
    assert check_pin('1234') == False
    assert check_pin('1111') == False
    assert check_pin('qwe') == False
    assert check_pin('112') == False
    assert check_pin('') == False
    assert check_pin('00001') == False
    assert check_pin('-123') == False
    '''
    True tsts
    '''
    assert check_pin('3332') == True
    assert check_pin('1100') == True
    assert check_pin('8954') == True

def test_check_mail():
    '''
    False tests
    '''
    assert check_mail('alabuga.ru') == False
    assert check_mail('alabugaru') == False
    assert check_mail('alabuga@ru') == False
    assert check_mail('alabugaru@') == False
    assert check_mail('alabugaru.') == False
    assert check_mail('@.') == False
    assert check_mail('@alabuga') == False
    assert check_mail('.alabuga') == False
    assert check_mail('@ga.ru') == False
    assert check_mail('alabu@.ru') == False
    assert check_mail('alabu@ga.') == False
    '''
    True tests
    '''
    assert check_mail('alabu@ga.ru') == True
    
def test_check_name():
    '''
    False test
    '''
    assert check_name('Denis') == False
    assert check_name('Денис_Черноморец') == False
    assert check_name('Денис+Черноморец') == False
    assert check_name('Денис Chernomorets') == False
    assert check_name('Денис123') == False
    '''
    True tests
    '''
    assert check_name('Денис Черноморец') == False
    assert check_name('Денис') == False
    assert check_name('ДенисЧерноморец') == False
    assert check_name('ДеНиС') == False
    assert check_name('денис') == False


def test_check_pass():
    '''
    False tests
    '''
    assert check_pass('123') == False
    assert check_pass('123qwe') == False
    assert check_pass('verylongpass') == False
    assert check_pass('12313144123') == False
    assert check_pass('qwe') == False
    assert check_pass('qwertyuio1234_}[]";') == False
    assert check_pass('') == False
    '''
    True tests
    '''
    assert check_pass('longpass12341') == True
    assert check_pass('12341longpass') == True
    assert check_pass('LoNlOjHg120Hg1') == True
    assert check_pass('qiiyh4912n3') == True
    assert check_pass('KJHIHBJ71BHj1') == True
    assert check_pass('1Juubhakqwda') == True
