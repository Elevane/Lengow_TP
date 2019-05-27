from xml.dom import minidom
import urllib.request
from django.shortcuts import render
from django.template import loader
from .models import Order


# Create your views here.
def index(request):
    template = loader.get_template('orders/index.html')
    return render()


#orders view
def show(request):
    dborder = Order()
    url = 'http://test.lengow.io/orders-test.xml'  # define XML location
    dom = minidom.parse(urllib.request.urlopen(url))  # parse the data
    elements = []
    order = dom.getElementsByTagName('count_by_status')
    for em in order:
        elements.append(dom.getElementsByTagName('cancel'))
        dborder.cancel = dom.getElementsByTagName('cancel')
        elements.append(dom.getElementsByTagName('new'))
        dborder.new = dom.getElementsByTagName('new')
        elements.append(dom.getElementsByTagName('shipped'))
        dborder.shipped = dom.getElementsByTagName('shipped')
        elements.append(dom.getElementsByTagName('processing'))
        dborder.processing = dom.getElementsByTagName('processing')

        dborder.save()

    return render(request, 'orders/index.html', {'elements': elements})