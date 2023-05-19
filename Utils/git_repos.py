
import platform

def import_repos():
    device_details = platform.uname()
    name_pc = device_details.node
    # list of directories where repos are stored depending on current local machine
    if name_pc == 'Bas-PC' or name_pc == 'DESKTOP-8KRF896':
        repos =[r'C:\Git\Papers-Reviews',
                r'C:\Git\Python_projects',
                r'C:\Git\MSKmodelling',
                r'C:\Git\msk_modelling_python',
                r'C:\Git\research_data',
                r'C:\Git\Kira_MSc_data',
                r'C:\Git\OpenSimOutputToMAT-main']
    else:
        repos = []
        print('Current machine not configured. Add folder paths to the script or perform "git pull manually"')
            
    return repos