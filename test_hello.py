from hello import more_hallo, more_goodbye


def test_more_hallo():
    assert more_hallo() == "hi"


def test_more_goodbye():
    assert more_goodbye() == "bye"
