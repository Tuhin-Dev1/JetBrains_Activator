import pyperclip
import platform
import subprocess
import os


def check_type(code):
    try:
        if code == 1:
            print("Pycharm License Activate")
            text = "pycharm30c210ef30ca681d992b95b0c083ea57-eyJsaWNlbnNlSWQiOiJweWNoYXJtMzBjMjEwZWYzMGNhNjgxZDk5MmI5NWIwYzA4M2VhNTciLCJsaWNlbnNlZU5hbWUiOiJBZnRlclNhbGUgVGVsZWdyYW0iLCJhc3NpZ25lZU5hbWUiOiJAamV0ZXJldGluZyIsImFzc2lnbmVlRW1haWwiOiIiLCJsaWNlbnNlUmVzdHJpY3Rpb24iOiJKZXRCcmFpbnMiLCJjaGVja0NvbmN1cnJlbnRVc2UiOnRydWUsInByb2R1Y3RzIjpbeyJjb2RlIjoiUEMiLCJmYWxsYmFja0RhdGUiOiIiLCJwYWlkVXBUbyI6IjIwMjUtMDMtMTEiLCJleHRlbmRlZCI6dHJ1ZX1dLCJtZXRhZGF0YSI6IjAxMjAyMzAxMDJQUEFBMDEzMDA5IiwiaGFzaCI6IjQxNDcyOTYxLzA6MTU2MzYwOTQ1MSIsImdyYWNlUGVyaW9kRGF5cyI6MCwiYXV0b1Byb2xvbmdhdGVkIjpmYWxzZSwiaXNBdXRvUHJvbG9uZ2F0ZWQiOmZhbHNlfQ==-K0llgnKEFs3TvStVQo4lWp3skwYSWA6wbKGbzwDOgXW1CSlQzxN/y0Mxz3S2A2HqqaldzPMYYgbpWEskWj7w1nzUlCIUl+R0+L9aT00UDRr1ouBqoXmpbxfq+m80UVMjiSX4hXtqqmMKgKH/PgNn1voTpnd5PynkSw/V3A93nmNJeJG9Es8w0Wi9TAqtG8Z99kAazY651ErDNcxAAOg97WgFXhs/6XqIO26NlEqJKST7tlXmpXySW2nzly4GzcB9OVuerNgXN2GRHlyAbCv40ty9J69LB/Ov9RNN58OmTKsiIyezQtRaPkMVNHdCNC+I1Un7Av5nWIxmrFzA2JT3pcOyWJjHrpYUC9S9yi/ArdkORlszdEn0IiVwh56AfM6YjF5dn9qnXaguxqEo1XD6iaclS/h1MDvHKmCX8XAOH/9Y4xC+FBRsMktQcON+CyWcDrfmg9eT8BvSVDSza7vQI4Qy8cGeTcwOQaAlJFaYKz3BJeIL31XRi7A8s7hNsngXOOwND7D78ulY/eTB336yMRJ2QvE87ARdNdyfvZx+mrcXblyT8N5OfvnU1WRlHXhegMGn0KQjY/vatjJ4TkeiVBAxGvGornTH9MqZCMYHneQY+4Ryev9qBQSaopVDFNt5zFuADIck96boeZYZEmDJk4gQdw+107rjB/Yspn+vSHc=-MIIEuTCCAqGgAwIBAgIGAY6TuckRMA0GCSqGSIb3DQEBCwUAMBgxFjAUBgNVBAMMDUpldFByb2ZpbGUgQ0EwIBcNMjQwMzMwMDg1NjUwWhgPMjEyNDAzMDcwODU2NTBaMCExHzAdBgNVBAMMFk5vdmljZS1mcm9tLTIwMjQtMDQtMDEwggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQC4zycY0O0AjrtYejv6QS4MnO/X2izUqGBpWLagJUiDuTFRxonrRF11jt0B93+PTqPszXO3J5wgsTJ4jlf7sRol6nz5lmQ6OrsZkUz6ktDp7LW2jkNLheZBl3yQASnQfI84ufd2TNp/fTpX+2EFmET/MES0xLKrDD5aP6u/SrdpvJRAwCmVppNJYuk+49kFu8kb8FN85FnV3zN1vzI30XbfHCqFSpsDAs0Y9RNez2E2My8vBQ3hGfndcp1fiFzllnC9Wk8OoXOha56k5/VcoCDMJ+8q4Hi8eDJ1WrF4+vj1MEP9yCmdVg258rmvtnCzR2AI2Aa0KhV5oMjrrgCqJaci0yTUo4jf6rzcW8y9RWoTg1ACJgcSWcGcyQ8W73Xd9AhloZqyaS9UTwclauP2XYaJ1PEAOyt1BoKybKIWMWS2kB0TNoVVSDBaOlTReAi60BN0S6UAch9LpFxguzArEhJ9fJnPxp3tRRx0sQBxUUmNl9z4vibpObPxa+f/Pf2eK81fSTdnGxBnBIZjomLzSBDQGgcO+p2NDlBI9mAQ/XS6hMwC8WnwZsXjltqNhDGHThbblcQdb/tNivUrhnzMIBmAlycJtAYZv4RmtDekd6P0IMHo5N1pe9o0o+20L7Dy6bTp5dss3Xhea3Se3hu5PdDldZdEnLzUq44/zTmLx9DgGQIDAQABMA0GCSqGSIb3DQEBCwUAA4ICAQBeKKDBqNdCgrf/+tV790YwltYYfC3sjhSslMzZ1vLUqQRw/hPSelEt2h9x7/L7/EHWKY7+tJ+vCH1lcjCw0NeYs1j4xml/uhbsLcdtQ73Wz5Tdk6DLgETPEre1dpkpNJck+iU/CHWNr2kPSA9IuC7+EpmVrtO4mRFbT1YW6yoB3VnN+7o81hDcM2OEvIoxWJ93tjgWkvltQ0IM5tAdgazWkFE+fehy4BYPdhezD+NlsJ3M5dkyaBMbOHPNg/xt7VFLCIgMcRoSxvIgdlZLx6hlpV2E4ef06EGQm0gErng3nkx4lwEFR11bRdFK+v3Ce8Ung90P9ulDaIk9NR8dR7zNJ7PHG9iYxxjIaLhA0qMuX3FwTASfZU+x+Ls4xiN17KC+pfVXzykh4DdkjGKWFvn1AGJSb6MjlL0nDpCUklaLrkLdXJHnZCujRXzKvm6hZzJeWpvBd0/bVvkuV+HdhnMAK4d6rAzwx+BZkr+0o7Lu9rc4i68AGBfpm01uS8STTHH0hdyrazVDXq8NSLQ9wagcSFr5Nxo8LuCPHp8Vi1wYjAftFWxdCf6c2lfaaM6uFA/e3I8it0Fa4tp3b+2BJ61aX8DafrkDdZYtt9tItpnkrgi+SfguguVVXmBid76nF/SNOkJ47dz7t9iEupcQximNc0GBiXilb94Jv+pR6he20g=="
            print(
                "One thing has been copied, now basically you go to Pycharm and activate Pycharm by submitting your code.")
            pyperclip.copy(text)

        elif code == 2:
            print("Again, as long as it hasn't arrived yet, you will actually get it.")

        elif code == 3:
            system = platform.system()
            if system == "Linux":
                print("The installation of Visual Studio Code on Linux is currently in progress.")
                commands = [
                    "sudo apt update",
                    "sudo apt install software-properties-common apt-transport-https curl",
                    "curl https://packages.microsoft.com/keys/microsoft.asc | sudo gpg --dearmor > /usr/share/keyrings/microsoft-archive-keyring.gpg",
                    "sudo sh -c 'echo \"deb [signed-by=/usr/share/keyrings/microsoft-archive-keyring.gpg] https://packages.microsoft.com/repos/vscode stable main\" > /etc/apt/sources.list.d/vscode.list'",
                    "sudo apt update",
                    "sudo apt install code"
                ]
                for cmd in commands:
                    subprocess.run(cmd, shell=True, check=True)

            elif system == "Windows":
                print("The installation of Visual Studio Code on Windows is currently in progress.")
                url = "https://update.code.visualstudio.com/latest/win32-x64-user/stable"
                installer_path = "C:\\Temp\\VSCodeSetup.exe"
                subprocess.run(["curl", "-L", url, "-o", installer_path], check=True)
                subprocess.run([installer_path, "/silent", "/mergetasks=desktopicon"], check=True)
                os.remove(installer_path)

            elif system == "Mac":
                print("The installation of Visual Studio Code on Mac is currently in progress.")
                subprocess.run(["brew", "install", "--cask", "visual-studio-code"], check=True)

        else:
            print("Invalid code. Please try again.")

    except Exception as e:
        if code == 1:
            print("Pycharm License Activate")
            text = "pycharm30c210ef30ca681d992b95b0c083ea57-eyJsaWNlbnNlSWQiOiJweWNoYXJtMzBjMjEwZWYzMGNhNjgxZDk5MmI5NWIwYzA4M2VhNTciLCJsaWNlbnNlZU5hbWUiOiJBZnRlclNhbGUgVGVsZWdyYW0iLCJhc3NpZ25lZU5hbWUiOiJAamV0ZXJldGluZyIsImFzc2lnbmVlRW1haWwiOiIiLCJsaWNlbnNlUmVzdHJpY3Rpb24iOiJKZXRCcmFpbnMiLCJjaGVja0NvbmN1cnJlbnRVc2UiOnRydWUsInByb2R1Y3RzIjpbeyJjb2RlIjoiUEMiLCJmYWxsYmFja0RhdGUiOiIiLCJwYWlkVXBUbyI6IjIwMjUtMDMtMTEiLCJleHRlbmRlZCI6dHJ1ZX1dLCJtZXRhZGF0YSI6IjAxMjAyMzAxMDJQUEFBMDEzMDA5IiwiaGFzaCI6IjQxNDcyOTYxLzA6MTU2MzYwOTQ1MSIsImdyYWNlUGVyaW9kRGF5cyI6MCwiYXV0b1Byb2xvbmdhdGVkIjpmYWxzZSwiaXNBdXRvUHJvbG9uZ2F0ZWQiOmZhbHNlfQ==-K0llgnKEFs3TvStVQo4lWp3skwYSWA6wbKGbzwDOgXW1CSlQzxN/y0Mxz3S2A2HqqaldzPMYYgbpWEskWj7w1nzUlCIUl+R0+L9aT00UDRr1ouBqoXmpbxfq+m80UVMjiSX4hXtqqmMKgKH/PgNn1voTpnd5PynkSw/V3A93nmNJeJG9Es8w0Wi9TAqtG8Z99kAazY651ErDNcxAAOg97WgFXhs/6XqIO26NlEqJKST7tlXmpXySW2nzly4GzcB9OVuerNgXN2GRHlyAbCv40ty9J69LB/Ov9RNN58OmTKsiIyezQtRaPkMVNHdCNC+I1Un7Av5nWIxmrFzA2JT3pcOyWJjHrpYUC9S9yi/ArdkORlszdEn0IiVwh56AfM6YjF5dn9qnXaguxqEo1XD6iaclS/h1MDvHKmCX8XAOH/9Y4xC+FBRsMktQcON+CyWcDrfmg9eT8BvSVDSza7vQI4Qy8cGeTcwOQaAlJFaYKz3BJeIL31XRi7A8s7hNsngXOOwND7D78ulY/eTB336yMRJ2QvE87ARdNdyfvZx+mrcXblyT8N5OfvnU1WRlHXhegMGn0KQjY/vatjJ4TkeiVBAxGvGornTH9MqZCMYHneQY+4Ryev9qBQSaopVDFNt5zFuADIck96boeZYZEmDJk4gQdw+107rjB/Yspn+vSHc=-MIIEuTCCAqGgAwIBAgIGAY6TuckRMA0GCSqGSIb3DQEBCwUAMBgxFjAUBgNVBAMMDUpldFByb2ZpbGUgQ0EwIBcNMjQwMzMwMDg1NjUwWhgPMjEyNDAzMDcwODU2NTBaMCExHzAdBgNVBAMMFk5vdmljZS1mcm9tLTIwMjQtMDQtMDEwggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQC4zycY0O0AjrtYejv6QS4MnO/X2izUqGBpWLagJUiDuTFRxonrRF11jt0B93+PTqPszXO3J5wgsTJ4jlf7sRol6nz5lmQ6OrsZkUz6ktDp7LW2jkNLheZBl3yQASnQfI84ufd2TNp/fTpX+2EFmET/MES0xLKrDD5aP6u/SrdpvJRAwCmVppNJYuk+49kFu8kb8FN85FnV3zN1vzI30XbfHCqFSpsDAs0Y9RNez2E2My8vBQ3hGfndcp1fiFzllnC9Wk8OoXOha56k5/VcoCDMJ+8q4Hi8eDJ1WrF4+vj1MEP9yCmdVg258rmvtnCzR2AI2Aa0KhV5oMjrrgCqJaci0yTUo4jf6rzcW8y9RWoTg1ACJgcSWcGcyQ8W73Xd9AhloZqyaS9UTwclauP2XYaJ1PEAOyt1BoKybKIWMWS2kB0TNoVVSDBaOlTReAi60BN0S6UAch9LpFxguzArEhJ9fJnPxp3tRRx0sQBxUUmNl9z4vibpObPxa+f/Pf2eK81fSTdnGxBnBIZjomLzSBDQGgcO+p2NDlBI9mAQ/XS6hMwC8WnwZsXjltqNhDGHThbblcQdb/tNivUrhnzMIBmAlycJtAYZv4RmtDekd6P0IMHo5N1pe9o0o+20L7Dy6bTp5dss3Xhea3Se3hu5PdDldZdEnLzUq44/zTmLx9DgGQIDAQABMA0GCSqGSIb3DQEBCwUAA4ICAQBeKKDBqNdCgrf/+tV790YwltYYfC3sjhSslMzZ1vLUqQRw/hPSelEt2h9x7/L7/EHWKY7+tJ+vCH1lcjCw0NeYs1j4xml/uhbsLcdtQ73Wz5Tdk6DLgETPEre1dpkpNJck+iU/CHWNr2kPSA9IuC7+EpmVrtO4mRFbT1YW6yoB3VnN+7o81hDcM2OEvIoxWJ93tjgWkvltQ0IM5tAdgazWkFE+fehy4BYPdhezD+NlsJ3M5dkyaBMbOHPNg/xt7VFLCIgMcRoSxvIgdlZLx6hlpV2E4ef06EGQm0gErng3nkx4lwEFR11bRdFK+v3Ce8Ung90P9ulDaIk9NR8dR7zNJ7PHG9iYxxjIaLhA0qMuX3FwTASfZU+x+Ls4xiN17KC+pfVXzykh4DdkjGKWFvn1AGJSb6MjlL0nDpCUklaLrkLdXJHnZCujRXzKvm6hZzJeWpvBd0/bVvkuV+HdhnMAK4d6rAzwx+BZkr+0o7Lu9rc4i68AGBfpm01uS8STTHH0hdyrazVDXq8NSLQ9wagcSFr5Nxo8LuCPHp8Vi1wYjAftFWxdCf6c2lfaaM6uFA/e3I8it0Fa4tp3b+2BJ61aX8DafrkDdZYtt9tItpnkrgi+SfguguVVXmBid76nF/SNOkJ47dz7t9iEupcQximNc0GBiXilb94Jv+pR6he20g=="
            print(
                "One thing has been copied, now basically you go to Pycharm and activate Pycharm by submitting your code.")
            pyperclip.copy(text)

        elif code == 2:
            print("Again, as long as it hasn't arrived yet, you will actually get it.")

        elif code == 3:
            system = platform.system()
            if system == "Linux":
                print("The installation of Visual Studio Code on Linux is currently in progress.")
                commands = [
                    "sudo apt update",
                    "sudo apt install software-properties-common apt-transport-https curl",
                    "curl https://packages.microsoft.com/keys/microsoft.asc | sudo gpg --dearmor > /usr/share/keyrings/microsoft-archive-keyring.gpg",
                    "sudo sh -c 'echo \"deb [signed-by=/usr/share/keyrings/microsoft-archive-keyring.gpg] https://packages.microsoft.com/repos/vscode stable main\" > /etc/apt/sources.list.d/vscode.list'",
                    "sudo apt update",
                    "sudo apt install code"
                ]
                for cmd in commands:
                    subprocess.run(cmd, shell=True, check=True)

            elif system == "Windows":
                print("The installation of Visual Studio Code on Windows is currently in progress.")
                url = "https://update.code.visualstudio.com/latest/win32-x64-user/stable"
                installer_path = "C:\\Temp\\VSCodeSetup.exe"
                subprocess.run(["curl", "-L", url, "-o", installer_path], check=True)
                subprocess.run([installer_path, "/silent", "/mergetasks=desktopicon"], check=True)
                os.remove(installer_path)

            elif system == "Mac":
                print("The installation of Visual Studio Code on Mac is currently in progress.")
                subprocess.run(["brew", "install", "--cask", "visual-studio-code"], check=True)

        else:
            print("Invalid code. Please try again.")
