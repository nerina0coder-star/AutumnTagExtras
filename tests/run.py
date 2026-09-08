import unittest

from Autumn import new

from AutumnTagExtras import Branch


class Run:

    def __init__(self):
        self.successful = {}

    def run(self):
        methods = list(filter(lambda x: x.startswith("run_") and x != "run_all", dir(self)))

        for method in methods:
            getattr(self, method)()

        if False in self.successful.values():
            raise AssertionError("One or more tests failed.")

    def run_all(self):
        self._load()
        test = unittest.loader.TestLoader().discover('tests', pattern='test_*.py')
        result = unittest.TextTestRunner(verbosity=2).run(test)
        self.successful["all"] = result.wasSuccessful()

    def run_containers(self):
        self._load()
        test = unittest.loader.TestLoader().discover('tests', pattern='test_containers.py')
        result = unittest.TextTestRunner(verbosity=2).run(test)
        self.successful["containers"] = result.wasSuccessful()

    def run_texts(self):
        self._load()
        test = unittest.loader.TestLoader().discover('tests', pattern='test_texts.py')
        result = unittest.TextTestRunner(verbosity=2).run(test)
        self.successful["texts"] = result.wasSuccessful()

    def run_phrasings(self):
        self._load()
        test = unittest.loader.TestLoader().discover('tests', pattern='test_phrasings.py')
        result = unittest.TextTestRunner(verbosity=2).run(test)
        self.successful["phrasings"] = result.wasSuccessful()

    def _load(self):
        with new():
            Branch()

if __name__ == "__main__":
    Run().run_all()