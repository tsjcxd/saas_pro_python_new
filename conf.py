import os
import configparser

# root dir
base_dir = os.path.dirname(os.path.abspath(__file__))

# read confs/env.in
config = configparser.ConfigParser()
env_path = os.path.join(base_dir, 'confs', 'env.ini')
config.read(env_path)
base_url = config.get(section='test_env', option='test_baseurl')
app_id = config.get(section='test_env', option='app_id')
app_version = config.get(section='test_env', option='app_version')
name = config.get(section='test_env', option='name')
password = config.get(section='test_env', option='password')
nvc_val = r"%7B%22a%22%3A%22FFFF0N0N00000000807F%22%2C%22c%22%3A%221607522481677%3A0.20366057656623404%22%2C%22d%22%3A%22nvc_login%22%2C%22j%22%3A%7B%22test%22%3A1%7D%2C%22h%22%3A%7B%22umidToken%22%3A%22T2gA2j-Cc41U7Epu7d1xCtv4krdpRW5uuXeWQukQ1O_yiHq52OZC4X0p28oErb3MU7mRYJeNJ2ZK7LbGUWrj14gX%22%7D%2C%22b%22%3A%22137%23LIc9hE9o9Yy3fFbmw9d9iHzqIn1BcHTvDD2ecU3DmlEN07%2FWSZwqCCi7idUrF8tjbUPNfsg1nO82646Yp4eZ9XV18c1VoNMRHs%2FyBU2Iyv8uUzeSK8JauPy42uMbRRjK%2FSSKrBSpsHYsm%2BleMloU%2FSUMHFeVytQiXMF1ZhWd35CbXRbSm%2BiiTaykV1epiM6DNZhnCkciPfPLmpt7LN72dph3WPCOgeHbJ1de%2F81PGTTONhDBKNxoq9GAfCx1Qj6PrTBAm8FVlg4XWurgBH5VyGPIrhV66CVED516MTCkO2MyQy7o%2Boz2oC8kRZc5qi1wOJNDiNp2MLXjMoTk8vJnVlP3mQJaOQ2WEEURMCngjd5E3IYT6Icpjc58jyAxBQrcc%2BobbqSV3T6K7ZD7OId99PwCrwVDAAy4h9ojqDrcvJLE5ytjgux128VIfME6Te8RUjBqPi8M%2FlAtLtC755ruODkkUslzgSn1B9VsyArkVf1GF27CP3XOOm2UnpgKrpskUxApDO9h%2BE0BSv%2Bw7ufF05FjRj0BazaU2E70rjsItUByc0q1FIuRphlLkRxGY5K3hi%2Br9A%2BAM0e7SkV14fyOZWR8eZPy7Jy1rH0IKbW15a9jPR25Jv6jCgAbIcoI30Jc1IeivtV66TOSelECpBNcLI2oxmpppkJE1Aey%2BtppYSUS1lQypXiwQonoBf6b5nVc1IBi%2BpiVYSUx1lLyodicQon%2BduYS1kOjDu9IAEUxYrJS1qQipBqmQofJ%2BGXpVkJc1IBy%2BtpVYTUx1lfFdqG9E%2Fg8JzMAz4BAH3nqNKDQzoYsn1byb03Eoi84ST7A8svefSaJvR6oGcvwLzBtTu3OUl1wUFukBwvdv5a%2FdN6gAUY5NJek8ul0U%2FjmeS1K8j20NqQv0JbBC2nBX9guppis91uY4aP9iIS2KIEzyQ0B7p2fpzQNcnadSLXs36f7jO93POITZNjQZXsJgj3GtKzZhBB7ljAV3nNlnuTO2QELd3OJk0xATAxyxc%2FgCcUBCUa5rB%2FBMEjh7zA2q0L8iZRCgZX6xJHj4bUTI%2FWuSRLQD8EWNFJkq9qOlXXbNIK6dUzQ61L6P%2B%2BbBbIqGSinDB2uG8iXt1Kid3X%2B1tX9BKoKIMLv15LjwdzC5BG63eU8PlnnHHj%2Fj5NmCXj1auNYE0%2B3rhL4WtruVTNp7kOhUGSuxTOebc3%2Bp%2BAprZbamQvMM6ig9q7S%2FvMXSYuw%22%2C%22e%22%3A%22O6uZI4ZY4hFcxw-PxHnYqqRoxhdc8gYhD0GXC_r1C9qOu02fmTbbQ8TJwo5S8wQyxFTeobcgqh4RB6SlJnz3dfhP9_15dpnrtSqJnvya92AqwVDaHNZgpMg_4xpYvsTMEAm48ZHXJRNfarQNwp4bK9te7IjH7RPuBOBxh2ZYEXKxNhHyyzjqjekUPz83kk7nuj_r0ZDUxx5o14nClKpcnA%22%7D"

# DB
test_db_info = {
    'host': config.get(section='test_env', option='host'),
    'port': int(config.get(section='test_env', option='port')),
    'user': config.get(section='test_env', option='user'),
    'passwd': config.get(section='test_env', option='passwd'),
    'db': config.get(section='test_env', option='db')
}

if __name__ == '__main__':
    # print(base_dir)
    # print((base_url))
    # print((nvc_val))
    print(test_db_info)
