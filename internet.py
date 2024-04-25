from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

@given(u'Launch the browser')
def launch(context):
    context.driver=webdriver.Edge()
    context.driver.maximize_window()


@when(u'Provide the URL of Modus Webapp Home')
def page(context):
    context.driver.get('https://modusretail.azurewebsites.net/Pages/Hierarchy/home.aspx')
    context.driver.implicitly_wait(2)


@then(u'Provide Log-in credentials')
def login(context):
     context.driver.find_element("name","loginfmt").send_keys('QA-Assignment@outlook.com')
     context.driver.find_element("xpath","//input[@id='idSIButton9']").click()
     time.sleep(4)
     context.driver.find_element("xpath","//input[@id='i0118']").send_keys('qa-assign10')
     context.driver.find_element("id", "idSIButton9").click()
     time.sleep(3)
     context.driver.find_element("id","declineButton").click()

@then(u'Click on User Hierarchy')
def user(context):
    time.sleep(8)
    context.driver.find_element("xpath","//body/form[@id='form1']/div[@id='s4-workspace']/div[@id='s4-bodyContainer']/div[4]/a[1]/div[1]").click()

@then(u'Click on Manage Module')
def manage(context):
    context.driver.find_element("xpath","//a[@id='MainContent_M_DisplayPageNavigationControl_MoDataList_HyperLink1_2']").click()


@then(u'Click on 3rd page of Manage Module Table')
def threepage(context):
    context.driver.find_element("xpath","//a[contains(text(),'3')]").click()


@then(u'Click on View button of Operating Model')
def optmodel(context):
    time.sleep(2)
    context.driver.find_element("xpath", "//input[@id='MainContent_ModuleSubModule_grdModule_btnViewLevel_3']").click()


@then(u'Click on Add')
def add(context):
    time.sleep(2)
    context.driver.find_element("xpath", "//input[@id='MainContent_ModuleSubModule_btnAddNew']").click()


@then(u'Enter “Test Automated Value Chain (Your Name)” in Title field')
def title(context):
    time.sleep(1)
    context.driver.find_element("xpath", "//input[@id='MainContent_ModuleSubModule_txtName']").click()
    context.driver.find_element("xpath", "//input[@id='MainContent_ModuleSubModule_txtName']").send_keys('Test Automated Value Chain (Shubham Borkar)')


@then(u'Select Modus QA Group')
def group(context):
    Drop = context.driver.find_element("xpath", "//select[@id='MainContent_ModuleSubModule_ddlSelectModuleGroup']")
    select = Select(Drop)
    select.select_by_visible_text('Modus QA Group')


@then(u'Click on Submit')
def submit(context):
    context.driver.find_element("xpath","//input[@id='MainContent_ModuleSubModule_btnOkay']").click()


@then(u'Click on Expand Arrow of Business Team')
def bussteam(context):
    time.sleep(20)
    context.driver.find_element("xpath","//body/form[@id='form1']/div[@id='s4-workspace']/div[@id='s4-bodyContainer']/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/ul[2]/li[1]/span[1]").click()


@then(u'Click on Expand Arrow of Business Department')
def bussdept(context):
    context.driver.find_element("xpath","//body/form[@id='form1']/div[@id='s4-workspace']/div[@id='s4-bodyContainer']/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/ul[2]/li[1]/ul[1]/ul[1]/li[1]/span[1]").click()


@then(u'Click on Read & Write of Business Role')
def bussrole(context):
    context.driver.find_element("xpath","//body/form[@id='form1']/div[@id='s4-workspace']/div[@id='s4-bodyContainer']/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/ul[2]/li[1]/ul[1]/ul[1]/li[1]/ul[1]/ul[1]/li[1]/ul[2]/li[1]/label[1]/input[1]").click()


@then(u'Click on Save')
def save(context):
    time.sleep(2)
    context.driver.find_element("xpath", "//input[@id='BtnSave_SubModulePermissionMapping UHAllbuttonColors']").click()


@then(u'Click on Ok button of Successful Role Assign alert popup')
def pop(context):
    time.sleep(2)
    alt = context.driver.switch_to.alert
    alt.accept()

@then(u'Click on Save button')
def save2(context):
    time.sleep(3)
    context.driver.find_element("xpath","//input[@id='btnSaveSubModuleFeatureMapping']").click()


@then(u'Click on Ok button of Successful Submodule Feature alert popup')
def popup(context):
    time.sleep(2)
    alt = context.driver.switch_to.alert
    alt.accept()


