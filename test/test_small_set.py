from small_set import SmallSet

def test_adds():
    s = SmallSet()
    s.add(3)
    assert s.contains(3)
    assert not s.contains(5)

def test_removes():
    s = SmallSet()
    s.add(10)
    s.add(15)
    s.remove(10)
    assert s.contains(15)
    assert not s.contains(10)
