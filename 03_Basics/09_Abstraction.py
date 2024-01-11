from abc import ABC, abstractmethod, abstractproperty


class skelton(ABC):
    @abstractproperty
    def dsm_class(self):
        pass

    @abstractproperty
    def mentor_name(self):
        pass

    @abstractproperty
    def class_timing(self):
        pass

    @abstractproperty
    def class_material(self):
        pass


# implementation
# dev -1
class pwskills_mentor(skelton):
    @property
    def dsm_class(self):
        print("This is function of dsm class")

    @property
    def mentor_name(self):
        print("This is s funn of mentor name")

    @property
    def class_timing(self):
        pass

    @property
    def class_material(self):
        pass


obj_pwskills_mentor = pwskills_mentor()
obj_pwskills_mentor.dsm_class()
