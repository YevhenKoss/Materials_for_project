import Change_App
import Clean_Folder


def return_cf():
    return Clean_Folder.main()


def return_ca():
    return Change_App.change_app()


if __name__ == '__main__':
    return_ca()
    return_cf()