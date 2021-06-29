import tomli_dumps


def test_newline_before_table():
    actual = tomli_dumps.dumps({"table": {}})
    expected = "[table]\n"
    assert actual == expected

    actual = tomli_dumps.dumps(
        {"table": {"nested": {}, "val3": 3}, "val2": 2, "val1": 1}
    )
    expected = """\
val2 = 2
val1 = 1

[table]
val3 = 3

[table.nested]
"""
    assert actual == expected