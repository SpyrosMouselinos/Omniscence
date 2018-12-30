from pytest import fixture
import codecov

@fixture
def op():
    from Omniscence.Data_analysis import OmniAnalyzer
    return OmniAnalyzer(file_dir='test.csv',task='classification', input_size=0, target='no_target')

def test_class_found(op):
    assert op.load() == True
    