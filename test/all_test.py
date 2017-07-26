import unittest

import bibliopixel
import bibliopixel.layout.geometry
import bibliopixel.project.data_maker
import bibliopixel.remote.server

from bibliopixel import (
    animation,
    colors,
    font,
    gamma,
    image,
    layout,
    log,
    matrix,
    util,
)

from bibliopixel.controllers import (
    gamepad,
    # serial_gamepad,
)

from bibliopixel.drivers import (
    SPI,
    # SimPixel,
    driver_base,
    dummy_driver,
    hue,
    network,
    network_receiver,
    network_udp,
    return_codes,
    serial,
)

from bibliopixel.main import (
    all_pixel,
    clear_cache,
    color,
    common_flags,
    demo,
    demo_table,
    devices,
    help,
    main,
    run,
    set,
    show,
    simpixel,
    update,
)


class ImportAllTest(unittest.TestCase):
    def test_all(self):
        # We pass just by successfully importing everything above.
        pass
