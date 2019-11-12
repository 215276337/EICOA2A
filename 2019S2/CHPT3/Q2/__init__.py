import check50
import check50.c

@check50.check()
def exists():
    """chpt3q2.c exists"""
    check50.exists("chpt3q2.c")
    
@check50.check(exists)
def compiles():
    """chpt3q2.c compiles"""
    check50.c.compile("chpt3q2.c")
    
@check50.check(compiles)
def test1():
    """First condition is true\nSecond condition is false\nThird condition is true"""
    check50.run("./question3").stdout("First condition is true\nSecond condition is false\nThird condition is true", regex=True).exit(0)
