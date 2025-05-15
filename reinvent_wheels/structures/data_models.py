from functools import cached_property
from dataclasses import dataclass, fields


@dataclass(init=False)  # This line is unnecessary, just to show how you should use it
class EasyDataclass:
    """
    Examples of defining optional parameters:
        optional_param1: Optional[str] = None
        optional_param2: Optional[str]  # NOTE: Incorrect optional definition
        optional_param3: str | None = None
        optional_param4 | None  # NOTE: Incorrect optional definition
        optional_param5: str = field(default='abc')
        optional_param6: str = field()  # NOTE: Incorrect optional definition
        optional_param7: str = field(default='abc')

        optional_param99:
        @property
        def custom_attribute(self):
            return [1,2,3]

    How to use:
        - @dataclass(init=False)
        ^ init=False is to enable custom init
        - model = self.INPUT_MODEL(**inputs)
        - print(model.optional_param1)
        - model.inject_attributes(self); print(self.optional_param99)
    """

    def __init__(self, **kwargs):
        """ ^^ Don't forget to use @dataclass(init=False)
        This customization is to ignore undefined Class-attributes.
        """
        self._original_inputs = kwargs
        for attribute in fields(self):
            value = kwargs.get(attribute.name)
            if value is not None:
                setattr(self, attribute.name, value)
        self.__post_init__()
        # with "init=False", dataclass will be lazy (not raising error until it's used), so we force to raise it
        repr(self)

    def __post_init__(self):
        self.special_logic()

    def inject_attributes(self, target_object: object):
        for field in fields(self):
            value = getattr(self, field.name, None)
            setattr(target_object, field.name, value)
        # Also add "@property" into attributes
        for name, attribute in vars(type(self)).items():
            if isinstance(attribute, (property, cached_property)):
                value = getattr(self, name, None)
                setattr(target_object, name, value)
        # Also add custom-init properties in init function, e.g., "self.attr1 = 123"
        for name, value in vars(self).items():
            if not hasattr(target_object, name):
                setattr(target_object, name, value)

    def special_logic(self):
        # Generate some new attributes based on initialized parameters
        pass
