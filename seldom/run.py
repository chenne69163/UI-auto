import seldom
from seldom import ChromeConfig

if __name__ == '__main__':
    ChromeConfig.executable_path = "/Users/chenneng/Desktop/UI_auto/lib/chromedriver"
    # run test
    # seldom.main("./test_dir/")
    seldom.main(path="./test_dir/test_login.py", browser="chrome", debug=False, timeout=10, save_last_run=True)

