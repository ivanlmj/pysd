from app import app, render_template
from app.modules import systemd


@app.route("/enabled")
def f_services_enabled():
    s = systemd.Systemd()
    data = s.services_config("enabled")
    page_title = "Enabled Services"
    return render_template("enabled.html", data=data, title=page_title)


@app.route("/disabled")
def f_services_disabled():
    s = systemd.Systemd()
    data = s.services_config("disabled")
    page_title = "Disabled Services"
    return render_template("disabled.html", data=data, title=page_title)


@app.route("/active")
def f_services_active():
    s = systemd.Systemd()
    data = s.services_state("active")
    page_title = "Active Services"
    return render_template("active.html", data=data, title=page_title)


@app.route("/inactive")
def f_services_inactive():
    s = systemd.Systemd()
    data = s.services_state("inactive")
    page_title = "Inactive Services"
    return render_template("inactive.html", data=data, title=page_title)


@app.route("/running")
def f_services_running():
    s = systemd.Systemd()
    data = s.services_state("running")
    page_title = "Running Services"
    return render_template("running.html", data=data, title=page_title)


@app.route("/exited")
def f_services_exited():
    s = systemd.Systemd()
    data = s.services_state("exited")
    page_title = "Exited Services"
    return render_template("exited.html", data=data, title=page_title)


@app.route("/dead")
def f_services_dead():
    s = systemd.Systemd()
    data = s.services_state("dead")
    page_title = "Dead Services"
    return render_template("dead.html", data=data, title=page_title)
