from dataclasses import dataclass


@dataclass
class Human:
    name: str
    age: int

    # @dataclass will automatically create __init__ method, so we don't need to define it
    # @dataclass will automatically create __repr__ method, so we don't need to define it
    # @dataclass will automatically create __eq__ method, so we don't need to define it


anuj = Human(name="Anuj", age=25)
print(anuj.name, anuj.age)
print(anuj)

ravi = Human(name="Ravi", age=30)
print(anuj == ravi)