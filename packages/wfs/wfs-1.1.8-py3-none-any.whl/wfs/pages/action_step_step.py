from utils.parseexcel import ParseExcel


def get_test_steps(test_object_repo, test_data_json, tstepx, steps_line, testdata, action, actiondesc):
    from utils.action_test_item import get_test_action_data, id_generator
    try:
        data = None
        jsonfile = open(test_data_json, 'w+')
        test_data_item, action_no, action_page_item, action_item, actionxdesc = get_test_action_data(steps_line,
                                                                                                     testdata,
                                                                                                     action, actiondesc)
        # print(test_data_item, action_page_item, action_item, actionxdesc, action_no)
        get_excel_data = ParseExcel(test_object_repo).get_row_all_col_data(sheetname="Object_Repo_BasePage",
                                                                           columnname="BasePage",
                                                                           pagename=action_page_item)
        # print(get_excel_data)
        elementIdentity, locatorIdentity, actionIdentity, description, felements, itemIdentity = get_action_description \
            (get_excel_data, actionxdesc)
        # print('#######################################################################################1')
        # print(elementIdentity, locatorIdentity, actionIdentity, description, felements, itemIdentity)
        # print('#######################################################################################2')
        data = []
        if test_data_item != "***" and action_item != "***" and action_no != '00' or test_data_item == "***" and \
                action_item != "***" and action_no != '00':
            if '&' in locatorIdentity and '&' in elementIdentity and '&' in actionIdentity and '&' in action_item and '&' in felements:
                lIdentity, eIdentity, aIdentity, aItem, tItem, felements = str(locatorIdentity).split('&'), str(
                    elementIdentity).split(
                    '&'), \
                    str(actionIdentity).split('&'), str(action_item).split('&'), str(test_data_item).split('&'), str(
                    felements).split('&')
                for xg in range(0, len(lIdentity)):
                    datax = lIdentity[xg] + '|' + eIdentity[xg] + '|' + aIdentity[xg] + '|' + description + '|' + \
                            tstepx + '|' + aItem[xg] + '|' + tItem[xg] + '|' + felements[xg] + '|' + itemIdentity + \
                            '|' + id_generator()
                    data.append(datax)
                    jsonfile.write(str(datax) + '\n')
            else:
                datax = locatorIdentity + '|' + elementIdentity + '|' + actionIdentity + '|' + description + '|' + \
                        tstepx + '|' + action_item + '|' + test_data_item + '|' + felements + '|' + itemIdentity + \
                        '|' + id_generator()
                data.append(datax)
                jsonfile.write(str(datax) + '\n')
        elif action_no == '00' and action_item != "***":
            datax = 'None|None|None|' + actionxdesc + '|' + \
                    tstepx + '|' + action_item + '|' + test_data_item + '|None|None|' + id_generator()
            data.append(datax)
            jsonfile.write(str(datax) + '\n')
        else:
            data = data
        # print(data)
        return data
    except Exception as e:
        return 'Error : ' + str(e)


def get_action_description(get_excel_data, action_description):
    elementIdentity, locatorIdentity, actionIdentity, description, felements, itemIdentity = None, None, None, None, \
        None, None
    for xdescrip in range(0, len(get_excel_data)):
        if action_description == get_excel_data[xdescrip]['Description']:
            elementIdentity = get_excel_data[xdescrip]['Elements']
            locatorIdentity = get_excel_data[xdescrip]['Locators']
            actionIdentity = get_excel_data[xdescrip]['Action']
            description = get_excel_data[xdescrip]['Description']
            felements = get_excel_data[xdescrip]['FetchElements']
            itemIdentity = get_excel_data[xdescrip]['Item']
            break
    return elementIdentity, locatorIdentity, actionIdentity, description, felements, itemIdentity
