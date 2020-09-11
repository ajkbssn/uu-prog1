from uu_prog1.word_count import lines_to_list


def test_lines_to_list():
    lines = [["Här kommer rad ETT!\n"], ["Och här är andra raden.\n"]]
    assert len(lines_to_list(lines)) == 9
