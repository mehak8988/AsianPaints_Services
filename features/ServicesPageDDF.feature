Feature: Services

  Scenario: validate Enquire Now Functionality with valid data
      Given Chrome is opened and asian paints app is opened
      When  customer is able to click on services link
      When  user enters <name> and <email> and <mobile> and <pincode>
      And   customer clicks on Enquire Now Button
      Then  it shows valid search result page 2


