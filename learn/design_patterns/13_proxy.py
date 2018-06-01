"""
The Proxy pattern provides a surrogate or placeholder for another object to control access to it.
It can be used for lazy initialization, access control, logging, or monitoring.
"""


class RealSubject:
    def request(self):
        return "RealSubject: Handling request."


class Proxy:
    def __init__(self, real_subject):
        self.real_subject = real_subject

    def request(self):
        print("Proxy: Logging request.")
        return self.real_subject.request()


# Usage
real = RealSubject()
proxy = Proxy(real)
print(proxy.request())
