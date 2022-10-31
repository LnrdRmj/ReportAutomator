from asyncio.windows_events import NULL

class ReplacerInterface: 

    def __init__ (self, stringToReplace):
        self.next = NULL
        self.stringToReplace = stringToReplace

    # Sets the next handler
    def setNext(self, newReplacer):
        self.next = newReplacer

    def handle(self, paragraph):
        if (self.next != NULL):
            self.next.handle(paragraph)

    def getStringToReplace(self):
        return self.stringToReplace

    # Override this method
    def canHandleRequest(self):
        return False

    def canHandleRequest(self, paragraph):
        return (self.getStringToReplace() in paragraph.text)