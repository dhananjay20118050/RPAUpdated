from django.db import models
from django.db.models import Q
from model_utils import Choices

ORDER_COLUMN_CHOICES = Choices(
    ('0', 'id'),
    ('1', 'name'),
    ('2', 'ip'),
    ('3', 'port'),
    ('4', 'updated_at'),
    ('5', 'created_at'),
    ('6', 'process_id'),
)


# Create your models here.
class Nodes(models.Model):
    name = models.CharField(max_length=100)  # blank=False
    ip = models.CharField(max_length=100)  # blank=False
    port = models.CharField(max_length=100, default="", null=False)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    process_id = models.IntegerField()

    class Meta:
        db_table = "nodes"


def query_nodes_by_args(**kwargs):
    draw = int(kwargs.get('draw', None)[0])
    length = int(kwargs.get('length', None)[0])
    start = int(kwargs.get('start', None)[0])
    search_value = kwargs.get('search[value]', None)[0]
    order_column = kwargs.get('order[0][column]', None)[0]
    order = kwargs.get('order[0][dir]', None)[0]

    order_column = ORDER_COLUMN_CHOICES[order_column]
    if order == 'desc':
        order_column = '-' + order_column

    queryset = Nodes.objects.all()
    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(id=search_value) |
                                   Q(name__icontains=search_value) |
                                   Q(ip__icontains=search_value) |
                                   Q(port__icontains=search_value) |
                                   Q(updated_at__icontains=search_value) |
                                   Q(created_at__icontains=search_value) |
                                   Q(process_id__icontains=search_value))

    count = queryset.count()
    queryset = queryset.order_by(order_column)[start:start + length]
    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }


class Hubs(models.Model):
    name = models.CharField(max_length=100)  # blank=False
    ip = models.CharField(max_length=100)  # blank=False
    port = models.CharField(max_length=100, default="", null=False)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    process_id = models.IntegerField()

    class Meta:
        db_table = "hubs"
