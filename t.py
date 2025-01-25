import sys
import time
import random
import math


class Program():
    __interpretation_started_timestamp__ = time.time() * 1000

    pi = 3.141592653589793
    grey = None

    def execMain(self):

        self.grey = 100
        while True:
            if (brick.sensor("A1").read() > self.grey):
                if (brick.sensor("A2").read() > self.grey):
                    brick.motor("M1").setPower(80)
                    brick.motor("M2").setPower(80)

                else:
                    brick.motor("M2").setPower(100)

                    brick.motor("M1").setPower(80)

            else:
                if not (brick.sensor("A2").read() > self.grey):
                    brick.motor("M3").setPower(50)
                    brick.motor("M4").setPower(50)

                    script.wait(300)

                    self.grey = 100
                    brick.motor("M1").powerOff()
                    brick.motor("M2").powerOff()
                    brick.motor("M3").powerOff()
                    brick.motor("M4").powerOff()

                    script.wait(100)

                    brick.motor("M2").setPower(50)

                    brick.motor("M1").setPower(-(50))

                    while True:
                        if brick.sensor("A1").read() < self.grey:
                            break
                        script.wait(5)

                    while True:
                        if brick.sensor("A1").read() > self.grey:
                            break
                        script.wait(5)

                    while True:
                        if brick.sensor("A1").read() < self.grey:
                            break
                        script.wait(5)

                    brick.motor("M1").powerOff()
                    brick.motor("M2").powerOff()
                    brick.motor("M3").powerOff()
                    brick.motor("M4").powerOff()

                    script.wait(1000)

                    brick.stop()
                    return
                    break
                brick.motor("M1").setPower(100)

                brick.motor("M2").setPower(80)

            script.wait(5)


def main():
    program = Program()
    program.execMain()


if __name__ == '__main__':
    main()
