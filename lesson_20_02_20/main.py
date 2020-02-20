from lesson_20_02_20.linkedlist import LinkedList
from lesson_20_02_20.structure_driver import JSONFileDriver
from lesson_20_02_20.sdfabric import SDFabric


if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_node(0, 'Привет')
    ll.insert_node(1, 'Python')

    # # для structure driver
    # ll.set_structure_driver(JSONFileDriver("test.txt"))
    # ll.save()

    # # для fabric driver
    # # driver_name = input('Please enter driver name >')
    # driver_name = 'json'
    # driver_builder = SDFabric().get_sd_driver(driver_name)
    #
    # ll.set_structure_driver(driver_builder.build())
    # ll.save()







