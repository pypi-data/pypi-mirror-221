# coding: utf-8

"""
Interfaces contain low level implementations that interact with CAN hardware.
"""

import warnings
from pkg_resources import iter_entry_points


# interface_name => (module, classname)
BACKENDS = {
    'kvaser':           ('minican.interfaces.kvaser',           'KvaserBus'),
    'socketcan':        ('minican.interfaces.socketcan',        'SocketcanBus'),
    'serial':           ('minican.interfaces.serial.serial_can','SerialBus'),
    'pcan':             ('minican.interfaces.pcan',             'PcanBus'),
    'bmcan':            ('minican.interfaces.bmcan',            'BmCanBus'),
    'usb2can':          ('minican.interfaces.usb2can',          'Usb2canBus'),
    'ixxat':            ('minican.interfaces.ixxat',            'IXXATBus'),
    'nican':            ('minican.interfaces.nican',            'NicanBus'),
    'iscan':            ('minican.interfaces.iscan',            'IscanBus'),
    'virtual':          ('minican.interfaces.virtual',          'VirtualBus'),
    'neovi':            ('minican.interfaces.ics_neovi',        'NeoViBus'),
    'vector':           ('minican.interfaces.vector',           'VectorBus'),
    'slcan':            ('minican.interfaces.slcan',            'slcanBus'),
    'canalystii':       ('minican.interfaces.canalystii',       'CANalystIIBus'),
    'systec':           ('minican.interfaces.systec',           'UcanBus')
}

BACKENDS.update({
    interface.name: (interface.module_name, interface.attrs[0])
    for interface in iter_entry_points('minican.interface')
})

# Old entry point name. May be removed >3.0.
for interface in iter_entry_points('python_can.interface'):
    BACKENDS[interface.name] = (interface.module_name, interface.attrs[0])
    warnings.warn('{} is using the deprecated python_can.interface entry point. '.format(interface.name) +
                  'Please change to minican.interface instead.', DeprecationWarning)

VALID_INTERFACES = frozenset(list(BACKENDS.keys()) + ['socketcan_native', 'socketcan_ctypes'])
