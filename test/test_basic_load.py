from pytest import fixture
import codecov


@fixture
def initialized_generator():
    from Omniscence.Data_analysis import OmniAnalyzer
    return OmniAnalyzer(file_dir='test.csv',task='classification', input_size=2, target='target_feature')

@fixture
def loaded_generator():
    from Omniscence.Data_analysis import OmniAnalyzer
    OmniAnalyzer_Generator = OmniAnalyzer(file_dir='test.csv',task='classification', input_size=2, target='target_feature')
    OmniAnalyzer_Generator.load()
    return OmniAnalyzer_Generator

def test_class_load(initialized_generator):
    assert initialized_generator.load() == True
    

def test_class_report(initialized_generator,loaded_generator):
    assert initialized_generator.report() == None
    assert type(loaded_generator.report()) != None

def test_class_analyze(loaded_generator):
    assert loaded_generator.analyze() == True
