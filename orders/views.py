from django.shortcuts import render, render_to_response, get_object_or_404
from orders.models import OrderItem, Order
from .forms import Order_Create_Form
from cart.cart import Cart
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import Order_Serializer
# from .serializers import Order_Item_Serializer
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail


class Order_List_View(generics.ListAPIView):

    queryset = Order.objects.all()
    serializer_class = Order_Serializer


class Order_Create_View(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):

        order = Order_Serializer(data=request.data)

        if order.is_valid():

            order.save

            return Response({"status": "Create"})




@staff_member_required
def Admin_Order_Detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html', {'order': order})

def Mail(order_id):

    order = Order.objects.get(id=order_id)
    subject = 'Заказ c номером {}'.format(order.id)
    message = 'Дорогой, {}, вы успешно сделали заказ.\
               Номер вашего заказа {}'.format(order.first_name, order.id)

    mail_send = send_mail(subject, message, 'admin@myshop.ua', [order.email])

    subject_2 = 'Поступил новый заказ {}'.format(order.id)
    message_2 = 'Новый заказ на суму {}'.format(order.get_total_cost)
    admin_email = 'admin_email@com.ua'

    mail_send_2 = send_mail(subject_2, message_2, 'admin@myshop.ua', [admin_email])

    return (mail_send, mail_send_2)

def Order_Create(request):

    cart = Cart(request)

    if request.method == 'POST':
        form = Order_Create_Form(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.cupon:
                order.cupon = cart.cupon
                order.discount = cart.cupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()

            Mail(order.id)

            return render_to_response( 'orders/order/created.html', {'order': order})

    else:
        form = Order_Create_Form()
        return render(request, 'orders/order/create.html', {'cart': cart,
                                                            'form': form})
