import IPython.display as ipd
import ipywidgets as widgets
from aksharify import AksharArt
from distributions import Normal, Exponential

def normal(img):
    m = widgets.FloatSlider(min=0, max=1, step=0.02, value=0.5, description='mean:')
    v = widgets.FloatSlider(min=-10, max=10, step=0.1, value=1, description='var:')
    output = widgets.Output()
    def handle_slider_change(change):
        with output:
            output.clear_output()
            norm = Normal(mean=m.value, var=v.value)
            art = AksharArt(img, norm)
            art.aksharify()
            art.show(False)
    m.observe(handle_slider_change, 'value')
    v.observe(handle_slider_change, 'value')
    ipd.display(m, v, output)


def exponential(img):
    p = widgets.FloatSlider(min=-5, max=5, step=0.02, value=1, description='power:')
    output = widgets.Output()
    def handle_slider_change(change):
        with output:
            output.clear_output()
            expo = Exponential(power=p.value)
            art = AksharArt(img, expo)
            art.aksharify()
            art.show(False)
    p.observe(handle_slider_change, 'value')
    ipd.display(p, output)