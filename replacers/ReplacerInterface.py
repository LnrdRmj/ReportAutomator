from asyncio.windows_events import NULL

class ReplacerInterface: 

    def __init__ (self):
        self.next = NULL

    # Sets the next handler
    def setNext(self, newReplacer):
        self.next = newReplacer

    def handle(self, paragraph):
        if (self.next != NULL):
            self.next.handle(paragraph)

    # Override this method
    def canHandleRequest(self):
        return False
