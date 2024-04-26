"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100

    >>> serial
    <SerialGenerator start=100 current=101>

    >>> serial.generate()
    101

    >>> serial
    <SerialGenerator start=100 current=102>

    >>> serial.reset()

    >>> serial
    <SerialGenerator start=100 current=100>

    """

    def __init__(self, start):
        """Start a new instance with a number to receive a steady stream of incremented numbers"""
        self.initial_start = start
        self.current = start - 1

    def __repr__(self):
        """Shows the serial generator data"""
        return f"<SerialGenerator start={self.initial_start} current={self.current + 1}>"

    def generate(self):
        """Increment then provide a serial when method is called"""
        self.current += 1
        return self.current
    
    def reset(self):
        """Reset the counter to the initialized value"""
        if self.current is not self.initial_start - 1:
            self.current = self.initial_start - 1
