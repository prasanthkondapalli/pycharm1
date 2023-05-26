from behave import *
from selenium import webdriver




@given('launch chrome browser')
def launchBrowser(context):
    driver=webdriver.chrome("")



@when(u'open application')
def navigateApplication(context):
    raise NotImplementedError(u'STEP: When open application')


@then(u'check the logo of the application')
def verifyingLogo(context):
    raise NotImplementedError(u'STEP: Then check the logo of the application')


@then(u'close the browser')
def closeBrowser(context):
    raise NotImplementedError(u'STEP: Then close the browser')
