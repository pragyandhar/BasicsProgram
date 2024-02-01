class time:
    def minute(self, sec) -> int:
        self.sec = sec
        print(f"{self.sec}sec is {self.sec//60}min and {self.sec % 60}sec")

    def hour(self, sec):
        self.sec = sec
        print(f"TIME: {self.sec//3600}:{(self.sec %
              3600)//60}:{self.sec % 60}")


sec = int(input("Enter seconds: "))
timeconverter = time()
timeconverter.minute(sec)
timeconverter.hour(sec)
