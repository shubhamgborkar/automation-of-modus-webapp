Feature: Assignments for QA
  Scenario: :Automation of creating a Value Chain
    Given Launch the browser
    When Provide the URL of Modus Webapp Home
    Then Provide Log-in credentials
    Then Click on User Hierarchy
    Then Click on Manage Module
    Then Click on 3rd page of Manage Module Table
    Then Click on View button of Operating Model
    Then Click on Add
    Then Enter “Test Automated Value Chain (Your Name)” in Title field
    Then Select Modus QA Group
    Then Click on Submit
    Then Click on Expand Arrow of Business Team
    Then Click on Expand Arrow of Business Department
    Then Click on Read & Write of Business Role
    Then Click on Save
    Then Click on Ok button of Successful Role Assign alert popup
    Then Click on Save button
    Then Click on Ok button of Successful Submodule Feature alert popup
    Then Select Role dropdown and Select Business Owner
    Then Click on Save 3
    Then Click on OK button of Successful Role Feature alert popup
    Then click on delete button of created submodule
    Then click on yes button of pop up
    And close browser

  Scenario: :Automation of creating Hierarchy Levels in Value Chain
    Given Launch the browser
    When Provide the URL of Modus Webapp Home
    Then Provide Log-in credentials
    Then Click on Operating Model
    Then Click on Operating Model Submodule X
    Then Click on Add Header Level button
    Then Enter Title “Test Automated Levels”
    Then Enter Description “automation”
    Then Select Publish Checkbox of L0 popup
    Then Click on Save button2
    Then Click on OK button of Successful alert popup
    Then Click on Add icon of Level Zero
    Then Enter Title “Test Automated Level Zero C1”
    Then Enter Description “Description L0 C1”
    Then Select Publish Checkbox of Level zero popup
    Then Click on Save button3
    Then Click on OK button of Successful Level Zero alert popup
    Then Click on Add icon of Level One
    Then Enter Title “Test Automated Level One C1”
    Then Enter Description “Description L1 C1”
    Then Enter Short Description “L1A”
    Then Select Team as Business Team
    Then Select Department as Business Department
    Then Select Role as Business Owner
    Then Select Publish Checkbox of Level One popup.
    Then Click on Save button4.
    Then Click on OK button of Successful Level One alert popup
    #-------------------reverse automation----------------------------------------
    Then Click on Delete icon of created Level One
    Then Click on OK button of Level One delete alert popup
    Then Click on Delete icon of created Level Zero
    Then Click on OK button of Level Zero delete alert popup
    Then Click on Delete icon of created Header Level
    Then Click on OK button of Header Level delete alert popup
    And close browser
