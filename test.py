import pytest
from modules import systemd

s = systemd.Systemd()

SERVICE = 'cron.service'

def test_active_services():
    assert type(s.active_services()) == list

def test_enabled_services():
    assert type(s.enabled_services()) == list

def test_is_enabled():
    assert type(s.is_enabled(SERVICE)) == bool
           
def test_is_active():
    assert type(s.is_active(SERVICE)) == bool
