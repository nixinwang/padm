import re

def test_regex_match():
    pattern = re.compile(r'.*?gcd.*?')
    source = r'/opt/sdo/tmp/gcd/hub_config.ingres'

    match = pattern.match(source)

    print(match)
    assert match is not None

def test_regex_content_search():
    source = "This is testing string"
    pattern = re.compile(r'test')
    found = pattern.search(source)
    print(found.string)
    assert found is not None

    another = "this has no content"
    found = pattern.search(another)
    assert found is None

if __name__ == '__main__':
    test_regex_match()