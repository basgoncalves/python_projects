
import platform

def import_repos():
    device_details = platform.uname()

    # list of directories where repos are stored depending on current local machine
    if device_details.node == 'Bas-PC':
        repos =[r'C:\Git\Papers-Reviews',
                r'C:\Git\Python_projects',
                r'C:\Git\MSKmodelling',
                r'C:\Git\msk_modelling_python',
                r'C:\Git\research_data']
    elif device_details.node == 'DESKTOP-8KRF896':
        repos =[r'C:\Git\Papers-Reviews',
                r'C:\Git\Python_projects',
                r'C:\Git\MSKmodelling',
                r'C:\Git\msk_modelling_python',
                r'C:\Git\research_data']
    else:
        repos = []
        print('Current machine not configured. Add folder paths to the script or perform "git pull manually"')
            
    return repos