@then(u'Select Role dropdown and Select Business Owner')
def step_impl(context):
    time.sleep(6)
    dop = context.driver.find_element("xpath", "//select[@id='DdlRoleValues']")
    select = Select(dop)
    select.select_by_visible_text('Business Role')


@then(u'Click on Save 3')
def save3(context):
    time.sleep(3)
    context.driver.find_element("xpath", "//input[@id='btnSaveFeatureRolePermissionMapping']").click()  # save


@then(u'Click on OK button of Successful Role Feature alert popup')
def popups(context):
    time.sleep(2)
    alt = context.driver.switch_to.alert
    alt.accept()


@then(u'click on delete button of created submodule')
def delete(context):
    time.sleep(1)
    context.driver.find_element("xpath"," //input[@id='MainContent_ModuleSubModule_grdModule_btnDelete_0']").click()


@then(u'click on yes button of pop up')
def popups(context):
    time.sleep(2)
    context.driver.find_element("xpath", "// input[ @ id = 'MainContent_ModuleSubModule_btnDeleteModule']").click()


@then(u'close browser')
def close(context):
    time.sleep(30)
    context.driver.close()

#assignment 2-------------------------------------------------------------------------------------------------------------------------

@then(u'Click on Operating Model')
def opt(context):
    context.driver.find_element("xpath", "//a[@id='MainContent_M_HomeControl_dtlist1_hypModule1_1']").click()


@then(u'Click on Operating Model Submodule X')
def sub(context):
    context.driver.find_element("xpath", "//body/form[@id='form1']/div[@id='s4-workspace']/div[@id='s4-bodyContainer']/div[3]/div[2]/div[1]/ul[1]/li[2]/a[1]/i[1]").click()
    time.sleep(2)
    context.driver.find_element("xpath", "//a[@id='MainContent_M_SubModulesControl1_rptAccordianContent_dtlist_1_hypModule_149']").click()


@then(u'Click on Add Header Level button')
def addheader(context):
    context.driver.find_element("xpath","//span[contains(text(),'Add Header Level')]").click()



@then(u'Enter Title “Test Automated Levels”')
def title1(context):
    time.sleep(1)
    context.driver.find_element("xpath","//input[@id='txtHeaderTitle']").send_keys('Test Automated Levels')


@then(u'Enter Description “automation”')
def des1(context):
    time.sleep(1)
    context.driver.find_element("xpath", "//textarea[@id='txtHeaderDescription']").send_keys('Automation')


@then(u'Select Publish Checkbox of L0 popup')
def pub1(context):
    context.driver.find_element("xpath", "//input[@id='chkHeader']").click()


@then(u'Click on Save button2')
def saveb1(context):
    context.driver.find_element("xpath", "//body/div[@id='s4-workspace']/div[@id='LayoutDiv']/div[@id='divAddNew']/div[1]/div[1]/div[2]/div[2]/button[1]/span[2]").click()


@then(u'Click on OK button of Successful alert popup')
def popups(context):
    time.sleep(2)
    alt = context.driver.switch_to.alert
    alt.accept()


@then(u'Click on Add icon of Level Zero')
def zero(context):
    time.sleep(2)
    context.driver.find_element("xpath", "//tbody/tr[1]/td[1]/div[1]/div[4]/*[1]").click()



@then(u'Enter Title “Test Automated Level Zero C1”')
def title2(context):
    time.sleep(1)
    context.driver.find_element("xpath", " //input[@id='txtTitle']").send_keys('Test Automated Level Zero C1')



@then(u'Enter Description “Description L0 C1”')
def desc2(context):
    time.sleep(1)
    context.driver.find_element("xpath", "//textarea[@id='txtDescription']").send_keys('Description L0 C1')


@then(u'Select Publish Checkbox of Level zero popup')
def publish2(context):
    context.driver.find_element("xpath", "//input[@id='chk']").click()


@then(u'Click on Save button3')
def saveb2(context):
    context.driver.find_element("xpath", "//body/div[@id='s4-workspace']/div[@id='LayoutDiv']/div[@id='divAddNewZeroLvl']/div[1]/div[1]/div[2]/div[2]/button[1]/span[2]").click()

@then(u'Click on OK button of Successful Level Zero alert popup')
def popups(context):
    time.sleep(2)
    alt = context.driver.switch_to.alert
    alt.accept()

@then(u'Click on Add icon of Level One')
def one(context):
    time.sleep(1)
    context.driver.find_element("xpath", "//img[@id='btnAddNewLevelOne']").click()


