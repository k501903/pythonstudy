import pytest

class TestCase(object):
    def test_eq_set(self):
        assert set([0, 10, 11, 12]) == set([0, 20, 21])

    def test_eq_dict(self):
        assert {'a': 0, 'b': 1, 'c': 0} == {'a': 0, 'b': 2, 'c': 0}

    def test_eq_list(self):
        assert [0, 1, 2] == [0, 1, 3]

    def test_eq_longer_list(self):
        assert [1, 2] == [1, 2, 3]

    def test_eq_num(self):
        assert 3*4 == 13, '测试3*4==13'

@pytest.fixture
def smtp1():
    import smtplib
    return smtplib.SMTP("smtp.qq.com")

def test_ehlo(smtp):
    response, msg = smtp.ehlo()
    assert response == 250
    # assert 0 # for demo purposes