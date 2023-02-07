from bs4 import BeautifulSoup

c="""<!DOCTYPE html>
<html lang="en" style="margin: 0;padding: 0;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;">
 <head style="margin: 0;padding: 0;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;">
  <meta charset="utf-8"/>
  <meta content="width=760, initial-scale=1.0" name="viewport"/>
  <meta content="ie=edge" http-equiv="X-UA-Compatible"/>
  <title>
   Document
  </title>
  <style>
   * {
            margin: 0;
            padding: 0;
            font-family: Arial, Helvetica, sans-serif;
            text-shadow: 0.2px 0.2px 0.5px black;
        }
        .container {
            padding: 10px 20px;
        }
        table {
            text-align: left;
            border-collapse: collapse;
            width: 100%;
        }
        table tr td {
            border: 1px solid;
            padding: 2px 10px;
        }
        table tr td.noBorder {
            border: none;
        }
        table tr td:nth-child(1) {
            width: calc(calc(100% / 13) * 4);
        }
        table tr td:nth-child(2),
        table tr td:nth-child(3),
        table tr td:nth-child(4),
        table tr td:nth-child(6) {
            width: calc(calc(100% / 13) * 2);
        }
        table tr td:nth-child(5) {
            width: calc(calc(100% / 13) * 1);
        }
        .space {
            margin: 30px;
        }
        ._center {
            text-align: center !important;
        }
        ._left {
            text-align: left !important;
        }
        ._right {
            text-align: right !important;
        }
        .green {
            background-color: #00b050;
        }
        .red {
            background-color: #ff0000;
        }
        .orange {
            background-color: #e26b09;
        }
        .blue {
            background-color: #00b0f0;
        }
        .silver {
            background-color: #bfbfbf;
        }
        .yellow {
            background-color: #ffff00;
        }
        .pink {
            background-color: #fabf8f;
        }
        p {
            margin-bottom: 30px;
        }
        .tooltip {
            position: relative;
            display: inline-block;
            border: none;
            height: 20px;
            width: 21px;
            float: right;
        }
  </style>
 </head>
 <body style="margin: 0;padding: 0;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;">
  <div style="margin: 0;padding: 10px 20px;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;">
   <p style="margin: 0;padding: 0;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;margin-bottom: 30px;">
    Subject: Test Suite Jenkins_Suite executed successfully at 2022-09-01 12:09:13 Thursday . 1/2 test cases
        passed
   </p>
   <table border="1" style="margin: 0;padding: 0;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;text-align: left;border-collapse: collapse;border: none;border-color: black;width: 100%;">
    <tr style="margin: 0;padding: 0;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;">
     <td bgcolor="#00b050" style="margin: 0;padding: 2px 10px;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;background-color: #00b050;width: calc(calc(100% / 13) * 4);">
      Passed
     </td>
     <td bgcolor="#ff0000" colspan="2" style="margin: 0;padding: 2px 10px;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;background-color: #ff0000;width: calc(calc(100% / 13) * 2);">
      Failed
     </td>
     <td bgcolor="#bfbfbf" colspan="2" style="margin: 0;padding: 2px 10px;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;background-color: #bfbfbf;width: calc(calc(100% / 13) * 2);">
      Total
     </td>
    </tr>
    <tr style="margin: 0;padding: 0;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;">
     <td bgcolor="#00b050" style="margin: 0;padding: 2px 10px;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;text-align: right;background-color: #00b050;width: calc(calc(100% / 13) * 4);">
      <span style="display: flex;justify-content: flex-end;">
       1
      </span>
     </td>
     <td bgcolor="#ff0000" colspan="2" style="margin: 0;padding: 2px 10px;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;text-align: right;background-color: #ff0000;width: calc(calc(100% / 13) * 2);">
      <span style="display: flex;justify-content: flex-end;">
       1
      </span>
     </td>
     <td bgcolor="#bfbfbf" colspan="2" style="margin: 0;padding: 2px 10px;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;text-align: right;background-color: #bfbfbf;width: calc(calc(100% / 13) * 2);">
      <span style="display: flex;justify-content: flex-end;">
       2
      </span>
     </td>
    </tr>
    <tr style="margin: 0;padding: 0;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;">
     <td colspan="3" style="margin: 0;padding: 2px 10px;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;border: none;width: calc(calc(100% / 13) * 4);">
     </td>
    </tr>
    <tr style="margin: 0;padding: 0;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;">
     <td bgcolor="ffff00" colspan="6" style="height: 40px;vertical-align: bottom;margin: 0;padding: 2px 10px;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;background-color: #ffff00;width: calc(calc(100% / 13) * 4);">
      TestSuite: Jenkins_Suite
      <span style="margin: 0;padding: 0;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;">
       Run
                        on [Local] / [Linux] / [Chrome 99.0.4844.74]
      </span>
      <span style="margin: 30px;padding: 0;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;">
      </span>
      <span style="margin: 0;padding: 0;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;">
       Overall
                        Status : Partial
      </span>
      <span style="margin: 30px;padding: 0;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;">
      </span>
     </td>
    </tr>
    <tr style="margin: 0;padding: 0;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;">
     <td bgcolor="#fabf8f" style="margin: 0;padding: 2px 10px;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;background-color: #fabf8f;width: calc(calc(100% / 13) * 4);">
      Test Case Name
     </td>
     <td bgcolor="#fabf8f" style="margin: 0;padding: 2px 10px;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;background-color: #fabf8f;width: calc(calc(100% / 13) * 2);">
      Start Time
     </td>
     <td bgcolor="#fabf8f" style="margin: 0;padding: 2px 10px;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;background-color: #fabf8f;width: calc(calc(100% / 13) * 2);">
      End Time
     </td>
     <td bgcolor="#fabf8f" style="margin: 0;padding: 2px 10px;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;background-color: #fabf8f;width: calc(calc(100% / 13) * 2);">
      Status
     </td>
     <td bgcolor="#fabf8f" style="margin: 0;padding: 2px 10px;font-family: Arial, Helvetica, sans-serif;text-shadow: 0.2px 0.2px 0.5px black;background-color: #fabf8f;width: calc(calc(100% / 13) * 2);">
      Message
     </td>
    </tr>
    <tr>
     <td>
      <div style="border: none;">
       <a href="https://u7854476.ct.sendgrid.net/ls/click?upn=5PY1nk9KbD-2Fp-2FPtgpyhknHXFtrqjCfpdEUT-2FKwXnODX0EzVi0HopE5ytnc-2B5jBa4z9QhreNFLw3uLD2AELcLx2jhRBkW5srBwRaJnXIyxMOcIf-2BKcH-2FaRk6CCz6mY-2B4sgyNWbdXjKuV1r9J-2BZfwt0-2B3Oe1P3NraJM5ZtbYaQQC5ubUEOSctyQOsIBZ92I1eZ8Vb6MjMMSN19Nn8YnvaPR5VhAh05onixhLYZAY81iVcKc6k5238S4MSLp2R9lkjE8h3ivN8gnIfkFSL0-2FIgKdGWMj3DwLSWX5I1u5ujejrg-3DXZVm_AymHPpTrxfT-2Bdnw7aDIlGhwCmvuCBENvQEHFr67-2BrX6r4pJQyOjWFov4ZhHhHMJyXDidqyFfGR2jvQRHs-2BJ-2FYXcjUka0-2FjJAAGJOxql0W1pFEwVD06Lc6N7EWtaP0Web8f-2FtT1hR8xhBx3yQXxdRK5UjLSPcknGUGZ8GsdlhE9fILmDcCdQbiEdA2l4DWZTyZ19tXdCMFQoV-2FvAhW2zlLddPlXhZhuwyafzWYiNL26g-3D">
        jenkins_Integration_1
       </a>
       <span class="tooltip" title="">
        <span style="padding: 0px 6px;border: 1px solid black;display:inline-block;border-radius:50%;background-color:#00b0f0;font-size: 16px;font-family:serif;line-height: 1;cursor: default;">
         i
        </span>
       </span>
      </div>
     </td>
     <td class="_right">
      <div style="float: left;">
       2022-09-01 12:08:48 Thursday
      </div>
     </td>
     <td class="_right">
      <div style="float: left;">
       2022-09-01 12:09:07 Thursday
      </div>
     </td>
     <td class="_right">
      <div style="float: left;">
       FAILED
      </div>
     </td>
     <td class="">
      <div style="float: left;">
       Success
      </div>
     </td>
     <tr>
      <td>
       <div style="border: none;">
        <a href="https://u7854476.ct.sendgrid.net/ls/click?upn=5PY1nk9KbD-2Fp-2FPtgpyhknHXFtrqjCfpdEUT-2FKwXnODX0EzVi0HopE5ytnc-2B5jBa45jzKtGM9Q4Bq2SwVcLxLHZ-2FEP0CBZmqRBnbsftReaCUxUM3X5JSN3TapcyKYavJuIZCM55yuQ2y-2FsbCSMyt4yuLOZ3-2BVMSS0A-2F7GsPaoKMSxnhMC-2B87BmGdmnEapk4JFgYtRQB8cDlLUk7R-2FTt6DNjtPIVzhYuZSaEAFGxC434TjObR8pmDiMRiE7YbvSZlPElJt59mRYg-2FYKMB9LP4cKMC69hZPQmN70-2FgJZZtlCVk-3DLnNm_AymHPpTrxfT-2Bdnw7aDIlGhwCmvuCBENvQEHFr67-2BrX6r4pJQyOjWFov4ZhHhHMJyXDidqyFfGR2jvQRHs-2BJ-2FYYBYUFMFiyJMTYbcLGPDzE4i4SPXy9TG-2B19Ck0OrwYxz7MrpnLJUNTguw-2F9F5rRD8YtAtVQpQEjD5twet-2Fwchjaq5zbxAexVTxC-2BBK-2F4zvziCtoXyJm0MMYNlzcBPmDQkubQEvt7i2xqx1XcEPSioo4-3D">
         jenkins_Integration_2
        </a>
        <span class="tooltip" title="">
         <span style="padding: 0px 6px;border: 1px solid black;display:inline-block;border-radius:50%;background-color:#00b0f0;font-size: 16px;font-family:serif;line-height: 1;cursor: default;">
          i
         </span>
        </span>
       </div>
      </td>
      <td class="_right">
       <div style="float: left;">
        2022-09-01 12:08:48 Thursday
       </div>
      </td>
      <td class="_right">
       <div style="float: left;">
        2022-09-01 12:09:13 Thursday
       </div>
      </td>
      <td class="_right">
       <div style="float: left;">
        FAILED
       </div>
      </td>
      <td class="">
       <div style="float: left;">
        Failed at step 3
       </div>
      </td>
     </tr>
    </tr>
   </table>
  </div>
  <img alt="" border="0" height="1" src="https://u7854476.ct.sendgrid.net/wf/open?upn=V6vX9e003JsVTXbWBWSpX-2FhCDlu6dtavD5C4FVbZENLPguO4KBRUYn2c-2BZpg4FmJnmmXYpmfQMsu2s75BqJaxmBY4E4zmVVik9N7MF-2By9cUz2yo-2FDvztxp1ZadRlN1QEAQXApTzwUz1607g8VWUofvorpRenYsnw1IpRtnokd0lEqxswZ6qKPk3-2FtUMv3yu6VbhMKNWS4d9PDvL-2BQ7CFQg7kDsP3-2BJgXrdW04neAmFA-3D" style="height:1px !important;width:1px !important;border-width:0 !important;margin-top:0 !important;margin-bottom:0 !important;margin-right:0 !important;margin-left:0 !important;padding-top:0 !important;padding-bottom:0 !important;padding-right:0 !important;padding-left:0 !important;" width="1"/>
 </body>
</html>"""

soup = BeautifulSoup(c, "html.parser")
a=soup.find('table')
row=a.find_all('div')
##print(row)
rowlen=int(len(row)/5)

for i in range(0,rowlen):
    val=i+1;number=val *5;j=number-2
    Status=row[j].text.strip()
    if(Status=="FAILED"):
        k=number-5
        url=row[k].a.get('href')
        #print(type(url))
        name=row[k].a.text.strip()
        if val==1:
            valueUpdated1="""<h2>FAILED TESTCASE LINKS</h2>""";
            print(valueUpdated1)
        valueUpdated="""<a href="{}">{}</a>""".format(url,name)
        print(valueUpdated)






