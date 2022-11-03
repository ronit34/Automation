Feature: Tuc config labels

  Scenario: Login to Onextel  config labels
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        ####################################################################
        #                     BLACKLIST BUTTON                             #
        ####################################################################
        Then click on Config
        And check the config text
        And check new blacklist button is present
        And check if  Category Name text is present or not
        And check if Total Numbers is present
        And check if  Category Description text is present or not
        And check if  Status text is present or not
        And check if  Action text is present or not
        And click on new blacklist button
        And check if Create Black List Category text is present inside new blacklist button
        And check if Category Name text is present inside new blacklist button
        And check if Category Status text is present inside new blacklist button
        And check if Category Description text is present inside new blacklist button
        And check the text of create button inside new blacklist button
        And click on the cancel button of new blacklist button

        ###############################################################################
        #                        BLACKLIST NUMBER                                    #
        ###############################################################################
        And check the text of BlackList Number tab
        And click on Black List Number
        And check the text of Add Blacklist Number tab
        And check if  Name text is present or not inside blacklist number tab
        And check if  Description text is present or not inside blacklist number tab
        And check if  Category text is present or not inside blacklist number tab
        And check if  Number text is present or not inside blacklist number tab
        And check the text of add button in tuc config blacklist
        And check if  Select Category text is present or not inside blacklist number tab
        And check if  Select Number(Optional) text is present or not inside blacklist number tab
        And check the text of limit in blacklist number
        And check the text of search in blacklist number
        And check the text of Delete Selected in blacklist number
        And check the text of Delete All in blacklist number
        And check the text of Upload Blacklist Number
        And click on Upload Blacklist Number
        And check text of Downlaod Sample file of Blacklist Number
        And check if Select Category Blacklist text is present or not is present inside category blacklist
        And check the text of upload button
        And check the text of Download Blacklist Number
        And click on Download Blacklist Number
        And check if  Category text is present or not inside download blacklist number tab
        And check if  File Type text is present or not
        And check if download button text is present or not
        ##########################################################################################
        #                          WHITELIST CATEGORY                                            #
        ##########################################################################################
        And check the text of Whitelist Category tab
        And click on White List Category
        And check if Category Name text is present inside Whitelist Category tab or not
        And check if total numbers text is present inside Whitelist Category tab or not
        And check if Category Description text is present inside Whitelist Category tab or not
        And check if Status text is present inside Whitelist Category tab or not
        And check if Action text is present inside Whitelist Category tab or not
        And check new Whitelist button is present
        And click on new Whitelist button
        And check if Create Whitelist Category text is present inside new whilelist button or not
        And check if Category Name text is present inside new whilelist button or not
        And check if Category Status text is present inside new whilelist button or not
        And check if Category Description text is present inside new whilelist button or not
        And check if text or create button is present or not
        And check the text of cancel button and click on it if it is present
        ############################################################################################
        #                        WHITELIST NUMBER                                                  #
        ############################################################################################
        And check the text of Whitelist Number tab
        And click on white list number
        And check the text of Add Whitelist Number tab
        And check if  Name text is present or not inside whitelist number tab
        And check if  Description text is present or not inside whitelist number tab
        And check if  Category text is present or not inside whitelist number tab
        And check if  Number text is present or not inside whitelist number tab
        And check the text of add button in tuc config Whitelist
        And check if  Select Category text second is present or not inside whitelist number tab
        And check if  Select Number(Optional) text is present or not inside whitelist number tab
        And check the text limit inside Add whitelist number tab
        And check the text of search in whitelist number
        And check the text of Delete Selected in whitelist number
        And check the text of Delete All in whitelist number
        And check the text of Upload Whitelist Number tab
        And click on Upload Whitelist Number tab
        And check text of Downlaod Sample file of Whitelist Number
        And check if Select Category Whitelist inside Upload Whitelist Number tab
        And check the upload button text inside Upload Whitelist Number tab
        And check the text of Download Whitelist Number tab
        And click on Download Whitelist Number
        And check if text Category is present or not inside Download Whitelist Number tab
        And check if text File Type is present or not inside Download Whitelist Number tab
        And check the Download button text inside Download Whitelist Number tab

        And Close driver window