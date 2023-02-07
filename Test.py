import json


def main():
    false ='false';
    true ='true'

    input = {
        "acg": [
        {
            "code": "BSMP",
            "globalId": "CFC7CAE1-3F05-411E-BE96-7DEEA7C14686",
            "isDeleted": false,
            "modifiedDate": "",
            "title": "Basic Set-up of Microwave products"
        },
        {
            "code": "CSI",
            "globalId": "0A20AB92-902F-4B83-BB9A-3D47FDA01AA3",
            "isDeleted": false,
            "modifiedDate": "2020-11-10T08:36:52Z",
            "title": "Core Site Installation"
        },
        {
            "code": "ERS",
            "globalId": "4D5274E4-764D-4085-A779-2F462360F10E",
            "isDeleted": false,
            "modifiedDate": "2020-11-10T08:36:52Z",
            "title": "Engineering of Radio Site"
        },
        {
            "code": "IFN-A",
            "globalId": "B0BD0F7A-0078-4D8B-984C-DDF07A0C5339",
            "isDeleted": false,
            "modifiedDate": "2020-11-10T08:36:52Z",
            "title": "IFN-A, Installation of Fiber Networks – Aerial products"
        },
        {
            "code": "IFN-M",
            "globalId": "4F75D599-C88F-45DD-9E5F-29FFAC23BFCB",
            "isDeleted": false,
            "modifiedDate": "2020-11-10T08:36:52Z",
            "title": "IFN-M, Installation of Fiber Networks – Micronet products"
        },
        {
            "code": "IFN-R",
            "globalId": "AD69CD16-F2F7-49FC-9238-6B46A83C3A9C",
            "isDeleted": false,
            "modifiedDate": "2020-11-10T08:36:52Z",
            "title": "IFN-R, Installation of Fiber Networks – Ribbonet products"
        },
        {
            "code": "IESC",
            "globalId": "9A1E4C7E-774D-4922-9308-BE37E03CB8F9",
            "isDeleted": false,
            "modifiedDate": "2020-11-10T08:36:52Z",
            "title": "Installation Ericsson Site Controller"
        },
        {
            "code": "IMP",
            "globalId": "66FCEF80-CAE7-42C9-9626-3D6BBB27E61D",
            "isDeleted": false,
            "modifiedDate": "2020-11-10T08:36:52Z",
            "title": "Installation of MINI-LINK products"
        },
        {
            "code": "ILHP",
            "globalId": "D898FD68-B045-46C9-A944-B13AA3C20F86",
            "isDeleted": false,
            "modifiedDate": "2020-11-10T08:36:52Z",
            "title": "Installation of Microwave Long Haul products"
        },
        {
            "code": "IONE",
            "globalId": "66C9D4BA-BFD9-4489-A58B-615B5B8F7073",
            "isDeleted": false,
            "modifiedDate": "2020-11-10T08:36:52Z",
            "title": "Installation of Optical Network elements"
        },
        {
            "code": "IRA",
            "globalId": "E38F9260-DE1D-4E69-ABCC-7DF69D37FC58",
            "isDeleted": false,
            "modifiedDate": "2020-11-11T10:22:36Z",
            "title": "Installation of RBS Antenna Systems products"
        },
        {
            "code": "IRC",
            "globalId": "8FC4553F-01D1-4C79-99C8-0AAF4148D85C",
            "isDeleted": false,
            "modifiedDate": "2020-11-10T08:36:52Z",
            "title": "Installation of Radio cabinet"
        },
        {
            "code": "SBC",
            "globalId": "D1C3126B-5E7E-472D-A58F-356A10F8862F",
            "isDeleted": true,
            "modifiedDate": "2020-12-15T06:36:40Z",
            "title": "SBC_Test_ACG"
        },
        {
            "code": "TEST_B_123",
            "globalId": "EB286EEC-1311-4C19-85C1-CA26F0C24C85",
            "isDeleted": false,
            "modifiedDate": "2021-04-16T04:54:56Z",
            "title": "TEST_B_123"
        },
        {
            "code": "TRS-2",
            "globalId": "5B1697C3-4CBC-45A5-B109-C5A5B8A38FA8",
            "isDeleted": false,
            "modifiedDate": "2020-11-10T08:36:52Z",
            "title": "Test of Radio Site 2G"
        },
        {
            "code": "TRS-3",
            "globalId": "0183B5F8-B11A-4979-96F8-22E1BE0B52FD",
            "isDeleted": false,
            "modifiedDate": "2020-11-10T08:36:52Z",
            "title": "Test of Radio Site 3G"
        },
        {
            "code": "TRS-4",
            "globalId": "E1ABA2E1-5F43-469C-9CF3-513E8DE64428",
            "isDeleted": false,
            "modifiedDate": "2020-11-10T08:36:52Z",
            "title": "Test of Radio Site 4G"
        },
        {
            "code": "TEST123C",
            "globalId": "CFC7CAE1-3F05-411E-BE96-7DEEA7C14686",
            "isDeleted": false,
            "modifiedDate": "2021-01-25T11:43:18Z",
            "title": "Test123Title"
        },
        {
            "code": "TEST555",
            "globalId": "1C694753-DC64-4A1C-8CFB-6879DFB76048",
            "isDeleted": false,
            "modifiedDate": "2021-02-16T08:57:09Z",
            "title": "Test555"
        },
        {
            "code": "TEST667",
            "globalId": "18D0271E-75A3-4DA6-8BE6-0A383D261AA2",
            "isDeleted": false,
            "modifiedDate": "2020-12-15T06:28:42Z",
            "title": "Test668"
        },
        {
            "code": "UT_7910",
            "globalId": "87DCF5AA-2EDE-4E75-9642-E5A16E41B25B",
            "isDeleted": false,
            "modifiedDate": "2020-11-16T05:38:53Z",
            "title": "UT_7910"
        }
        ]
        }
    outputList =[]
    for i in input['acg']:
        values1=i
        for key,values in values1.items():
            if(values == "BSMP" and key== "code"):## value and key need be pass dynamically
                for key, values in values1.items():
                    if values == '':
                        outputList.append(key)
                return outputList


empty_key = main()
print(empty_key)














