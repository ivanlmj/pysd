from json import dumps
from app import app
from app.modules import systemd


@app.route("/api/v1.0/enabled")
def f_api_services_enabled():
    s = systemd.Systemd()
    data = s.services_config("enabled")
    return dumps(data)


@app.route("/api/v1.0/disabled")
def f_api_services_disabled():
    s = systemd.Systemd()
    data = s.services_config("disabled")
    return dumps(data)


@app.route("/api/v1.0/active")
def f_api_services_active():
    s = systemd.Systemd()
    data = s.services_state("active")
    return dumps(data)


@app.route("/api/v1.0/inactive")
def f_api_services_inactive():
    s = systemd.Systemd()
    data = s.services_state("inactive")
    return dumps(data)


@app.route("/api/v1.0/running")
def f_api_services_running():
    s = systemd.Systemd()
    data = s.services_state("running")
    return dumps(data)


@app.route("/api/v1.0/exited")
def f_api_services_exited():
    s = systemd.Systemd()
    data = s.services_state("exited")
    return dumps(data)


@app.route("/api/v1.0/dead")
def f_api_services_dead():
    s = systemd.Systemd()
    data = s.services_state("dead")
    return dumps(data)
