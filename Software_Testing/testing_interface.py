# testing programmatic interface
# author Xiaoqin LI

import coverage
coverage.erase()
coverage.start()
import SplayTree_testing
SplayTree_testing.test()
coverage.stop()
coverage.analysis(SplayTree_testing)
coverage.report(SplayTree_testing)
