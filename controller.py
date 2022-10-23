import findemployee
import input
import logg
import salary
import adder
import delete_number

def work_with_phonk():
    a = input.show_menu()

    if a == 1:
        name = input.last_name()
        findemployee.PersonFinder(name)
        logg.log_info(name)
    elif a == 2:
        job = input.PostJob()
        findemployee.PersonFinder(job)
        logg.log_info(job)
    elif a == 3:
        zarplata = input.zp()
        salary.SalWal(zarplata)
        logg.log_info(zarplata)
    elif a == 4:
        person = input.AddPer()
        adder.impo(person)
        logg.log_info(person)
    elif a ==  5:
        choz = input.DelPerson()
        delete_number.delit(choz)
        logg.log_info(str(choz))
    elif a == 6:
        ...