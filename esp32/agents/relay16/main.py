# Relay16 Agent v0.1.0
# ESP 32
import machine
import utime
import utils

try:
    import picoweb
except ImportError:
    print('Getting picoweb...')
    import upip
    upip.install('picoweb')
    upip.install('pycopy-ulogging')

# agent = utils.Agent()
app = picoweb.WebApp(__name__)
led = machine.Pin(15, machine.Pin.OUT, value=0)
# relay = machine.Pin(26, machine.Pin.OUT)


print('Relay16 agent is ready!')
print(wlan.ifconfig())


@app.route("/", methods=['POST'])
def query(request, response):
    if request.method == "POST":
        yield from request.read_form_data()
    else:  # GET, apparently
        # Note: parse_qs() is not a coroutine, but a normal function.
        # But you can call it using yield from too.
        request.parse_qs()

    # Whether form data comes from GET or POST request, once parsed,
    # it's available as req.form dictionary

    yield from picoweb.start_response(response)
    yield from response.awrite("Hello %s!" % request.form["name"])


app.run(debug=True, host="0.0.0.0")


# while True:
#     # print(agent.__dict__)
#     led.value(1)

#     if relay():
#         relay.value(0)
#     else:
#         relay.value(1)

#     utime.sleep(10)
