from gendiff.comparer import generate_diff


def test_generate_diff():
    pathfile1 = 'tests/fixtures/file1.json'
    pathfile2 = 'tests/fixtures/file2.json'
    with open(pathfile1, 'r'):
        with open(pathfile2, 'r'):
            with open('tests/fixtures/result_json', 'r') as result:
                result = result.read()
                assert generate_diff(pathfile1, pathfile2) == result
