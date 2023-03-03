Feature: services
  Background: AsianPaintsNavigation
    Given  Chrome is opened and Asian Paints app is opened
    When   user clicks on Not Now button

  Scenario: Successful Navigation on service page
      When  customer is able to click on services link
      Then  It shows services page
  Scenario: Successfully able to click on know more button
      When  customer is able to click on services link
      When  customer is able to click on Know More Button
      Then  It shows the page Safe Painting Services:Home Painting Services For Interior & Exterior House Painting - Asian Paints

  Scenario: Successfully able to click on Expand Button
      When  customer is able to click on services link
       And  customer is able to click on Expand Button
      Then  It show content

  Scenario Outline: validate Enquire Now Functionality with valid data
      When  customer is able to click on services link
      When  customer enters <validname> and <validemail> and <validmobile> and <validpincode>
      And   customer clicks on Enquire Now Button
      Then  it shows Thank you image

    Examples:
      | validname   | validemail      | validmobile | validpincode     |
      | john        | john1@gmail.com | 6005888975  | 123456           |
      | dev         | dev34@gmail.com | 7788654377  | 119988           |

  Scenario Outline: validate Enquire Now Functionality with invalid data
      When  customer is able to click on services link
      When  customer enters <invalidname> and <invalidemail> and <invalidmobile> and <invalidpincode>
      And   customer clicks on Enquire Now Button
      Then  It is on the same page

    Examples:
        | invalidname | invalidemail  | invalidmobile | invalidpincode |
        | @#$*        | johngmail.com | 0123456789    | 123            |
        | ####        | dev34@        | 99@88$4       | 11998866       |
