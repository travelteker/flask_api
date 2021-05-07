from unittest import TestLoader, TestSuite, TextTestRunner

from tests.unit.models.queries.test_search_by_position import TestSearchByPosition
from tests.unit.models.queries.test_search_by_word import TestSearchByWord
from tests.unit.models.queries.test_search_words import TestSearchWords
from tests.unit.models.queries.test_update_word import TestUpdateWord
from tests.unit.models.test_base_queries import TestBaseQueries
from tests.unit.schemas.test_word import TestWordSchema
from tests.unit.utils.responses.structures.test_success import TestSuccess
from tests.unit.utils.logger.test_logger import TestLogger
from tests.unit.utils.filters.test_anagrams import TestAnagrams
from tests.unit.utils.conditions.test_word_repetead import TestWordRepeated
from tests.unit.utils.conditions.test_base import TestBase
from tests.unit.utils.conditions.test_version import TestVersion
from tests.unit.utils.conditions.test_create_dir import TestCreateDir
from tests.unit.utils.conditions.test_operation_mode import TestOperationMode
from tests.unit.models.test_words import TestWords
from tests.unit.models.test_transactions import TestTransactions
from tests.unit.middlewares.headers_middleware import TestHeadersMiddleware
from tests.unit.handlers.test_logger_req_res import TestLoggerReqRes
from tests.unit.handlers.test_register_error import TestRegisterError


def prepare_suite():
    """Generate suite for all tests cases
    :return: TestSuite
    """
    loader = TestLoader()
    suite = TestSuite()

    test_modules = [
        TestSearchByPosition, TestSearchByWord, TestSearchWords, TestUpdateWord,
        TestBaseQueries, TestWordSchema, TestSuccess, TestLogger, TestAnagrams,
        TestWordRepeated, TestBase, TestVersion, TestCreateDir, TestOperationMode,
        TestWords, TestTransactions, TestHeadersMiddleware, TestLoggerReqRes,
        TestRegisterError
    ]

    for module in test_modules:
        suite.addTest(loader.loadTestsFromTestCase(module))
    return suite


if __name__ == "__main__":
    """Entrypoint to execute all unit test case using suite"""
    runner = TextTestRunner(verbosity=1)
    results = runner.run(prepare_suite())
