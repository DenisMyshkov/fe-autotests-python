import pytest
import allure


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(scope="function", autouse=True)
def screenshot_when_test_has_failed(app, request):
    yield
    if request.node.rep_call.failed:
        try:
            allure.attach(app.driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
        except:
            pass
