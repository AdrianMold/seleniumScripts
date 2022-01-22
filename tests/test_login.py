from TestGroupLogin import TestGroupLogin
"""
Execute test cases
"""
def main():
  test_subject = TestGroupLogin()
  
  # run happy test cases
  test_subject.test_login_should_be_ok("mngr327236", "rehavAs")

  # run sad test cases
  test_subject.test_login_should_not_be_ok("mngr327236", "parolaNOK", " user ok, password nok")
  test_subject.test_login_should_not_be_ok("userNOK", "rehavAs", " user nok, password ok")
  test_subject.test_login_should_not_be_ok("userNOK", "parolaNOK", " user nok, password nok")
  test_subject.test_login_should_not_be_ok("", "rehavAs", " user <empty>, password ok")
  test_subject.test_login_should_not_be_ok("mngr327236", "", " user ok, password <empty>")

  test_subject.teardownTests()


if __name__ == "__main__":
  main()