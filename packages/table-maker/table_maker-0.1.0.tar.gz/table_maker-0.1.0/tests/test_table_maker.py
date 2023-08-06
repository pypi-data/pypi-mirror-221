"""Test suite""" 

def test_make_table() -> None: 
    """test the make_table function"""
    cols = ('dist. (ft)', 'contested?', 'result')
    rows = (('15', 'yes', 'miss'), ('27', 'no', 'miss'), ('03', 'no', 'make'))
    expected = '\n'.join(
        ('+------------+------------+------------+',
          '| dist. (ft) | contested? | result     |',
          '+============+============+============+',
          '| 03         | no         | make       |',
          '+------------+------------+------------+',
          '| 15         | yes        | miss       |',
          '+------------+------------+------------+',
          '| 27         | no         | miss       |',
          '+------------+------------+------------+'))
    assert make_table(rows, cols, spacing=3) == expected

     
