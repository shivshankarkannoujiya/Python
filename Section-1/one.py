def make_chai():
    if kettle_has_water():
        fill_kettle()
    plug_in_kettle()
    boil_water()

    if not is_cup_clean():
        wash_cup()
    add_to_cup("tea leaves")
    add_to_cup("sugar")
    pour("boiled water")
    stie("cup")
    serve("chai")


# function need to be call for executing the code
make_chai()