@then(u'Enter Title “Test Automated Level One C1”')
def title3(context):
    time.sleep(1)
    context.driver.find_element("xpath", "//input[@id='txtTitleLevelOne']").send_keys('Test Automated Level One C1')


@then(u'Enter Description “Description L1 C1”')
def desc3(context):
    context.driver.find_element("xpath", "//textarea[@id='txtDescriptionLevelOne']").send_keys('Description L1 C1')


@then(u'Enter Short Description “L1A”')
def shortdesc(context):
    context.driver.find_element("xpath", "//input[@id='txtShortDescriptionLevelOne']").send_keys('L1A')


@then(u'Select Team as Business Team')
def team(context):
    time.sleep(2)
    context.driver.find_element("xpath", "//body/div[@id='s4-workspace']/div[@id='LayoutDiv']/div[@id='divAddNewLevelOne']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/div[2]/span[1]/span[1]/div[1]/button[1]").click()
    time.sleep(1)
    context.driver.find_element("xpath", "//body/div[@id='s4-workspace']/div[@id='LayoutDiv']/div[@id='divAddNewLevelOne']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/div[2]/span[1]/span[1]/div[1]/ul[1]/li[4]/a[1]/label[1]/input[1]").click()
    context.driver.find_element("xpath", "//body/div[@id='s4-workspace']/div[@id='LayoutDiv']/div[@id='divAddNewLevelOne']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/div[1]/label[1]").click()


@then(u'Select Department as Business Department')
def bussdepartment(context):
    time.sleep(2)
    context.driver.find_element("xpath", "//span[contains(text(),'Select Department')]").click()
    time.sleep(1)
    context.driver.find_element("xpath", "//body/div[@id='s4-workspace']/div[@id='LayoutDiv']/div[@id='divAddNewLevelOne']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[7]/div[2]/span[1]/span[1]/div[1]/ul[1]/li[2]/a[1]/label[1]/input[1]").click()
    context.driver.find_element("xpath", "//body/div[@id='s4-workspace']/div[@id='LayoutDiv']/div[@id='divAddNewLevelOne']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/div[1]/label[1]").click()


@then(u'Select Role as Business Owner')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element("xpath", "//span[contains(text(),'Select Role')]").click()
    time.sleep(1)
    context.driver.find_element("xpath", "//body/div[@id='s4-workspace']/div[@id='LayoutDiv']/div[@id='divAddNewLevelOne']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/div[2]/span[1]/span[1]/span[1]/div[1]/ul[1]/li[2]/a[1]/label[1]/input[1]").click()
    context.driver.find_element("xpath", "//body/div[@id='s4-workspace']/div[@id='LayoutDiv']/div[@id='divAddNewLevelOne']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/div[1]/label[1]").click()


@then(u'Select Publish Checkbox of Level One popup.')
def publish(context):
    context.driver.find_element("xpath", "//input[@id='chkLevelOne']").click()


@then(u'Click on Save button4.')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element("xpath", "//body/div[@id='s4-workspace']/div[@id='LayoutDiv']/div[@id='divAddNewLevelOne']/div[1]/div[1]/div[3]/button[1]/span[2]").click()


@then(u'Click on OK button of Successful Level One alert popup')
def popups(context):
    time.sleep(2)
    alt = context.driver.switch_to.alert
    alt.accept()



#--------------------------------------Reversal assignment 2------------------------------------------------------------------
@then(u'Click on Delete icon of created Level One')
def delone(context):
    time.sleep(2)
    context.driver.find_element("xpath","//tbody/tr[2]/td[1]/div[1]/div[5]/span[1]/img[1]").click()
    time.sleep(3)
    context.driver.switch_to.alert.accept()

@then(u'Click on OK button of Level One delete alert popup')
def popups(context):
    time.sleep(7)
    alt = context.driver.switch_to.alert
    alt.accept()

@then(u'Click on Delete icon of created Level Zero')
def delzero(context):
    time.sleep(2)
    context.driver.find_element("xpath","//img[@id='btnDelete']").click()
    context.driver.switch_to.alert.accept()

@then(u'Click on OK button of Level Zero delete alert popup')
def popups(context):
    time.sleep(2)
    alt = context.driver.switch_to.alert
    alt.accept()

@then(u'Click on Delete icon of created Header Level')
def delhead(context):
    time.sleep(2)
    context.driver.find_element("xpath","//tbody/tr[1]/td[1]/div[1]/div[5]/*[1]").click()
    context.driver.switch_to.alert.accept()

@then(u'Click on OK button of Header Level delete alert popup')
def popups(context):
    time.sleep(2)
    alt = context.driver.switch_to.alert
    alt.accept()