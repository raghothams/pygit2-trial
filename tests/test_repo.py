
from pygit2 import init_repository
from pygit2 import clone_repository
from pygit2 import Repository


def test_init():

    repo = init_repository("test-repo")
    print repo

test_init()

