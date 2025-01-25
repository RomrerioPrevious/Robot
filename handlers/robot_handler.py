from models.enums import Dir


def read_barcode() -> str:
    result = ""

    brick.encoder("E2").reset()

    brick.motor("M2").setPower(78)
    brick.motor("M1").setPower(70)

    while True:
        if brick.sensor("A2").read() > self.grey and brick.sensor("A1").read() > self.grey:
            break
        script.wait(50)

    enk = brick.encoder("E2").read()

    brick.encoder("E2").reset()

    while True:
        if brick.sensor("A2").read() < self.grey and brick.sensor("A1").read() < self.grey:
            break
        script.wait(50)

    enk = (enk + brick.encoder("E2").read()) / 2

    while not (brick.encoder("E2").read() > enk):
        script.wait(10)

    for i in range(6):
        while not (brick.encoder("E2").read() > enk / 2):
            script.wait(10)

        if brick.sensor("A2").read() < self.grey:
            result += "0"
        else:
            result += "1"

        while not (brick.encoder("E2").read() > enk / 2):
            script.wait(10)


    brick.stop()
    return

def follow_route(route: [Dir], my_dir: Dir = Dir.none):
    start = 0
    if my_dir == Dir.none:
        my_dir = route[0]

        if my_dir == Dir.down:
            right()
        elif my_dir == Dir.up:
            left()
        go()
        start = 1

    for i in range(start, len(route)):
        dir = route[i]
        n = Dir.relate(my_dir, dir)
        if n == Dir.right:
            right()
        elif n == Dir.left:
            left()
        go()

    script.wait(5000)

def go():
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
            brick.motor("M1").setPower(100)
            brick.motor("M2").setPower(80)


def right():
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

def left():
    brick.motor("M1").powerOff()
    brick.motor("M2").powerOff()
    brick.motor("M3").powerOff()
    brick.motor("M4").powerOff()

    script.wait(100)

    brick.motor("M2").setPower(-50)
    brick.motor("M1").setPower((50))

    while True:
        if brick.sensor("A2").read() < self.grey:
            break
        script.wait(5)

    while True:
        if brick.sensor("A2").read() > self.grey:
            break
        script.wait(5)

    while True:
        if brick.sensor("A2").read() < self.grey:
            break
        script.wait(5)

    brick.motor("M1").powerOff()
    brick.motor("M2").powerOff()
    brick.motor("M3").powerOff()
    brick.motor("M4").powerOff()

    script.wait(1000)

    brick.stop()
    return

def make_sound():
    ...


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
        brick.motor("M1").setPower(100)

        brick.motor("M2").setPower(80)

    script.wait(5)