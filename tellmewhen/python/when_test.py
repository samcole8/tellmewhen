import when

def test_gen_crontab():
    print(when.gen_crontab({'test': ['', 'set', '0 0 31 2 *']}))